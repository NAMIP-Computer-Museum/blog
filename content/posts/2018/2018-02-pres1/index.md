+++
title = "L'ordinateur BULL Gamma 60 - 2e partie"
date = 2018-06-30
numero = "2018/2"
ordre = 2
themes = ["Préservation"]
auteurs = ["Gilbert Natan"]
series = ["L'ordinateur BULL Gamma 60"]
source = "http://pionnier.nam-ip.be/NAM-ip-Info201802-Pres1.html"
+++

{{< galerie >}}
nam-ip-info201801pres1a.jpg | Gamma 60 Cablage - ©NAM-IP
nam-ip-info201801pres1b.jpg | Gamma 60 Dérouleur - ©NAM-IP
nam-ip-info201801pres1c.jpg | Gamma 60 Plaques logiques- ©NAM-IP
nam-ip-info201801pres1d.jpg | Gamma 60 Pupitre- ©NAM-IP
nam-ip-info201801pres1e.jpg | Gamma 60 Programme- ©NAM-IP
{{< /galerie >}}

[Le début de cet article a paru dans NAM-Ip/Infos 2018/1 ▶]({{< relref "/posts/2018/2018-01-pres1" >}})

## La réalisation technique

### Mémoires internes

La mémoire centrale à tores de ferrite fut d’abord étudiée, puis commandée au début chez Remington-Rand, lequel en fabriquait pour son Univac. Sa construction fut ensuite sous-traitée en France. Le Gamma 60 posséda ainsi en 1959 une mémoire centrale de grande capacité – pour l’époque – (jusqu'à 32.768 mots de 24 "bits"), ceci sous forme de tores magnétiques d'accès «rapide» (10 microsecondes), adressable sans discontinuité de 0 à 32.767. (Ce n’est que bien plus tard que les systèmes opératoires renonceront à cette linéarité intégrale de l'adressage, d'abord en réduisant la linéarité à une "partition" pour chaque programme, puis à n "segments" d'instructions et de données par programme, et ceci pour des raisons de protection des programmes, ou des sections de programme, vis-à-vis les uns des autres).

Le mot de 24 bits se prêtait bien au calcul en virgule flottante: 2 mots représentaient 10 chiffres et 2 exposants. Les nombres et exposants étaient codés en décimal, chaque chiffre sur 4 bits. Il faut remarquer que les calculs portaient donc sur des nombres codés en décimal et non en binaire sous forme de 2n. En effet, à l’époque, la lourdeur des conversions des nombres en binaire pur fit que l’on préféra leur représentation et leur traitement en décimal. Un mot pouvait aussi représenter 4 caractères alphanumériques (lettres ou chiffres) de 6 bits chacun. (Ce mot de 24 bits portait le nom de «catène»). La mémoire centrale était constituée de maximum 8 blocs, lesquels étaient composés de 27 plans de 4.096 tores de ferrite. 27 plans car chaque mot de 24 bits était accompagné de 3 bits de contrôle et correction! (1 bit de parité pour les 9 bits du type d’opération et 2 bits pour les 15 bits de la partie adresse, du jamais vu!).

### Circuits logiques

La technique des circuits montés sur des plaques logiques permutables fut adoptée.

La technologie des transistors fut choisie. Elle était toute récente. En effet, le premier ordinateur entièrement transistorisé fut le PHILCO qui ne sortit qu’en 1958, tandis que le IBM 7070, l’ELEA 9003, le UNIVAC III et le Z23 ne furent commercialisés qu’en 1960.

Bruno Leclerc, le directeur du projet Gamma 60, fit remarquer que le choix du transistor entraîna de grosses difficultés techniques. Heureusement, le fournisseur choisi, Radiotechnique, était une filiale de Philips. Mais ce n’est qu’en 1959 que Philips pu livrer des transistors du type « pnp » convenant tout à fait aux besoins. La contribution des deux entités fournisseur dans la définition de normes de contrôle, de tolérance et de mode d’emploi fut déterminante.

### Mémoires externes

En plus d'une grande capacité d'adressage en mémoire centrale, le Gamma 60 héritait d’une extension en mémoire externe adressable: un à quatre tambours magnétiques déjà fabriqués chez Bull pour le Gamma «Ordonnateur».

Ce tambour avait une vitesse de rotation de 2975 t/m et comportait 128 pistes de 200 mots. Soit donc une capacité de 25.000 mots ou 102.400 caractères. Son temps d’accès moyen : 10 ms.

On y ajouta venant de fournisseurs extérieurs à la Compagnie:

Des dérouleurs de ruban magnétique, dont la partie électromécanique fut commandée à ElectroData Co; une société californienne constructeur de calculateurs électroniques. Elle sera reprise peu après par Burroughs Co lequel mit à son catalogue le Datatron 203, en le renommant B 203. (À noter, concernant les dérouleurs, l’offre de la société belge «ACEC» qui avait été sérieusement prise en compte. Un retard des ACEC dans la mise au point causa l’abandon de cette option.) La partie électronique des dérouleurs, avec les têtes de lecture/écriture, fut réalisée par la Compagnie. Sans doute une première, la technique de modulation de phase fut utilisée. Les rubans magnétiques étaient prévus en encodage 9 voies, sur une largeur de ½ pouce, 8 pistes écrites en suivant un mode d’enregistrement «entrelacé» des mots de 24 bits. \
Densité d’écriture: 300 bpi, débit: 22 Koctets/sec. À noter: la lecture pouvait se faire aussi bien en avant qu’en arrière, option très utile dans les tris car évitant des rebobinages. La gestion des dérouleurs se faisait via un à dix contrôleurs (unisélecteurs). Ceux-ci pouvaient gérer jusqu’à 48 dérouleurs.

À noter qu’en 1960, chaque constructeur avait son propre mode d’encodage sur rubans magnétiques. Il fallut attendre l’apparition du IBM 360 pour que cette grande société informatique impose au marché des ordinateurs ses propres standards d’écriture sur ruban magnétique.

### Périphériques «classiques»

Côté périphérie «papier», le Gamma 60 profitait des périphériques déjà fabriqué par la Compagnie des Machines Bull. Plusieurs de ceux-ci étaient connectables au système : \
- lecteurs-perforateurs de carte (jusqu’à 4), avec poste de relecture pour vérification;\
- imprimantes (jusqu’à 8) avec vérification par écho des caractères frappés;\
- en option de 1 à 4 lecteurs ou perforateurs de bande papier. (Origine Ferranti).

### Gestion de la périphérie

Le Gamma 60 pouvait gérer tous ces périphériques en un ou plusieurs traitements simultanés. Tous ces périphériques fonctionnaient, via des contrôleurs spécialisés, sous le contrôle de l'Unité Centrale. Ceci justifiait le nom de "Cerveau Électronique" que l'on donnait alors volontiers à une telle installation.

Un informaticien commandait cet ensemble au moyen d'un pupitre de commande et de contrôle comportant une machine à écrire (origine Remington) et un lecteur de bande perforée, plus un jeu de commutateurs. D’où le nom de «pupitreur» donné à ce spécialiste. \
La machine à écrire électrique, fort sollicitée, était un point faible du système.

### Architecture

Le traitement d'information proprement dit était réalisé non pas par un processeur unique comme il était d'usage, mais par quatre processeurs centraux spécialisés travaillant en simultanéité les uns vis-à-vis des autres et en simultanéité avec les éléments périphériques:\
- un Calculateur Arithmétique opérant sur des nombres en virgule flottante codés en décimal, avec contrôle des résultats par la preuve par 7;\
- Un calculateur Logique opérant sur des données en binaire;\
- un Comparateur Général (très utile dans les tris par ex.), qui servait aussi aux transferts de données entre emplacements de mémoire;\
- un Traducteur.

S’ajoutaient à ces éléments centraux des contrôleurs de périphériques pour les tambours, les dérouleurs (unisélecteurs) et les périphériques «lents».

Le Gamma 60 introduisait, avant même que les termes n'apparaissent dans le langage, les concepts de multiprogrammation (en anglais multi-programming: exécution en parallèle de plusieurs programmes indépendants), de multitraitement (ou multi-tâche: exécution simultanée de plusieurs séquences de programme à l'intérieur du même programme), et de multi-processing (exécution simultanée de plusieurs instructions par multiplication des processeurs).

Le Gamma 60 constituait donc, avec ses simultanéités de traitement d'un grand nombre de programmes indépendants et ses nombreux organes périphériques travaillant en parallèle, une véritable "usine à traiter l'information", sans commune mesure avec les matériels précédents de la Compagnie et sans équivalent chez les concurrents. Les gros ordinateurs d'IBM étaient, supérieurs en termes de puissance de calcul pure. Les processeurs centraux du Gamma 60, eux, étaient relativement lents.

## La Programmation

### La programmation de base

Elle se faisait par instruction de longueur fixe de 1 mot. \
Elles se décomposaient en code opération sur 9 bits, et en adresse sur 15 bits. \
La partie adresse était codée en binaire. Elle était de valeur absolue ou relative. \
Il y avait un large répertoire d’instructions, chaque élément central ayant son propre jeu d’instructions.

### La structuration des programmes

L’Instruction de Coupure. \
Chaque programme élémentaire, ou tâche, était divisé en séquences par des "Instructions de COUPURE". Une Coupure citait le nom d'un élément (ARIT pour Calculateur Arithmétique, LOGI pour Calculateur Logique, COMP pour Comparateur Général, TRAD pour Traducteur, TAMB pour Tambour Magnétique, DERU pour Dérouleur, etc…). \
L'ensemble des instructions suivant une Coupure, et jusqu'à la Coupure suivante constituait le programme local de l'élément. Ce programme comportait à la fois des "Directives d’Exécution" de l'élément, et des "Directives Centrales" qui étaient exécutées via le Distributeur de Programme. Quand l'élément avait reçu une "Directive d'Exécution", il se mettait au travail de façon autonome et libérait le Distributeur de Programme qui pouvait alors travailler pour le compte d'un autre élément.

### La simultanéité programmée

Un autre élément de la structuration des programmes est la simultanéité programmée par instruction SIMU qui pouvait être assimilée à une Coupure. Une instruction SIMU citait l'adresse d'une instruction ("branche extraordinaire") qui était forcément une Coupure. Les instructions suivant cette Coupure (Directives Préparatoires, Directives Centrales) s'exécutaient jusqu'à rencontrer une Directive d'Exécution qui mettait au travail l'élément cité, et le programme reprenait à l'instruction suivant la SIMU ("branche ordinaire").\
Les files d’attente étaient gérées par des chaînes de reprise, qui constituaient une chaîne des adresses des instructions de Coupure. (Notion de «stack» que l’on retrouve en Multix par exemple).

### Les langages de programmation

Au départ, deux niveaux de langages étaient disponibles: \
Le langage A, ou langage-machine, avec adressage en valeur absolue. \
Le langage B, un auto codeur.

Les développeurs renoncèrent à implémenter le Fortran (jugé probablement peu adapté à un système de gestion), ou le Cobol (à peine né et qui sera très peu utilisé en Europe entre 1960 et 1965).

Le choix se porta sur l’Algol 60, dans sa version stabilisée publiée en 1960. Une première mondiale en matière de développement de ce langage si bien adapté à la résolution d’algorithmes. Son interpréteur fut définitivement au point sur le Gamma 60 en 1965.

## Suite au prochain numéro de NAM-IP/Infos

G. Natan
{.signature}
