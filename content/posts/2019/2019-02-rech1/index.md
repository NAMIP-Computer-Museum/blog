+++
title = "À propos des Mathématiques (2e partie)"
date = 2019-06-30
numero = "2019/2"
ordre = 5
themes = ["Recherche"]
auteurs = ["Gilbert Natan"]
series = ["À propos des Mathématiques"]
source = "http://pionnier.nam-ip.be/NAM-ip-INFO201902-Rech1.html"
+++

{{< galerie >}}
nam-ip-info201902rech1a.jpg | Tableau 1: Tables de vérité - ©NAM-IP
nam-ip-info201902rech1b.jpg | Tableau 2: Euclide: Algorithme du PGCD - ©NAM-IP
{{< /galerie >}}

[Le début de cet article a paru dans NAM-Ip/Infos 2019/1 ▶]({{< relref "/posts/2019/2019-01-rech4" >}})

## B. Informatique et mathématiques

Aux bases théoriques de l’informatique, on trouve nombre de mathématiciens incontestablement à l’origine de cette science. Ci-dessous quelques exemples saisissants et passionnants.

### L’algèbre de Boole, où l’on réfléchit en termes de 0 (zéro) et de 1 (un)

Pas de circuits électroniques, pas d’informatique, concevable sans se référer à l’inventeur de la logique booléenne et des règles de l’algèbre, définies par le Britannique George Boole (1815-1864). La mathématique a ici aussi précédé ses applications pratiques. Boole ne pouvait prévoir que des machines complexes ne fonctionneraient qu’en termes binaires. Il permit à des sciences comme la logique des circuits, la cryptographie, l’électronique et bien entendu l’informatique de se structurer et de se développer sans limites.

Les tables de vérité sont une de ses applications les plus connues.

Elles permettent de synthétiser la relation bi ou univoque de divers éléments d’un ensemble. Par exemple, les circuits logiques «ET» et «OU» se traduisent en table de vérité, voir Tableau 1.

### Les Algorithmes, un concept nouveau?

C’est le mathématicien perse Abu A. M. Ibn Musa al-Khwarizmi (780-850), qui a laissé son nom à une méthode d’algèbre logique, méthode diffusée à son époque dans tout l’empire arabo musulman «Abbasside». (J’ai déjà évoqué ce savant à propos de l’algèbre). Des raisonnements algorithmiques s’y retrouvaient déjà classés! Mais il y eut des algorithmes bien avant lui, à Babylone notamment.

C’est le mathématicien grec Euclide (428-346 av. J.-C.), évoqué plus haut, qui avait déjà formalisé un algorithme resté célèbre qui permet de calculer le plus grand commun diviseur (PGCD) des nombres a et b.

Je le reproduis, car il concrétise immédiatement la notion d’algorithme:

début:\
a/b = r\
a = b\
b = r\
si r non nul, retour en début si non b est le PGCD.

Dans l’exemple joint,voir Tableau 2, le PGCD est 12. Il n’est pas évident de le trouver a priori.

On le voit clairement ici: un algorithme est une suite d’instructions (un programme) qui contient au moins une séquence conditionnelle.

Leibnitz, toujours lui, poussa plus loin les bases théoriques des algorithmes avec une algèbre logique où l’on découvre ce qu’il appela «ratiocinateur».

Et voilà, l’algèbre avec ses algorithmes, a dû attendre près de 2.000 ans avant que les calculateurs électroniques ne puissent en exploiter son potentiel!

### John von Neumann (1903-1957), un être d’exception

Oserais-je dire qu’il s’agit du Mozart de la mathématique et de la physique du XXe siècle? Son parcours et son œuvre sont tout simplement uniques et fascinants! Mais nettement moins célèbre que le musicien!

Cela vaut d’être évoqué en bref dans le cadre de cet article consacré aux mathématiques en relation avec la naissance de l'informatique.

János naquit à Budapest (Autriche-Hongrie avant 1914) et se révéla dès l’âge de deux ans comme un enfant prodige doué d’une mémoire et d’une intelligence exceptionnelle. Il fut nommé Docteur en mathématiques à l’Université de Budapest à l’âge de 22 ans!

Entre 1926 et 1930, à l’université de Göttingen, il côtoiera de grands cerveaux de mathématiciens et de physiciens tels que Robert Oppenheimer, David Hilbert, Werner Heisenberg, Kurt Gödel. De 1933 à sa mort, il fut professeur de mathématiques à la faculté «for Advanced Study» de l’université de Princeton, USA. Il y rencontra entre autres Albert Einstein et Alan Turing. Naturalisé Américain en 1937, lui, comme d’autres grands cerveaux, participera à la guerre par ses études, portant notamment sur l’amélioration des performances des premiers calculateurs électroniques.

Ses contributions aux sciences furent multiple : logique mathématique, mécanique quantique, économie, armement atomique… (On ne cite généralement que Oppenheimer, et pourtant von Neumann apporta aussi une contribution déterminante).

Enfin, en informatique, il a donné son nom à une architecture d’ordinateur encore largement utilisée de nos jours, au point d’en être devenue un critère de définition.

Visionnaire? Aussi, dans son ouvrage de quasi-science-fiction *Theory of self-reproduction automate*.

### Claude Elwood Shannon (1916-2001).

C’était un ingénieur de Bell Laboratories qui s’intéressait particulièrement au domaine de la transmission.

Il publia, en 1948, avec l’aide d’un autre mathématicien, sa «Théorie mathématique de la Communication», où l’idée de base est que tout message se résume à une suite de 0 et de 1.

C’est de lui que vient le mot *bit* = *Binary Digit*, l’information élémentaire, mais parfaitement fiable entre une source de données et le poste de réception. De lui, que vient l’idée, que tout message peut être traduit et transmis sans altérations par une suite de 0 et de 1.

Également de lui, l’idée d’ajout de codage correcteur à un message pour éviter ce qu’il a appelé les «bruits» de la transmission. Encore de lui que vient l’idée de supprimer d’un message les informations inutiles: il est donc le père des applications de compression de données, dont les plus connues sont MP3 en musique et JPEG en imagerie.

Le *Théorème de Shannon*: On peut digitaliser tout signal, sans perte d’information, pourvu que la fréquence d’échantillonnage soit supérieure au double de la plus haute fréquence à transmettre.

À propos de Shannon, j’ai été saisi par une coïncidence étrange de la science : C’est en décembre 1947, soit à quelques mois de la parution de l’ouvrage évoqué ci-dessus, que le transistor est inventé dans les laboratoires de Bell Laboratories. Le support idéal du bit!

### Alan Turing (1912-1954)

Est un mathématicien devenu mythique. Il est surtout connu pour son rôle décisif dans le décryptage des messages codés par «Enigma» (voir les articles concernant Turing dans ce site). Il rencontra d’ailleurs Shannon aux USA, car tous deux travaillèrent au service de cryptage. Son travail théorique *On Computable Numbers, with an Application to the Entscheidungsproblem* (problème de décision), défend, en gros, la thèse que tout ce qui est vrai est programmable.

Pour cela et pour d’autres travaux ultérieurs, il est considéré comme un des pères de la science informatique. Son aventure personnelle permit de sortir les mathématiques dans l’univers du roman!

## La puissance multipliée des algorithmes va-t-elle vers l’écrasement de l’humain?

Des remarques essentielles: \
1) C’est l’accumulation de données à caractère privé qui devrait surtout nous faire peur. \
2) Les algorithmes servent à l’usage qui en est fait dans les domaines marketing, politique et militaire. Aussi, de plus en plus, comme outil pour la cybercriminalité. Cela fait peur, à raison sans doute. \
3) La robotique et l’intelligence artificielle recourent à des algorithmes de plus en plus sophistiqués, au point de permettre aux engins un auto apprentissage. Des algorithmes qui exploitent d’immenses bases de données. \
4) On l’a vu, les algorithmes, ce n’est que de la mathématique appliquée. Cette mathématique est le fruit du cerveau humain. On peut concevoir des robots qui se reproduiront eux-mêmes. On est loin de pouvoir imaginer des machines qui créeraient leur propre système mathématique! \
5) Les algorithmes très sophistiqués peuvent s’appuyer sur la puissance inimaginable des calculateurs actuels (dont la vitesse se chiffre en centaines de pétaflops, soit en 2019 jusqu’à 200 millions de milliards d’instructions par secondes)! Et aussi sur la dimension d’immenses bases de données (qui se chiffrent en 2019 jusqu’à une centaine de pétaoctets, 100 millions de giga-octets).

  6) Loin d’être des outils inhumains au service d’intelligences artificielles opposées à l’humain, les algorithmes servent à comprendre l’univers, à notre survie et à notre subsistance.

C’est là tout un livre qu’il faudrait écrire!

### Quelques exemples qui intéressent notre quotidien

Dans le domaine de la santé, dès les années 1960 des tentatives furent menées pour aider les médecins à diagnostiquer des maladies. Entre autres à la polyclinique de l’Hopital Universitaire de Bavière, le professeur M. O. Houziaux avait commencé avec quelques collaborateurs, une application qui avait comme premier objectif la formation médicale.

Un cas très récent: début 2019, des chercheurs de l’Université de San Francisco (UCSF) ont annoncé avoir mis au point un système permettant de détecter la redoutable maladie d’Alzheimer chez un patient jusqu’à 6 ans avant l’évidence médicale habituelle. Pour cela, Jae Ho Sohn, mentor de l’équipe de Big Data en radiologie à l’UCSF, a mis au point avec le reste de l’équipe une intelligence artificielle capable de diagnostiquer la maladie d'Alzheimer avant un médecin humain. Le responsable explique que la maladie est difficile à repérer dans les premiers temps. “*Quand tous les symptômes cliniques se sont manifestés et qu’il est possible de réaliser un diagnostic définitif, trop de neurones sont morts, ce qui rend la maladie irréversible*”, explique-t-il dans un article publié par l’UCSF à son sujet.

Sans aller aux USA, la société IBA à Louvain-la-Neuve travaille sur l’assistance au suivi de l’évolution des tumeurs traitées par protonthérapie. Il s’agirait de proposer au médecin à chaque traitement les ciblages précis des rayons de protons. Ceci au moyen de puissants algorithmes et de bases de données en la matière.

Dans le domaine de l’énergie: Tout récemment paraissait une interview de Damien Ernst, professeur à l’Université de Liège. Il a reçu en 2018 la médaille Blondel, une des plus belles distinctions internationales qu’un ingénieur électricien puisse obtenir!

Le résultat d’années de travail sur la mise au point d’algorithmes qui permettent d’équilibrer les différents facteurs qui influencent les réseaux de distribution électrique. Énoncé abstrait, mais qui cache une solution par algorithmes d’un problème qui nous impacte tous, de plus en plus: la transition énergétique.

Notre quotidien est influencé par des avancées de l’usage des algorithmes en biologie clinique, en imagerie médicale, en criminologie, en cybersécurité, en assistance à la conduite (automobiles, camions, trains, avions…), gestion des flux de télécommunications, etc.

### Les merveilles futuristes de la mécanique quantique

J’avoue ne rien connaitre en physique quantique, et donc encore moins en mathématiques quantiques. Le père en est célèbre: Werner Heisenberg (1901-1976). Heureusement pour moi, un très grand contributeur à cette physique, Richard Feynman; aurait dit à son propos: «*Si vous croyez comprendre la mécanique quantique, c’est que vous ne la comprenez pas*».

J’en retiens quand même ce qui suit.

Pour les objets microscopiques, la physique ordinaire n’est plus d’application! Une particule microscopique peut être dans un mélange de plusieurs états. Aussi incroyable que cela paraisse, cela veut dire qu’un électron peut par exemple posséder à la fois deux vitesses, ou être à deux endroits différents au même instant. Voire plus de deux endroits simultanément! Donc, la position, la vitesse, le champ magnétique d’un «quanta» n’est pas une valeur absolue. C’est une probabilité d’avoir «n» états bien déterminés, mais n étant limité à quelques valeurs bien précises. On est amené à traiter des «quanta» comme des ondes. Les mathématiques quantiques serviront à traiter ces phénomènes.

### Et l’informatique dans cela?

Au début de ce XXIe siècle, des scientifiques ont réussi à isoler certains éléments de matière (les quanta) et à pouvoir provoquer chez eux, à volonté, plusieurs états différents. On a ainsi créé des ordinateurs quantiques, dont l’élément de mémoire n’est plus le *bit*, mais le *qbit*. C’est l’état qui représente la plus petite unité de stockage d’information quantique. Il peut prendre plusieurs valeurs.

Ici se situe la révolution en cours: une information élémentaire peut représenter plusieurs valeurs, en fonction de probabilités.

Les nouveaux algorithmes quantiques pourront donc traiter des *qbits* comme des valeurs probables. Le champ est ouvert à de nouveaux instruments de recherche dans des bases de données à caractère probabiliste.

Une question telle que: «Trouver les concentrations des produits présents dans les parfums les plus achetés par les femmes qui fréquentent 50 % des centres commerciaux proches de leur domicile» sera résolue de manière bien plus performante qu’actuellement.

Une bonne introduction à la physique quantique : [les-7-merveilles-de-la-mecanique-quantique](https://sciencetonnante.wordpress.com/2013/09/30/les-7-merveilles-de-la-mecanique-quantique/)

## Pour conclure

Ces quelques plongées dans l'Histoire des mathématiques, de l'arithmétique aux algorithmes et à la mécanique quantique, ne nous montrent-elles pas que les mathématiques sont loin d’être froides, anonymes, inhumaines? Ne procèdent-elles pas, depuis 4000 ans av. J.-C., à nos jours, à la formidable créativité de l’esprit humain et à sa capacité de s’extraire de la simple réalité pour plonger dans des univers ou des visions saisissantes?

Et en guise de postface, cette citation attribuée à J. von Neumann:

Si les gens ne croient pas que les mathématiques sont simples, c’est uniquement parce qu’ils ne réalisent pas à quel point la vie est compliquée!.

G. Natan
{.signature}
