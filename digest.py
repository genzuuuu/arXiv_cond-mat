import datetime
import os
import re
import time
from dataclasses import dataclass

import feedparser
import yaml
from openai import OpenAI

from email_sender import send_digest_email, smtp_configured

PROFILES_DIR = os.path.join(os.path.dirname(__file__), "profiles")

LINK_CITATION_RULES = """
Citation rules (mandatory):
- Every paper must include a clickable markdown link copied from the input URL field.
- Use exactly: [Paper Title](https://arxiv.org/abs/XXXX.XXXXX)
- Do NOT use bare indices like [12], **[12]**, (12), or [Title (12)] without the arXiv URL.
""".strip()


@dataclass
class DigestProfile:
    id: str
    name_en: str
    name_zh: str
    feed_urls: list[str]
    data_dir: str
    readme_path: str
    demo_url: str
    repo_url: str
    email_subject: str
    system_prompt_en: str
    system_prompt_zh: str


def load_profile(profile_id: str) -> DigestProfile:
    path = os.path.join(PROFILES_DIR, f"{profile_id}.yaml")
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return DigestProfile(**data)


def get_feed_update_date(feed):
    for key in ("published_parsed", "updated_parsed"):
        parsed = feed.feed.get(key)
        if parsed:
            return datetime.datetime.fromtimestamp(time.mktime(parsed))
    raise ValueError("Could not determine arXiv feed update date")


def fetch_merged_feed(feed_urls: list[str]):
    entries = []
    seen_links = set()
    update_dates = []

    for url in feed_urls:
        feed = feedparser.parse(url)
        if not feed.entries:
            print(f"Warning: no entries from {url}")
            continue
        try:
            update_dates.append(get_feed_update_date(feed))
        except ValueError:
            print(f"Warning: could not parse update date from {url}")
        for entry in feed.entries:
            link = entry.get("link", "")
            if link and link not in seen_links:
                seen_links.add(link)
                entries.append(entry)

    if not entries:
        raise ValueError(f"Failed to fetch arXiv feeds: {feed_urls}")

    update_date = max(update_dates) if update_dates else datetime.datetime.now()
    return entries, update_date


def build_paper_index(entries):
    return {
        i + 1: {"title": entry["title"].strip(), "link": entry["link"].strip()}
        for i, entry in enumerate(entries)
    }


def inject_paper_links(summary: str, entries) -> str:
    index = build_paper_index(entries)
    if not index:
        return summary

    def linked_citation(number: int, title: str | None = None) -> str | None:
        paper = index.get(number)
        if not paper:
            return None
        label = title or paper["title"]
        return f"[{label}]({paper['link']})"

    def replace_title_with_number(match):
        title = match.group(1).strip()
        number = int(match.group(2))
        citation = linked_citation(number, title)
        return citation if citation else match.group(0)

    def replace_bold_number(match):
        number = int(match.group(1))
        citation = linked_citation(number)
        return f"**{citation}**" if citation else match.group(0)

    def replace_bare_number(match):
        number = int(match.group(1))
        citation = linked_citation(number)
        return citation if citation else match.group(0)

    def replace_bold_title_with_number(match):
        citation = linked_citation(int(match.group(2)), match.group(1).strip())
        return f"**{citation}**" if citation else match.group(0)

    # **[Title (290)]** or **[Title(290)]**
    summary = re.sub(
        r"\*\*\[([^\]]+?)\s*\((\d+)\)\]\*\*",
        replace_bold_title_with_number,
        summary,
    )
    # [Title (290)] without bold
    summary = re.sub(
        r"(?<!\()\[([^\]]+?)\s*\((\d+)\)\](?!\()",
        replace_title_with_number,
        summary,
    )
    # **[290]**
    summary = re.sub(r"\*\*\[(\d+)\]\*\*", replace_bold_number, summary)
    # bare [12] not already part of a markdown link
    summary = re.sub(r"\[(\d+)\](?!\()", replace_bare_number, summary)

    return summary


def build_paper_content(entries):
    content = ""
    for i, entry in enumerate(entries):
        title = entry["title"]
        abstract = entry["summary"].split("Abstract: ")[-1]
        author = entry.get("author", "")
        link = entry["link"]
        content += (
            f"### Paper [{i + 1}]\n"
            f"Title: {title}\n"
            f"URL: {link}\n"
            f"Authors: {author}\n"
            f"Abstract: {abstract}\n\n"
        )
    return content


def build_file_header(profile: DigestProfile, day, update_date, lang):
    if lang == "zh":
        return (
            f"### 自动更新 {profile.name_zh}\n"
            f"  - **代码更新时间** {day.isoformat()}\n"
            f"  - **arXiv 更新时间** {update_date.isoformat()}\n"
            f"  - **demo 页面** [{profile.name_zh}]({profile.demo_url})\n"
            f"  - **源代码** [GitHub 仓库]({profile.repo_url})\n"
        )
    return (
        f"### {profile.name_en}\n"
        f"  - **Generated at** {day.isoformat()}\n"
        f"  - **arXiv update** {update_date.isoformat()}\n"
        f"  - **Demo** [{profile.name_en}]({profile.demo_url})\n"
        f"  - **Source** [GitHub repo]({profile.repo_url})\n"
    )


def summarize(client, papers, model, system_prompt):
    full_prompt = f"{system_prompt.strip()}\n\n{LINK_CITATION_RULES}"
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": full_prompt},
            {"role": "user", "content": papers},
        ],
        stream=False,
        extra_body={"thinking": {"type": "disabled"}},
    )
    summary = response.choices[0].message.content or ""
    if not summary.strip():
        raise ValueError("Empty summary from model")
    return summary


def generate_summary(api_key, base_url, model, papers, system_prompt, lang):
    if not api_key:
        fallback = (
            "### 未配置 API key，以下是 arXiv 原文\n\n"
            if lang == "zh"
            else "### No API key configured. Raw arXiv feed:\n\n"
        )
        return fallback + papers

    try:
        client = OpenAI(api_key=api_key, base_url=base_url)
        return summarize(client, papers, model, system_prompt)
    except Exception as exc:
        print(f"LLM error ({lang}): {exc}")
        fallback = (
            "### LLM 运行出错，以下是 arXiv 原文\n\n"
            if lang == "zh"
            else "### LLM error. Raw arXiv feed:\n\n"
        )
        return fallback + papers


def save_markdown(path, header, summary):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{header}\n{summary}")


def run_digest(profile_id: str, api_key: str, base_url: str, model: str, send_email: bool = False):
    profile = load_profile(profile_id)
    day = datetime.datetime.now()
    entries, update_date = fetch_merged_feed(profile.feed_urls)

    if update_date.date() != day.date():
        print(f"[{profile_id}] No new arXiv feed for today ({day.date()}); skipping.")
        return False

    papers = build_paper_content(entries)
    date_str = day.strftime("%Y-%m-%d")

    save_markdown(f"{profile.data_dir}/{date_str}_origin.md", "", papers)

    summary_en = generate_summary(
        api_key, base_url, model, papers, profile.system_prompt_en, "en"
    )
    summary_zh = generate_summary(
        api_key, base_url, model, papers, profile.system_prompt_zh, "zh"
    )

    summary_en = inject_paper_links(summary_en, entries)
    summary_zh = inject_paper_links(summary_zh, entries)

    header_en = build_file_header(profile, day, update_date, "en")
    header_zh = build_file_header(profile, day, update_date, "zh")

    save_markdown(f"{profile.data_dir}/{date_str}_en.md", header_en, summary_en)
    save_markdown(f"{profile.data_dir}/{date_str}_zh.md", header_zh, summary_zh)
    save_markdown(f"{profile.data_dir}/{date_str}.md", header_en, summary_en)
    save_markdown(profile.readme_path, header_en, summary_en)

    if send_email or smtp_configured():
        send_digest_email(
            subject=f"{profile.email_subject} ({date_str})",
            summary_en=summary_en,
            summary_zh=summary_zh,
            meta={
                "title": profile.name_en,
                "arxiv_update": update_date.isoformat(),
                "generated_at": day.isoformat(),
                "demo_url": profile.demo_url,
                "repo_url": profile.repo_url,
            },
        )

    print(f"[{profile_id}] Digest generated for {date_str}")
    return True
