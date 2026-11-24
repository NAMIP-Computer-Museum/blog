"""Shared helpers for the pionnier.nam-ip.be migration."""
import re
from pathlib import Path

BASE = "http://pionnier.nam-ip.be/"
INDEX = "NAM-IP-Infos.html"
HERE = Path(__file__).resolve().parent
CACHE = HERE / "cache"
PAGES = CACHE / "pages"
IMAGES = CACHE / "images"
REPO = HERE.parent.parent

ARTICLE_RE = re.compile(
    r"^NAM-ip-INFO(\d{4})(\d{2})-([A-Za-z]+)((?:\d+(?:-\d+)*[A-Za-z]{0,2})?)\.html$", re.I
)

THEMES = {
    "edito": "Éditorial",
    "pres": "Préservation",
    "expos": "Exposition",
    "rech": "Recherche",
    "acq": "Acquisition",
    "cr": "Comptes rendus",
    "news": "Nouvelles",
    "communique": "Communiqué",
}


def decode(data: bytes) -> str:
    """Pages declare UTF-8 but often contain cp1252 bytes."""
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("cp1252", errors="replace")


def cache_name(href: str) -> str:
    """Case-insensitive, Windows-safe cache filename for a site-relative path."""
    return href.replace("\\", "/").split("/")[-1].lower()


def parse_article_name(href: str):
    m = ARTICLE_RE.match(href.split("/")[-1])
    if not m:
        return None
    year, issue, code, num = m.groups()
    num = num or ""
    return {
        "year": int(year),
        "issue": int(issue),
        "code": code.lower(),
        "num": num,
        "slug": f"{year}-{issue}-{code.lower()}{num.lower()}",
    }
