"""Audit: source index vs. the previous migration (from git) vs. the new conversion.

Run after convert.py. Writes tools/migration/audit.md.
Usage: python audit.py [--old-ref 4e7837a] [--pre-delete-ref 09a3e7c]
"""
import argparse
import difflib
import json
import re
import subprocess
from collections import Counter

from common import HERE, REPO, cache_name


def git(*args):
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True,
                          text=True, encoding="utf-8", errors="replace").stdout


def old_posts(ref):
    """{source page key: (path, title, draft)} for posts in content/posts at ref."""
    out = {}
    for path in git("ls-tree", "-r", "--name-only", ref, "content/posts").split():
        if not path.endswith(".md") or "/20" not in path or path.endswith("_index.md"):
            continue
        text = git("show", f"{ref}:{path}")
        m = re.search(r"pionnier\.nam-ip\.be/(\S+?\.html)", text)
        title = re.search(r'^title\s*=\s*"(.*)"', text, re.M)
        draft = re.search(r"^draft\s*=\s*true", text, re.M) is not None
        out.setdefault(cache_name(m.group(1)) if m else f"?{path}", []).append(
            (path, title.group(1) if title else "", draft))
    return out


RUBRIQUE_CODES = {"editorial": "edito", "edito": "edito", "preservation": "pres",
                  "exposition": "expos", "recherche": "rech", "acquisition": "acq",
                  "comptes": "cr", "news": "news", "nouvelles": "news"}


def match_by_title(posts, arts):
    """Re-key posts without source URL using 'NAM-IP Infos AAAA/N – Rubrique Titre' titles."""
    from convert import fold
    out = {k: v for k, v in posts.items() if not k.startswith("?")}
    for key, entries in posts.items():
        if not key.startswith("?"):
            continue
        for path, title, draft in entries:
            m = re.match(r"NAM-IP\s*/?\s*Infos?\s+(\d{4})\s*/\s*(\d)\s*[–-]\s*(\S+)\s*(.*)", title)
            best, score = None, 0.0
            if m and not m.group(4).strip():
                # Only the rubrique: unambiguous if the issue has one article of that rubrique.
                code = RUBRIQUE_CODES.get(fold(m.group(3)).strip())
                cands = [a for a in arts if (a["year"], a["issue"], a["code"]) ==
                         (int(m.group(1)), int(m.group(2)), code)]
                if len(cands) == 1:
                    best, score = cands[0], 1.0
            elif m:
                y, n, t = int(m.group(1)), int(m.group(2)), fold(m.group(4))
                for a in arts:
                    if (a["year"], a["issue"]) == (y, n):
                        r = difflib.SequenceMatcher(None, t, fold(a["index_title"])).ratio()
                        if r > score:
                            best, score = a, r
            if best and score > 0.5:
                out.setdefault(best["key"], []).append((path, title, draft))
            else:
                out.setdefault(f"?{path}", []).append((path, title, draft))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--old-ref", default="4e7837a", help="state of the previous migration")
    ap.add_argument("--pre-delete-ref", default="09a3e7c", help="state before the 'fix2 tree' deletions")
    args = ap.parse_args()

    arts = json.loads((HERE / "cache" / "articles.json").read_text("utf-8"))
    report = json.loads((HERE / "cache" / "convert-report.json").read_text("utf-8"))
    sub = json.loads((HERE / "cache" / "subpages.json").read_text("utf-8")) \
        if (HERE / "cache" / "subpages.json").exists() else {}
    indexed = [a for a in arts if not a.get("parent")]
    by_key = {a["key"]: a for a in arts}

    old = match_by_title(old_posts(args.old_ref), arts)
    pre = match_by_title(old_posts(args.pre_delete_ref), arts)

    L = ["# Audit de la migration NAM-IP/Infos", ""]
    L += ["## Synthèse", "",
          f"| | Nombre |", "|---|---:|",
          f"| Articles listés dans l'index source | {len(indexed)} |",
          f"| Sous-pages « voir la suite » (hors index) | {len(sub)} |",
          f"| **Articles convertis (nouvelle migration)** | **{len(arts)}** |",
          f"| Posts de l'ancienne migration avant suppressions ({args.pre_delete_ref}) | {sum(len(v) for v in pre.values())} |",
          f"| Posts de l'ancienne migration publiés ({args.old_ref}) | {sum(len(v) for v in old.values())} |",
          f"| Images reprises | {len({i for a in arts for i in a['image_names']})} |",
          ""]

    years = Counter(a["year"] for a in arts)
    themes = Counter(a["code"] for a in arts)
    L += ["Par année : " + ", ".join(f"{y}: {n}" for y, n in sorted(years.items())), "",
          "Par rubrique : " + ", ".join(f"{k}: {n}" for k, n in themes.most_common()), ""]

    missing_old = [a for a in indexed if a["key"] not in old]
    L += [f"## Articles absents de l'ancienne migration publiée ({len(missing_old)})", "",
          "Désormais repris. Ceux qui existaient avant le commit « fix2 tree » mais avaient été supprimés sont marqués ✂.", ""]
    for a in missing_old:
        mark = " ✂" if a["key"] in pre else ""
        L.append(f"- {a['year']}/{a['issue']} · {a['code']} · [{a['index_title']}]({a['href']}){mark}")
    L.append("")

    L += ["## Confusions dans l'ancienne migration", ""]
    conf = []
    for key, entries in pre.items():
        if key.startswith("?"):
            for path, title, draft in entries:
                conf.append(f"- `{path}` « {title} » : pas de page source identifiable{' (draft)' if draft else ''}")
            continue
        a = by_key.get(key)
        if len(entries) > 1:
            conf.append(f"- `{key}` migré {len(entries)} fois : " + ", ".join(f"`{p}`" for p, _, _ in entries))
        for path, title, draft in entries:
            m = re.search(r"/(\d{4})/", path)
            if a and m and int(m.group(1)) != a["year"]:
                conf.append(f"- `{path}` rangé en {m.group(1)} alors que l'article est de {a['year']}/{a['issue']} ({a['index_title']})")
    L += (conf or ["Aucune."]) + [""]

    L += ["## Points à vérifier (rapport de conversion)", ""]
    for k, v in report.items():
        if k == "page absente du cache (non téléchargée ou 404)" and not v:
            continue
        L.append(f"### {k} ({len(v)})")
        L.append("")
        L += [f"- {x}" for x in v[:80]]
        if len(v) > 80:
            L.append(f"- … et {len(v) - 80} autres")
        L.append("")

    series = {}
    for a in arts:
        for s in a["series"]:
            series.setdefault(s, []).append(a)
    L += [f"## Séries détectées ({len(series)})", "",
          "À corriger au besoin dans `series.yaml`.", ""]
    for s, parts in sorted(series.items()):
        parts = sorted(parts, key=lambda p: (p["year"], p["issue"], p["ordre"]))
        L.append(f"- **{s}** : " + " → ".join(f"{p['year']}/{p['issue']} {p['slug']}" for p in parts))
    L.append("")

    authors = Counter(x for a in arts for x in a["authors"])
    L += [f"## Auteurs ({len(authors)})", "", "À normaliser au besoin dans `authors.yaml`.", ""]
    L += [f"- {n} ({c})" for n, c in authors.most_common()] + [""]

    (HERE / "audit.md").write_text("\n".join(L), "utf-8")
    print(f"audit.md écrit: {len(arts)} articles, {len(missing_old)} absents de l'ancienne migration, "
          f"{len(conf)} confusions, {len(series)} séries")


if __name__ == "__main__":
    main()
