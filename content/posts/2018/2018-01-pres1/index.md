+++
title = "L'ordinateur BULL Gamma 60"
date = 2018-03-31
numero = "2018/1"
ordre = 2
themes = ["Préservation"]
auteurs = ["Gilbert Natan"]
series = ["L'ordinateur BULL Gamma 60"]
source = "http://pionnier.nam-ip.be/NAM-ip-Info201801-Pres1.html"
+++

{{< galerie >}}
nam-ip-info201801pres1a.jpg | Gamma 60 Cablage - ©NAM-IP
nam-ip-info201801pres1b.jpg | Gamma 60 Dérouleur - ©NAM-IP
nam-ip-info201801pres1c.jpg | Gamma 60 Plaques logiques- ©NAM-IP
nam-ip-info201801pres1d.jpg | Gamma 60 Pupitre- ©NAM-IP
nam-ip-info201801pres1e.jpg | Gamma 60 Programme- ©NAM-IP
{{< /galerie >}}

## Introduction

Le Computer Museum présente depuis juillet 2017 une maquette représentant un «Bull Gamma 60», lequel fut installé à la Régie Belge des Télégraphes et Téléphones de 1962 à 1974. \
Qu’est ce système, peu connu en dehors du cercle des Anciens de la société Bull ? Dans quel contexte de l’histoire informatique fut il conçu ? Pourquoi cette maquette ? Quel intérêt y a-t-il à la présenter ? C’est à ces questions que je tente de répondre en 6 chapitres:

Un peu d’histoire\
La Rupture chez Bull\
Naissance du projet\
La réalisation technique\
La programmation\
Le système opératoire\
Les contraintes d’installation\
ConclusionsNotes et Références

## Un peu d’histoire

Pour ce qui concernait la Compagnie des Machines Bull, il faut savoir que jusque dans les années 1950, elle partageait le marché européen des machines électromécaniques à cartes perforées avec son grand concurrent IBM. Powers (Sperry Rand) était peu présent sur ce marché européen, ICT (ICL) restait surtout centré sur la Grande-Bretagne et l’ex-Empire britannique.

La technologie à tubes électroniques appliquée aux calculateurs, était déjà née durant la guerre 1940-45, tant aux USA qu’en Allemagne. Par la suite, les constructeurs de machine à cartes perforées ne tardèrent pas à créer des calculateurs électroniques connectables à leurs machines électromécaniques afin d’en augmenter la puissance de calcul. \
À la Compagnie des Machines Bull, des électroniciens furent embauchés afin de réaliser de tels calculateurs. Ce fut le cas du Gamma 3, fabriqué à partir de 1953. Mais le Gamma 3 était "asservi" à la tabulatrice et ne la commandait pas. En 1959, Bull lançait le «Gamma 3 Extension Tambour», surnommé. «Ordonnateur», lequel inversait les rôles et dans lequel c'étaient désormais les machines connectées qui étaient asservies à l'organe de calcul électronique. Il comportait une mémoire externe : le tambour magnétique où des programmes étaient enregistrés.

Mais ce système, malgré un certain succès commercial, arrivait déjà trop tard. En effet, l’on vit se développer à partir de 1955 toutes sortes de systèmes dits «de deuxième génération», qui mettaient à profit la disponibilité des diodes au germanium, de transistors et de mémoires à tores de ferrite, ces 2 derniers éléments encore assez chers. (J’ai retrouvé le prix moyen d’achat d’un transistor en 1962: 0.80 $, soit 32 fr. belges de la même année.) \
Ce fut le temps de la commercialisation de «gros systèmes»: UNIVAC I (1951), IBM 650 (1955), IBM 305 (1956), Z22 de Zuse (D,1958), IBM 305 (RAMAC, 1957), IBM 705 (1959), PDP-1 de DEC (1959) et d’autres.

Pendant ce temps, le département Études de la Compagnie des Machines BULL mettait en chantier en 1956 un système plus évolué que le Gamma 3 Extension Tambour: le Gamma 4.

En réaction à la concurrence évoquée plus haut, la Compagnie décida d’annoncer dès fin 1960 ce nouvel ordinateur. Mais ils le prénommèrent Gamma 60.

La Compagnie des Machines BULL développait en parallèle à cela un ordinateur à carte perforée, «Série 300», qui fut disponible vers 1958.

Sans entrer dans le détail, disons de la Série 300 qu’il s’agissait d’un système hybride. Son développement permit cependant aux ingénieurs électromécaniciens de la Compagnie de développer le sommet de leur art, surtout pour deux périphériques. Un lecteur/perforateur de cartes à 300 cartes par minutes et une imprimante à tambour 300 lignes par minutes, à double entraînement de papier, c’est-à-dire pouvant être considérée par le système comme deux imprimantes indépendantes se partageant les 120 colonnes de large. Ces périphériques allaient dans la suite être améliorés et être connectés à bien des systèmes Bull à venir, dont le Gamma 60 dont je vais parler.

Par ailleurs, des constructeurs bâtissaient de très grands ensembles, souvent assez élaborés dans leur architecture. Ils furent reproduits en peu d’exemplaires: le STRETCH ou IBM 7030 (1961), le LARC d’Univac (1960) ; le H 800 d’Honeywell (1960) qui, lui, se vendit à plus de 80 exemplaires. N’oublions pas non plus l’ambitieux Olivetti Elea 9003 (1960), entièrement transistorisé et à vocation multiprogrammation; hélas aussi reproduit à très peu d’exemplaires.

## La Rupture chez Bull. Naissance du projet

Dès 1957, des ingénieurs «logiciens» de la Compagnie décidèrent, dans le cadre de ce qui devrait être le Gamma 60, de s'affranchir des contraintes du passé et de faire table rase de tout ce qui existait dans leur société. Ils voulaient concevoir une machine entièrement nouvelle et extrêmement ambitieuse, mettant à profit les dernières avancées technologiques. Dans ce but, des personnalités très compétentes furent mobilisées. Inutile de les citer tous, on les retrouve dans l’ouvrage «Aventure du Gamma 60» en référence. Je citerai quand même l’équipe de trois brillants électroniciens qui s’imposa à la réalisation du projet: Bruno Leclerc, Pierre Chenu et Henri Fessel. Extrêmement brillants, passionnés et enthousiastes, ils entraînèrent avec eux non seulement leurs équipes, mais aussi leur hiérarchie. Ils avaient un manque, partagé par beaucoup de cadres en France dans ces années: aucun ne comprenait bien l’anglais, encore moins celui parlé par les Américains. Ils étaient donc fermés aux énormes sources de connaissances existant aux USA. \
Seul personnage important dans cette aventure à avoir une très bonne pratique de l’anglais, Philippe Dreyfus ramenait quantités d’informations de ses voyages aux USA… mais ne diffusait ses connaissances que dans les contextes académiques et commerciaux!

Des moyens financiers considérables furent mis à disposition des Études et de la Fabrication afin de concevoir et fabriquer ce qu’ils voyaient surtout comme un très puissant ordinateur destiné aux applications scientifiques propres aux très grandes entreprises: Énergies, Banques, Transports. Les applications de gestion venaient en seconde priorité. Grave erreur pour une société dont la clientèle était largement demanderesse d’améliorer ses applications de gestion.

## Suite au prochain numéro de NAM-IP/Infos

G. Natan
{.signature}
