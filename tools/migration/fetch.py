"""Politely mirror NAM-IP/Infos articles and their images into ./cache.

One request at a time, with a pause between requests (the origin server is slow).
Already cached files are never fetched again, so the script can be resumed.
Usage: python fetch.py [--delay 4]
"""
import argparse
import json
import random
import re
import sys
import time

import requests
from bs4 import BeautifulSoup

from common import BASE, CACHE, IMAGES, INDEX, PAGES, cache_name, decode, parse_article_name

session = requests.Session()
session.headers["User-Agent"] = "Mozilla/5.0 (archive migration script)"
last_request = 0.0


def get(path: str, delay: float) -> bytes | None:
    global last_request
    wait = delay + random.uniform(0, 1) - (time.time() - last_request)
    if wait > 0:
        time.sleep(wait)
    url = BASE + path.replace("\\", "/")
    try:
        r = session.get(url, timeout=90)
    except requests.RequestException as e:
        print(f"  ERROR {url}: {e}", flush=True)
        return None
    finally:
        last_request = time.time()
    if r.status_code != 200:
        print(f"  HTTP {r.status_code} {url}", flush=True)
        return None
    return r.content


def fetch_to(path: str, dest, delay: float, log: dict) -> bool:
    if dest.exists():
        return True
    data = get(path, delay)
    log[path] = "ok" if data is not None else "missing"
    if data is None:
        return False
    dest.write_bytes(data)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--delay", type=float, default=4.0)
    args = ap.parse_args()
    PAGES.mkdir(parents=True, exist_ok=True)
    IMAGES.mkdir(parents=True, exist_ok=True)
    logfile = CACHE / "fetch-log.json"
    log = json.loads(logfile.read_text("utf-8")) if logfile.exists() else {}

    index_file = PAGES / cache_name(INDEX)
    fetch_to(INDEX, index_file, args.delay, log)
    soup = BeautifulSoup(decode(index_file.read_bytes()), "html.parser")

    articles = {}
    for a in soup.find_all("a", href=True):
        if parse_article_name(a["href"]):
            articles.setdefault(cache_name(a["href"]), a["href"])
    print(f"{len(articles)} articles in index", flush=True)

    images = {}
    for i, (key, href) in enumerate(sorted(articles.items()), 1):
        dest = PAGES / key
        new = not dest.exists()
        if fetch_to(href, dest, args.delay, log) and new:
            print(f"[{i}/{len(articles)}] page {href}", flush=True)
        if dest.exists():
            page = BeautifulSoup(decode(dest.read_bytes()), "html.parser")
            for img in page.find_all("img", src=True):
                src = img["src"].strip()
                if not re.match(r"https?:", src):
                    images.setdefault(cache_name(src), src)
        logfile.write_text(json.dumps(log, indent=1), "utf-8")

    # Follow "Voir la suite" sub-pages that are not listed in the index.
    extra = {}
    todo = list(articles)
    while todo:
        key = todo.pop()
        if not (PAGES / key).exists():
            continue
        page = BeautifulSoup(decode((PAGES / key).read_bytes()), "html.parser")
        for a in page.find_all("a", href=True):
            sub = cache_name(a["href"])
            if parse_article_name(sub) and sub not in articles and sub not in extra:
                extra[sub] = a["href"]
                if fetch_to(a["href"], PAGES / sub, args.delay, log):
                    print(f"  sub-page {a['href']}", flush=True)
                    todo.append(sub)
                    sp = BeautifulSoup(decode((PAGES / sub).read_bytes()), "html.parser")
                    for img in sp.find_all("img", src=True):
                        src = img["src"].strip()
                        if not re.match(r"https?:", src):
                            images.setdefault(cache_name(src), src)
    (CACHE / "subpages.json").write_text(json.dumps(extra, indent=1), "utf-8")
    print(f"{len(extra)} sub-pages", flush=True)

    print(f"{len(images)} distinct images referenced", flush=True)
    for i, (key, src) in enumerate(sorted(images.items()), 1):
        dest = IMAGES / key
        new = not dest.exists()
        if fetch_to(src, dest, args.delay, log) and new:
            print(f"[{i}/{len(images)}] image {src}", flush=True)
        if i % 10 == 0:
            logfile.write_text(json.dumps(log, indent=1), "utf-8")
    logfile.write_text(json.dumps(log, indent=1), "utf-8")
    missing = [k for k, v in log.items() if v == "missing"]
    print(f"done; {len(missing)} missing: {missing}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
