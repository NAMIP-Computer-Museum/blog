+++
title = "Inventaire ou Base de connaissances? — 2.3 Une proposition pour NAM-IP"
date = 2019-12-31
numero = "2019/4"
ordre = 2.3
themes = ["Préservation"]
auteurs = ["Yolande Juste"]
series = ["Inventaire ou Base de connaissances?"]
source = "http://pionnier.nam-ip.be/NAM-ip-Info201904-Pres1-2-3.html"
+++

{{< galerie >}}
nam-ip-info201904pres1-3a.jpg | Fig. 1: Ecran d'accueil
nam-ip-info201904pres1-3b.jpg | Fig. 2: Sélection dans la Table des matières
nam-ip-info201904pres1-3c.jpg | Fig. 3: Fiche détaillée d'un objet
nam-ip-info201904pres1-3d.jpg | Fig. 4: Archives photographiques
nam-ip-info201904pres1-3e.jpg | Fig. 5: Sélection par la liste des mots
{{< /galerie >}}

**[▶1. Les Collections du Fonds Informatique Pionnière en Belgique, déposées au Computer Museum NAM-IP]({{< relref "/posts/2019/2019-04-pres1-1" >}})**

**▶[2. Quelles sont les normes? Que font les autres musées?\
2.1 Comparaison des fiches de l'ICOM, de FEBB, de MMIL]({{< relref "/posts/2019/2019-04-pres1-2-1" >}})**

**▶ [2.2 Accès en ligne? Analyse de quelques propositions\
2.2.1 FWB (Fédération Wallonie Bruxelles) : inventaires automatisés AICIM\
2.2.2 FWB (Fédération Wallonie Bruxelles): numeriques.be\
2.2.3 Musée Rops\
2.2.4 CNAM et CNUM\
2.2.5 IBM Hursley Museum]({{< relref "/posts/2019/2019-04-pres1-2-2" >}})**

## 2.3 Une proposition pour NAM-IP?

Le Fonds informatique pionnière en Belgiqe de la Fondation Roi Baudouin possède des ressources immatérielles. Parmi celles-ci le moteur de recherche "Knowhowsphere" (en abrégé KHS) créé par un des 4 Collectionneurs Fondateurs de ce Fonds.

En acceptant en dépot les Collections du Fonds, NAM-IP a donc aussi l'obligation de valoriser les ressources immatérielles de ce Fonds.

Une des meilleures façons serait de conserver cette ressource active en l'utilisant pour les besoins du NAM-IP.

Intervient ici une grande question: un patrimoine immatériel inscrit à l'inventaire doit-il être conservé actif ou non-actif?

En ne l'utilisant pas, le risque est évident de le condamner à jamais. Il en va de même pour toutes les ressources électroniques qui demandent à être copiées et vérifiées régulièrement sous peine d'être perdues.

### 2.3.1 Caractéristiques du moteur de recherche KHS

Il se différencie de tous les exemples analysés plus haut, notamment :

-il montre l'étendue du Corpus et le présente de manière logique à travers une arborescence, une Table des Matières

 - il montre tous les mots ou expressions présentes dans le Corpus de telle façon que toutes les recherches aboutissent toujours. Il est impossible de faire une recherche sur un mot non présent dans le Corpus et il est inutile de se référer à un thésaurus ou d'indiquer des mots-cléfs ou vedettes

 - il montre toujours les documents trouvés, dans leur contexte logique de la Table des Matières

 - il peut gérer aussi bien des fiches d'inventaires que des contenus textuels et des images ou photos

Comme tous les moteurs de recherche, il permet de limiter la recherche à une section de l'arborescence, il permet des recherches avancées utilisant les opérateurs booléens. Il permet à l'utilisateur de recevoir par courriel le résultat de sa recherche…

L'outil peut aussi traiter la numérisation de documents et leur présentation sous forme d'images de pages ou de recherche de contenu.

### 2.3.2 Quel format d'inventaire adopter?

Comme nous l'avons vu, il n'y a pas véritablement de normes mais seulement des recommandations. L'idée était toutefois de pouvoir gérer dans un même format aussi bien les artefacts, objets, que la documentation, la bibliothèque, les ressources électroniques…

Après analyse, le format retenu est celui de l'ISBD ([International Standard Bibliographic Description](https://www.ifla.org/files/assets/cataloguing/isbd/44-fr.pdf)) intégré. Cette version de Description bibliographique a intégré les différentes versions spécialisées par type de ressource. Elle permet de décrire dans le même format aussi bien des objets, des livres, des périodiques, de la musique, des fichiers électroniques…

Le tableau reprend les Zones de l'ISBD pour trois types d'objet: Livre ou périodique, Fichier électronique ou logiciel, objet et dans la dernière colonne l’ISBD appliqué à NAM-IP dans KHS.

On retrouve donc bien tous les champs recommandés par l'ICOM dans cette dernière colonne.

Nous avons transposé ce format en XML et l’avons étendu pour permettre l’ajout d’informations, telles que des illustrations, des notes… et tout le contenu textuel possible et cherchable sur l'objet décrit.

Le format XML est par définition indépendant de tout format "propriétaire" lié à un programme comme le sont souvent les formats des SGBD. Les mêmes données peuvent donc être utilisées de diverses façons sans problème de synchronisation.

Chaque objet aura donc obligatoirement sa description technique en ISBD et toutes les autres données utiles en mode texte cherchable sur tous les mots.

En intégrant à chaque objet décrit, toutes les informations connues à son sujet, la Base de Données de l’inventaire devient alors une Base de Connaissance et la mémoire des objets inscrits à l'inventaire.

| N° d'inventaire |  |  |  |  |
| --- | --- | --- | --- | --- |
| Zone 0Forme de contenu et médiation | Livre / Périodique/ Représentation graphique | Musique / Fichier électronique / Logiciel | Objet / Sculpture | ISBD pour NAM-IP |
| Zone 1Titre et mentions | Titre / Auteur | Titre / Compositeur / Auteur | Titre / Artiste | Nom de l'objet et description |
| Zone 2Édition | Livraison |  |  |  |
| Zone 3Mentions particulières |  |  |  |  |
| Zone 4Éditeur, Lieu, Date | Éditeur, Lieu, Date | Éditeur, Lieu, Date | Lieu, Date de production | Fabricant, Lieu, Date |
| Zone 5Description matérielle | Pages, ill., Dimensions | Durée, taille, format, | Dimensions | Dimensions, Poids, Matériaux |
| Zone 6Collection | Livraisons ou parties |  | Collection | Collections / Fonds |
| Zone 7Notes |  |  |  | État de conservation |
| Zone 8Identification et acquisitionConditions | N° ISBN, Prix | Prix |  | Acquisition, mode, provenance, date |
|  |  |  |  | Description longuePhotos |

### 2.3.3 État actuel de la proposition

L'inventaire complet et unifié du Fonds Informatique Pionnière en Belgique est un travail de longue haleine. Soit il faut créer l'inventaire à partir de rien, soit il faut adapter l'inventaire au format retenu et à la nouvelle situation des Collections dans le bâtiment de NAM-IP.

Dans la proposition KHS, l'écran est toujours divisé en 3 parties: \
à gauche l'Arborescence de la Table des Matières, \
au centre le Document courant, \
à droite le Cherchable et la recherche dans des index particuliers.

 1. Arborescence dans laquelle ont peut naviguer en ouvrant successivement les nœuds et en parcourant la Base de données comme un "livre" mais avec différentes fonctions de navigation: ouvrir tous les nœuds, aller au nœud suivant ou précédent, fixer les bornes de la recherche, marquer des documents manuellement, afficher uniquement les documents marqués par la recherche…

 2. Partie centrale: le Document courant avec différentes fonctions: naviguer d'un document trouvé à l'autre, naviguer dans le contexte des documents marqués par la recherche, envoi de documents par email, impression, aller d'un document à l'autre et revenir au document appelant, agrandir la photo affichée en vignette…

 3. Á droite: le Cherchable, les index et la recherche: l'index de tous les mots de la Base de Données de A à Z ou des index particuliers pour les nombres, les dates, les localisations, les numéros ISBN, les numéros de série… Dans l'index A-Z des suffixes indiquent si le mot est présent dans la description de l'objet ou dans la zone Éditeur ce qui permet de limiter facilement la recherche aux mots de la description par exemple.

Une fonction de recherche avancée permet la contruction logique de la requête à l'aide des opérateurs booléens (ET, OUF, SAUF).

Cette Base de Donées est organisée en 4 Fonds: \
Fonds des Objets, Fonds Numérique, Fonds Documentaire et Fonds d'Archives

Á ce jour:

 - le Fonds des Objets comprend la totalité de la Collection Systèmes de calcul de Jacques Lemaire, les machines de mécanographie de Bull.

 - le Fonds Numérique comprend principalement des photographies, ± 7.000

 - le Fonds Documentaire comprend une partie de la Bibliothèque et des Périodiques

 - le Fonds d'Archives comprend principalement les description sommaires des Archives de l'application I&B.

Il est donc trop incomplet pour être publié et mis à disposition aujourd'hui.

### Quelques exemples de recherche :

**• Fig. 1: écran d'accueil avec l'arborescence à gauche, le document introductif au centre et la liste des mots à droite**

**• Fig. 2: Un objet sélectionné par une navigation dans la table des matières**

**• Fig. 3: Fiche détaillée d'un objet, augmentée d'une description longue**

**• Fig. 4: Archives photographiques d'un événement**

**• Fig. 5: Un objet sélectionné par une recherche dans la liste alphabétique des mots**

Cet outil n'est cependant pas parfait:

 - la saisie devrait être améliorée par l'ajout de formulaires,

 - la puissance de la recherche suppose une chaîne de traitement des données et donc une validation,

 - l'ajout de méta-données permettant le moissonage pourrait être ajouté à la chaîne de traitement.

## Conclusion

Cet exemple montre la possibilité de combiner dans une seule Base de Données un inventaire détaillé d'objets, de documents, de livres, de fichiers, de photos, associé à un moteur de recherche très complet.

Mais mettre l'inventaire complet et unifié du Fonds Infomatique Pionnière en Belgique dans ce moteur de recherche constituerait une tâche immense qui en est seulement à ses débuts.

La valorisation des Collections par leur disponibilité dans Internet serait pourtant un réel avantage pour le Fonds.

Á titre d'exemple: le Living Computers Museum+Labs de Seattle, récemment visité, possède des réserves les mieux organisées qui soient. La responsable des Collections nous disait que que 3 personnes travaillent à l'inventaire depuis 7 ans… 21 années/homme!

Faut-il dès lors privilégier la création d'un inventaire de type Tableur, accessible en tout ou en partie dans Internet via des Formulaires de recherche ou la création d'une Base de Connaissance sur le Fonds, incluant un inventaire et donnant un véritable outil de recherche à l'utilisateur?

L'avenir nous le dira!

Yolande Juste
{.signature}

PS: Tous les liens et les captures d'écran sont vérifiés à la date de publication de cet article.
