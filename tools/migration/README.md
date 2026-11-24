# Migration NAM-IP/Infos (pionnier.nam-ip.be → Hugo)

Scripts qui reconstruisent `content/posts/` à partir de l'ancien site
http://pionnier.nam-ip.be/NAM-IP-Infos.html.

```sh
python -m venv .venv && .venv/Scripts/pip install -r requirements.txt   # une fois
.venv/Scripts/python fetch.py      # aspiration lente (4-5 s entre requêtes), avec reprise ; cache/ ignoré par git
.venv/Scripts/python convert.py    # hors ligne : régénère content/posts/** (page bundles + images)
.venv/Scripts/python audit.py      # écrit audit.md (comparaison source / ancienne migration / nouvelle)
```

`convert.py` est rejouable : corriger les fichiers ci-dessous puis relancer.

| Fichier | Rôle |
|---|---|
| `authors.yaml` | normalisation des noms d'auteurs, auteurs imposés par article |
| `series.yaml` | corrections des séries détectées (`slug: "Nom"` ou `slug: null`) |
| `titles.yaml` | titres imposés (sous-pages sans titre exploitable) |

Ce que fait la conversion :
- métadonnées (titre, auteur, numéro, rubrique) prises dans l'index ; auteur de secours dans la signature `.sig` ;
- mise en forme reconstituée depuis les classes CSS de la source (`txt1ji` → italique, `txt1jbold` → gras,
  `txt1lb13`/`txt1lb12` → intertitres) ;
- galeries `prettyPhoto` → shortcode `{{</* galerie */>}}` avec légendes, images ≤ 1200 px, BMP → PNG ;
- liens internes réécrits en `relref`, sous-pages « Voir la suite » rattachées à leur article (série) ;
- séries détectées via « Le début de cet article… », « 2e partie », etc.
