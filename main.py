import argparse
import os

from digest import run_digest


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True, help="Digest profile id, e.g. cond-mat or embodied-ai")
    parser.add_argument("--api_key", default=os.environ.get("API_KEY", ""))
    parser.add_argument("--base_url", default=os.environ.get("BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--model", default=os.environ.get("MODEL", "deepseek-v4-flash"))
    parser.add_argument("--send_email", action="store_true")
    args = parser.parse_args()
    run_digest(
        profile_id=args.profile,
        api_key=args.api_key,
        base_url=args.base_url,
        model=args.model,
        send_email=args.send_email,
    )
