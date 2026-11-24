"""Convert the cached pionnier.nam-ip.be articles into Hugo page bundles.

Offline: reads ./cache only (run fetch.py first). Re-runnable: rewrites content/posts.
Usage: python convert.py [--dry-run]
"""
import argparse
import difflib
import json
import re
import shutil
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

from urllib.parse import unquote

import yaml
from PIL import Image, ImageOps
from bs4 import BeautifulSoup, Comment, NavigableString, Tag
from markdownify import MarkdownConverter

from common import (BASE, HERE, IMAGES, INDEX, PAGES, REPO, THEMES, cache_name,
                    decode, parse_article_name)

POSTS = REPO / "content" / "posts"
TITLES = {}  # filled in main() from titles.yaml
ISSUE_DATES = {1: "03-31", 2: "06-30", 3: "09-30", 4: "12-31"}
# Site chrome images that are not article content.
CHROME_IMAGES = {"yjnam-ip-logo2017r.jpg", "nam-iplogo.png", "empreinte.png"}
CHROME_IMAGE_RE = re.compile(r"^h[e]?a?rd?er?img|^headerimg|^hearderimg", re.I)

report = defaultdict(list)


# ---------------------------------------------------------------- helpers

def clean_space(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("\xa0", " ")).strip()


def fold(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"[^a-z0-9 ]", " ", "".join(c for c in s if not unicodedata.combining(c)))


def toml_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def load_yaml(name):
    p = HERE / name
    return (yaml.safe_load(p.read_text("utf-8")) or {}) if p.exists() else {}


# ---------------------------------------------------------------- index

def parse_index():
    """Return ordered list of article dicts with issue, rubrique label, title, authors."""
    soup = BeautifulSoup(decode((PAGES / cache_name(INDEX)).read_bytes()), "html.parser")
    articles, seen = [], set()
    current = None
    order = defaultdict(int)
    for el in soup.find_all(["h3", "a"]):
        if el.name == "h3":
            m = re.search(r"(\d{4})\s*/\s*(\d)", el.get_text())
            if m:
                current = (int(m.group(1)), int(m.group(2)))
            continue
        href = el.get("href", "")
        info = parse_article_name(href)
        if not info:
            continue
        key = cache_name(href)
        if key in seen:
            report["doublon dans l'index"].append(href)
            continue
        seen.add(key)
        if current and current != (info["year"], info["issue"]):
            report["section d'index ≠ nom de fichier"].append(
                f"{href} listé sous {current[0]}/{current[1]}")
        # Author: text after the link up to the next link / <br>.
        tail = []
        for sib in el.next_siblings:
            if isinstance(sib, Tag) and sib.name in ("a", "br", "td", "tr"):
                break
            tail.append(sib.get_text() if isinstance(sib, Tag) else str(sib))
        m = re.search(r"\bpar\s+(.+)", clean_space(" ".join(tail)))
        authors = split_authors(m.group(1)) if m else []
        info.update(
            href=href, key=key, index_title=clean_space(el.get_text(" ")).lstrip("•·- ").strip(),
            index_authors=authors,
        )
        order[(info["year"], info["issue"])] += 1
        info["ordre"] = order[(info["year"], info["issue"])]
        articles.append(info)
    return articles


def safe_image_name(cached: str) -> str:
    """URL-safe bundle filename: no accents, spaces or %xx; BMP becomes PNG."""
    name = unicodedata.normalize("NFKD", unquote(cached))
    name = "".join(c for c in name if not unicodedata.combining(c)).lower()
    name = re.sub(r"[^a-z0-9._-]+", "-", name)
    return re.sub(r"\.bmp$", ".png", name)


def split_authors(s: str):
    s = s.strip(" ,;•·")
    parts = re.split(r"\s*(?:,|\bet\b|&)\s*", s)
    return [p.strip() for p in parts if p.strip()]


def add_subpages(arts):
    """'Voir la suite' pages not listed in the index: attach them after their parent."""
    p = HERE / "cache" / "subpages.json"
    if not p.exists():
        return
    by_key = {a["key"]: a for a in arts}
    subs = json.loads(p.read_text("utf-8"))
    # Which cached page links to each sub-page (first linking page = parent).
    linked_from = {}
    for key in list(by_key) + sorted(subs):
        f = PAGES / key
        if not f.exists():
            continue
        for href in re.findall(r'href="([^"]+\.html)"', decode(f.read_bytes()), re.I):
            sub = cache_name(href)
            if sub in subs and sub != key:
                linked_from.setdefault(sub, key)
    children = defaultdict(int)
    for key in sorted(subs):
        href = subs[key]
        info = parse_article_name(href)
        root = linked_from.get(key)
        while root in subs and linked_from.get(root) not in (None, key):
            root = linked_from[root]          # sub-page of a sub-page: climb to the article
        parent = by_key.get(root) or next(
            (a for a in arts if a["year"] == info["year"] and a["issue"] == info["issue"]
             and a["code"] == info["code"]), None)
        children[parent["key"] if parent else None] += 1
        info.update(href=href, key=key, index_title=None,
                    index_authors=parent["index_authors"] if parent else [],
                    ordre=round((parent["ordre"] if parent else 99) + 0.1 * children[parent["key"] if parent else None], 2),
                    parent=parent["key"] if parent else None)
        report["sous-page « voir la suite » (hors index)"].append(
            f"{href} → parent {parent['href'] if parent else '?'}")
        arts.append(info)


# ---------------------------------------------------------------- page parsing

class MD(MarkdownConverter):
    # markdownify 0.13.x signatures: (el, text, convert_as_inline)
    def convert_img(self, el, text, convert_as_inline):
        src = el.get("data-local")
        if not src:
            return ""
        alt = clean_space(el.get("alt", "")).replace("[", "(").replace("]", ")")
        return f"![{alt}]({src})"

    def convert_a(self, el, text, convert_as_inline):
        href = el.get("href", "")
        if not text.strip():
            return text
        if href.startswith("{{<"):
            return f"[{text.strip()}]({href})"
        return super().convert_a(el, text, convert_as_inline)


def md(node) -> str:
    return MD(heading_style="ATX", bullets="-", strip=["span", "font", "section", "div"],
              escape_underscores=False, escape_misc=False,
              newline_style="BACKSLASH").convert_soup(node)


def extract_content(html: str):
    m = re.search(r'<!--\s*#BeginEditable\s+"content"\s*-->(.*?)<!--\s*#EndEditable', html, re.S | re.I)
    body = m.group(1) if m else html
    return BeautifulSoup(body, "html.parser")


def localize_links(soup, by_key, art, images_used):
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        target = cache_name(href.split("#")[0]) if not re.match(r"(https?:|mailto:)", href, re.I) else None
        if target and target in by_key and (PAGES / target).exists():
            other = by_key[target]
            a["href"] = '{{< relref "/posts/%d/%s" >}}' % (other["year"], other["slug"])
            art["links_to"].add(target)
        elif re.search(r"(?:^|[\s:])www\.", href):
            # e.g. "voir :%20www.sigcis.org/files/x.pdf" — missing scheme.
            a["href"] = "https://" + unquote(href)[unquote(href).index("www."):].strip()
        elif target and re.search(r"\.(jpe?g|png|gif|bmp)$", target, re.I):
            # Link to a full-size image: handled with the image itself.
            a["data-image-link"] = target
        elif target:
            a["href"] = BASE + href.replace("\\", "/")
            report["lien vers page non-article (gardé vers pionnier)"].append(f"{art['slug']}: {href}")
    for img in soup.find_all("img", src=True):
        name = cache_name(img["src"].strip())
        if name in CHROME_IMAGES or CHROME_IMAGE_RE.match(name):
            img.decompose()
            continue
        if (IMAGES / name).exists():
            safe = safe_image_name(name)
            img["data-local"] = safe
            art["images"][safe] = name
            images_used.add(name)
        else:
            report["image manquante sur le site source"].append(f"{art['slug']}: {img['src']}")
            img.decompose()


def image_caption(img):
    a = img.find_parent("a")
    cap = (a.get("title") if a else None) or img.get("title") or img.get("alt") or ""
    cap = clean_space(cap)
    return "" if re.fullmatch(r"(?i)(image|photo|img|logo\S*)?\s*\d*", cap) else cap


def galleries_to_shortcode(soup, placeholders):
    """Replace image blocks by a placeholder later expanded to a {{< galerie >}} block."""
    blocks = soup.find_all(class_=re.compile(r"gallery|galerie", re.I))
    # Also: plain paragraphs that only hold several images.
    for p in soup.find_all("p"):
        if p not in blocks and len(p.find_all("img")) >= 2 and not clean_space(p.get_text(" ")):
            blocks.append(p)
    for block in blocks:
        imgs = [(i["data-local"], image_caption(i)) for i in block.find_all("img") if i.get("data-local")]
        if not imgs:
            continue
        lines = "\n".join(f"{f} | {c}" if c else f for f, c in imgs)
        token = f"GALERIE{len(placeholders)}X"
        placeholders[token] = "{{< galerie >}}\n" + lines + "\n{{< /galerie >}}"
        new = soup.new_tag("p")
        new.string = token
        block.replace_with(new)


def normalize_whitespace(soup):
    for c in soup.find_all(string=lambda t: isinstance(t, Comment)):
        c.extract()
    for t in soup.find_all(string=True):
        if t.find_parent("pre"):
            continue
        new = re.sub(r"[ \t\r\n\xa0]+", " ", str(t))
        if new != str(t):
            t.replace_with(NavigableString(new))


ITALIC_CLASSES = {"txt1ji", "txt1jital"}
BOLD_CLASSES = {"txt1jbold", "txt1b", "titlisteboldnews"}
HEADING_CLASSES = {"txt1lb13": "h2", "txt1lb12": "h3"}


def apply_class_styles(soup):
    """The source encodes formatting with (now undefined) CSS classes: make it semantic."""
    for el in soup.find_all(class_=True):
        classes = set(el.get("class", []))
        text = clean_space(el.get_text(" "))
        if classes & ITALIC_CLASSES or classes & BOLD_CLASSES:
            if not text:
                continue
            wrapper = soup.new_tag("em" if classes & ITALIC_CLASSES else "strong")
            for child in list(el.contents):
                wrapper.append(child.extract())
            el.append(wrapper)
        elif el.name == "p" and classes & set(HEADING_CLASSES):
            if not text:
                el.decompose()
                continue
            links_text = clean_space(" ".join(a.get_text(" ") for a in el.find_all("a")))
            if links_text == text or len(text) > 150:
                continue  # a link line or a whole paragraph styled as label: keep as is
            el.name = HEADING_CLASSES[(classes & set(HEADING_CLASSES)).pop()]
            del el["class"]


def heading_matches(text, title):
    a, b = fold(text), fold(title)
    if not a.strip():
        return False
    return a.strip() in b or b.strip() in a or difflib.SequenceMatcher(None, a, b).ratio() > 0.6


def parse_article(art, by_key, images_used):
    html = decode((PAGES / art["key"]).read_bytes())
    soup = extract_content(html)
    for sel in ["#picnam", "script", "style", "#fb-root"]:
        for x in soup.select(sel):
            x.decompose()
    # Navigation / issue headings.
    page_title = None
    for h in soup.find_all(["h1", "h2", "h3"]):
        t = clean_space(h.get_text())
        if "▲" in t or re.search(r"NAM-?IP\s*/?\s*Infos?\s+\d{4}\s*/\s*\d", t, re.I) or not t:
            h.decompose()
        elif page_title is None:
            page_title = t
            if not art["index_title"]:
                parent = by_key.get(art.get("parent")) or {}
                art["index_title"] = f"{parent['index_title']} — {t}" if parent.get("index_title") else t
                h.decompose()
            elif heading_matches(t, art["index_title"]):
                h.decompose()
            else:
                report["titre de page ≠ titre d'index (gardé dans le corps)"].append(
                    f"{art['slug']}: page «{t}» / index «{art['index_title']}»")
            break

    forced = TITLES.get(art["slug"])
    if forced:
        art["index_title"] = forced
    elif not art["index_title"]:
        parent = by_key.get(art.get("parent")) or {}
        art["index_title"] = f"{parent.get('index_title', art['slug'])} (suite)"
        report["sous-page sans titre (titre du parent + « suite »)"].append(art["slug"])

    # Signature(s): placeholder paragraphs, expanded after markdown conversion
    # (a "{.signature}" attribute line must survive whitespace normalisation).
    placeholders = {}
    sigs = []
    for p in soup.select(".sig"):
        s = clean_space(p.get_text(" "))
        if not s:
            p.decompose()
            continue
        sigs.append(s)
        token = f"SIGNATURE{len(placeholders)}X"
        placeholders[token] = s.replace("*", "\\*") + "\n{.signature}"
        new = soup.new_tag("p")
        new.string = token
        p.replace_with(new)
    art["signature"] = sigs
    # Stray tag fragments left as text in the source (e.g. " div>").
    for t in soup.find_all(string=re.compile(r"^\s*</?\s*[a-z]+\s*>?\s*$|^\s*/?[a-z]+>\s*$")):
        if not isinstance(t, Comment) and re.fullmatch(r"\s*</?\s*(div|p|span|section|td|tr|br)\s*>?\s*|\s*/?(div|p|span|section)>\s*", str(t)):
            t.extract()

    # Series hints.
    text = clean_space(soup.get_text(" "))
    art["has_suite"] = bool(re.search(r"suite au prochain num[ée]ro|(?:à|a) suivre", text, re.I))
    art["prev_links"] = set()
    for a in soup.find_all("a", href=True):
        ctx = clean_space(a.parent.get_text(" ")) if a.parent else ""
        if re.search(r"d[ée]but de cet article|premi[èe]re partie|partie pr[ée]c[ée]dente|article pr[ée]c[ée]dent|voir .*NAM-?IP.?Infos", ctx, re.I):
            key = cache_name(a["href"])
            if key in by_key:
                art["prev_links"].add(key)

    apply_class_styles(soup)
    art["links_to"] = set()
    art["images"] = {}
    localize_links(soup, by_key, art, images_used)
    galleries_to_shortcode(soup, placeholders)
    normalize_whitespace(soup)
    body = md(soup)
    for token, block in placeholders.items():
        body = body.replace(token, "\n\n" + block + "\n\n")
    # Tidy markdown.
    body = re.sub(r"[ \t]+\n", "\n", body)
    # Leading whitespace would turn source indentation into code blocks; keep it only for list items.
    body = re.sub(r"(?m)^[ \t]+(?![-*+] |\d+[.)] )(?=\S)", "", body)
    body = re.sub(r"\\\n(\s*\n)", r"\n\1", body)           # hard break just before a blank line
    body = re.sub(r"(?m)^\\$\n?", "", body)                # lines holding only a hard break
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
    art["body"] = body
    # Keep only images that made it into the markdown.
    art["images"] = {k: v for k, v in art["images"].items() if k in body}
    art["image_names"] = sorted(art["images"])
    textlen = len(clean_space(re.sub(r"[#*_\[\]()!{}<>]", "", body)))
    if textlen < 50 and not art["images"]:
        art["empty"] = True
        report["page vide sur le site source (exclue)"].append(
            f"{art['slug']} « {art['index_title']} » : {body.strip()!r}")
    elif textlen < 200:
        report["article très court (à vérifier)"].append(
            f"{art['slug']} ({textlen} car.) {art['index_title']}")


# ---------------------------------------------------------------- authors & series

SIG_CUT = re.compile(r",|\s(?:Facult|professeur|Professeur|Administrat|Universit|Directeur|Pr[ée]sident|Namur\b|asbl)|\S+@\S+")
INITIALS = re.compile(r"^(?:[A-Z][a-zé]?\.-?\s?)+(?:[A-Z]\.)?\s*")


def sig_name(sig: str):
    """Leading person name of a signature line, or None."""
    name = SIG_CUT.split(sig, maxsplit=1)[0].strip(" .")
    words = name.split()
    if 2 <= len(words) <= 4 and all(w[0].isupper() or w[0] in "dv" for w in words):
        return name.replace("’", "'")
    return None


def surname(name: str):
    return fold(name.replace("’", "'").split()[-1]).strip() if name.split() else ""


def learn_full_names(arts):
    """Map folded surname -> most frequent full (non-initial) name seen in signatures/index."""
    seen = defaultdict(lambda: defaultdict(int))
    for a in arts:
        for n in a["index_authors"] + [x for x in map(sig_name, a["signature"]) if x]:
            first = n.split()[0]
            if not re.fullmatch(r"(?:[A-Z][a-zé]?\.-?)+", first):  # not only initials
                seen[surname(n)][n.replace("’", "'")] += 1
    return {k: max(v, key=v.get) for k, v in seen.items()}


def resolve_authors(art, aliases, full_names):
    per_article = (aliases.get("articles") or {}).get(art["slug"])
    if per_article:
        art["authors"] = per_article
        return
    raw = list(art["index_authors"])
    if not raw:
        raw = [x for x in (sig_name(s) for s in art["signature"][-1:]) if x]
        if raw:
            report["auteur pris dans la signature (absent de l'index)"].append(f"{art['slug']}: {raw[0]}")
    out = []
    for r in raw:
        r = clean_space(r).replace("’", "'")
        canon = (aliases.get("noms") or {}).get(r) or full_names.get(surname(r), r)
        if canon not in out:
            out.append(canon)
    if not out:
        report["sans auteur"].append(f"{art['slug']} {art['index_title']}")
    art["authors"] = out


PART_RE = re.compile(
    r"\s*[-–—:,(]*\s*(?:\(?\s*(?:\d+|I+|1re|1ère|\d+e|\d+ème|premi[èe]re|deuxi[èe]me|troisi[èe]me|derni[èe]re)"
    r"\s*(?:partie|p\.?)\s*\)?|\(suite(?: et fin)?\)|suite(?: et fin)?)\s*\.?\s*$", re.I)


def base_title(t):
    return PART_RE.sub("", t).strip(" -–—:")


def build_series(arts, by_key, overrides):
    parent = {a["key"]: a["key"] for a in arts}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        parent[find(a)] = find(b)

    # 1. Explicit "début de cet article" links, and "voir la suite" sub-pages.
    for a in arts:
        if a.get("parent") in parent:
            union(a["key"], a["parent"])
        for p in a["prev_links"]:
            union(a["key"], p)
    # 2. Same base title with a "partie"/"suite" marker.
    by_base = defaultdict(list)
    for a in arts:
        if PART_RE.search(a["index_title"]):
            by_base[fold(base_title(a["index_title"]))].append(a)
    for a in arts:
        b = fold(a["index_title"])
        if b in by_base:
            by_base[b].append(a)
    for group in by_base.values():
        for g in group[1:]:
            union(group[0]["key"], g["key"])
    # 3. Manual overrides: {slug: "Nom de série"} or {slug: null} to exclude.
    groups = defaultdict(list)
    for a in arts:
        groups[find(a["key"])].append(a)
    for members in groups.values():
        members.sort(key=lambda x: (x["year"], x["issue"], x["ordre"]))
        name = None
        if len(members) >= 2:
            name = base_title(members[0]["index_title"])
        for m in members:
            m["series"] = [name] if name else []
    for slug, name in (overrides or {}).items():
        for a in arts:
            if a["slug"] == slug:
                a["series"] = [name] if name else []
    for a in arts:
        if a["has_suite"] and not a["series"]:
            report["« suite au prochain numéro » sans suite détectée"].append(
                f"{a['slug']} {a['index_title']}")


# ---------------------------------------------------------------- output

def write_bundle(a):
    d = POSTS / str(a["year"]) / a["slug"]
    d.mkdir(parents=True, exist_ok=True)
    numero = f"{a['year']}/{a['issue']}"
    fm = [
        "+++",
        f"title = {toml_str(a['index_title'])}",
        f"date = {a['year']}-{ISSUE_DATES.get(a['issue'], '12-31')}",
        f"numero = {toml_str(numero)}",
        f"ordre = {a['ordre']}",
        f"themes = [{toml_str(THEMES.get(a['code'], a['code'].capitalize()))}]",
        f"auteurs = [{', '.join(toml_str(x) for x in a['authors'])}]",
        f"series = [{', '.join(toml_str(x) for x in a['series'])}]",
        f"source = {toml_str(BASE + a['href'])}",
        "+++",
        "",
    ]
    (d / "index.md").write_text("\n".join(fm) + "\n" + a["body"], "utf-8", newline="\n")
    for safe, cached in a["images"].items():
        save_web_image(IMAGES / cached, d / safe)


MAX_SIDE = 1200


def save_web_image(src, dest):
    """Copy an image, downscaled to MAX_SIDE px and recompressed (originals stay in the cache)."""
    try:
        with Image.open(src) as im:
            im = ImageOps.exif_transpose(im)
            big = max(im.size) > MAX_SIDE
            if big:
                im.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
            ext = dest.suffix.lower()
            if ext in (".jpg", ".jpeg"):
                im.convert("RGB").save(dest, "JPEG", quality=80, optimize=True, progressive=True)
            elif ext == ".png" and (big or src.suffix.lower() == ".bmp"):
                im.save(dest, "PNG", optimize=True)
            else:
                shutil.copy2(src, dest)
        if dest.stat().st_size > src.stat().st_size and src.suffix.lower() == dest.suffix.lower():
            shutil.copy2(src, dest)  # recompression did not help: keep the original
    except OSError as e:
        report["image illisible (copiée telle quelle)"].append(f"{src.name}: {e}")
        shutil.copy2(src, dest)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    aliases = load_yaml("authors.yaml")
    series_overrides = load_yaml("series.yaml")
    TITLES.update(load_yaml("titles.yaml"))
    arts = parse_index()
    add_subpages(arts)
    by_key = {a["key"]: a for a in arts}
    images_used = set()
    missing_pages = []
    for a in arts:
        if not (PAGES / a["key"]).exists():
            missing_pages.append(a["href"])
            continue
        parse_article(a, by_key, images_used)
    arts = [a for a in arts if "body" in a and not a.get("empty")]
    full_names = learn_full_names(arts)
    for a in arts:
        resolve_authors(a, aliases, full_names)
    for h in missing_pages:
        report["page absente du cache (non téléchargée ou 404)"].append(h)
    build_series(arts, by_key, series_overrides)

    if not args.dry_run:
        # Replace generated content (keep posts/_index.md).
        for child in POSTS.iterdir():
            if child.is_dir():
                shutil.rmtree(child)
            elif child.name != "_index.md":
                child.unlink()
        for a in arts:
            write_bundle(a)

    meta = [{k: (sorted(v) if isinstance(v, set) else v) for k, v in a.items() if k != "body"} for a in arts]
    (HERE / "cache" / "articles.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf-8")
    (HERE / "cache" / "convert-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), "utf-8")
    print(f"{len(arts)} articles convertis, {len(images_used)} images, "
          f"{sum(1 for a in arts if a['series'])} articles en série")
    for k, v in report.items():
        print(f"  {k}: {len(v)}")


if __name__ == "__main__":
    sys.exit(main())
