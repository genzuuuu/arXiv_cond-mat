import argparse
import datetime
import os
import time

import feedparser
from openai import OpenAI

from email_sender import send_digest_email, smtp_configured

DEMO_URL = "https://genzuuuu.github.io/arXiv_cond-mat/"
REPO_URL = "https://github.com/genzuuuu/arXiv_cond-mat/"

SYSTEM_PROMPTS = {
    "en": (
        "The user will send today's arXiv condensed matter physics papers. "
        "Summarize the key theoretical, computational, and experimental advances in English. "
        "Group by topic, include paper links, and keep the tone concise and readable."
    ),
    "zh": (
        "用户将发送今天 arXiv 凝聚态物理相关论文。请用中文总结今日重要进展，"
        "涵盖新的理论、计算和实验工作。按主题分组，保留文章链接，语言简洁易读。"
    ),
}


def get_feed_update_date(feed):
    for key in ("published_parsed", "updated_parsed"):
        parsed = feed.feed.get(key)
        if parsed:
            return datetime.datetime.fromtimestamp(time.mktime(parsed))
    raise ValueError("Could not determine arXiv feed update date")


def build_paper_content(feed):
    content = ""
    for i, entry in enumerate(feed.entries):
        title = entry["title"]
        abstract = entry["summary"].split("Abstract: ")[-1]
        author = entry.get("author", "")
        content += (
            f"[{i + 1}]. [*{title}*]({entry['link']} \"{title}\")\n"
            f"{author}\n{abstract}\n\n"
        )
    return content


def build_file_header(day, update_date, lang):
    if lang == "zh":
        return (
            f"### 自动更新 arXiv 凝聚态物理文章\n"
            f"  - **代码更新时间** {day.isoformat()}\n"
            f"  - **arXiv 更新时间** {update_date.isoformat()}\n"
            f"  - **demo 页面** [arXiv 凝聚态物理每日导读]({DEMO_URL})\n"
            f"  - **源代码** [GitHub 仓库]({REPO_URL})\n"
        )
    return (
        f"### Daily arXiv Condensed Matter Digest\n"
        f"  - **Generated at** {day.isoformat()}\n"
        f"  - **arXiv update** {update_date.isoformat()}\n"
        f"  - **Demo** [arXiv cond-mat daily digest]({DEMO_URL})\n"
        f"  - **Source** [GitHub repo]({REPO_URL})\n"
    )


def summarize(client, papers, model, lang, update_date):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPTS[lang]},
        {"role": "user", "content": papers},
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=False,
        extra_body={"thinking": {"type": "disabled"}},
    )
    summary = response.choices[0].message.content or ""
    if not summary.strip():
        raise ValueError(f"Empty {lang} summary from model")
    return summary


def generate_summary(api_key, base_url, model, papers, lang, update_date):
    if not api_key:
        fallback = "### 未配置 API key，以下是 arXiv 原文\n\n" if lang == "zh" else "### No API key configured. Raw arXiv feed:\n\n"
        return fallback + papers

    try:
        client = OpenAI(api_key=api_key, base_url=base_url)
        return summarize(client, papers, model, lang, update_date)
    except Exception as exc:
        print(f"LLM error ({lang}): {exc}")
        fallback = "### LLM 运行出错，以下是 arXiv 原文\n\n" if lang == "zh" else "### LLM error. Raw arXiv feed:\n\n"
        return fallback + papers


def save_markdown(path, header, summary):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{header}\n{summary}")


def main(api_key, base_url, model, send_email=False):
    day = datetime.datetime.now()
    feed = feedparser.parse("https://rss.arxiv.org/rss/cond-mat")
    if not feed.entries:
        raise ValueError("Failed to fetch arXiv feed")

    update_date = get_feed_update_date(feed)
    if update_date.date() != day.date():
        print(f"No new arXiv feed for today ({day.date()}); skipping.")
        return

    papers = build_paper_content(feed)
    date_str = day.strftime("%Y-%m-%d")

    save_markdown(f"data/{date_str}_origin.md", "", papers)

    summary_en = generate_summary(api_key, base_url, model, papers, "en", update_date)
    summary_zh = generate_summary(api_key, base_url, model, papers, "zh", update_date)

    header_en = build_file_header(day, update_date, "en")
    header_zh = build_file_header(day, update_date, "zh")

    save_markdown(f"data/{date_str}_en.md", header_en, summary_en)
    save_markdown(f"data/{date_str}_zh.md", header_zh, summary_zh)
    save_markdown(f"data/{date_str}.md", header_en, summary_en)
    save_markdown("README.md", header_en, summary_en)

    if send_email or smtp_configured():
        send_digest_email(
            subject=f"arXiv cond-mat Daily Digest | 凝聚态每日导读 ({date_str})",
            summary_en=summary_en,
            summary_zh=summary_zh,
            meta={
                "arxiv_update": update_date.isoformat(),
                "generated_at": day.isoformat(),
                "demo_url": DEMO_URL,
                "repo_url": REPO_URL,
            },
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_key", default=os.environ.get("API_KEY", ""))
    parser.add_argument("--base_url", default=os.environ.get("BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--model", default=os.environ.get("MODEL", "deepseek-v4-flash"))
    parser.add_argument("--send_email", action="store_true")
    args = parser.parse_args()
    main(
        api_key=args.api_key,
        base_url=args.base_url,
        model=args.model,
        send_email=args.send_email,
    )
