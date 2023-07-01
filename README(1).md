
## PRINCIPE 
Ce programme permet d'afficher la liste des vols entre 4 aéroports (Montréal, Ottawa, Toronto et Vancouver) pris à un jour donné. 
Il utilise une base de données listant tous les vols entre ces 4 aéroports, qui contient pour chaque vol: 
- La compagnie 
- Le numéro de vol 
 - Le type de l'appareil 
- Le statut du vol (arrivé, planifié, annulé) 
-  L'heure de départ 
- L'heure d'arrivée 
- La ville de départ 
- La ville d'arrivée 
## FONCTIONNEMENT 
Le programme se lance avec la commande
> python <span>main.py</span>

Sous forme de questions-réponses successifs dans une invite de commande, l'utilisateur peut choisir de façon précise quelles informations afficher. 
Voici les options proposées: 
- Visualisation de la base de données complètes 
- Possiblité de filtrer la base de données pour n'afficher que certains vols, en fonction des critères mentionnés ci-dessus (compagnie, numéro de vol,...). 
Il est possible de sélectionner un ou plusieurs de ces critères, puis de choisir les valeurs que l'on souhaite garder. Cela permet par exemple de ne garder que les vols d'une certaine compagnie aérienne, ou faits par un certain type d'avion... Une visualisation des vols correspondants est proposée lorsque le choix des valeurs est effectué. 
- Possibilité de sauvegarder la base de données filtrées selon les préférences utilisateur, en choisissant le nom 
- Possibilité de générer un graphique 2D en fonction de critères choisis (par exemple: nombres d'avions d'un certain type par compagnie,...) Les données filtrées ainsi que le graphique peuvent être enregistrés si l'utilisateur le désire 
- Possibilité d'afficher et sauvegarder des informations en lien avec les aéroports
 -- Météo
  -- Fréquentations de chaque aéroport par heure 
 - Possibilité d'afficher la carte d'une ligne entre 2 aéroports parmi les 4 considérés, qui montre les positions des villes de départ et d'arrivée ainsi que le trajet entre les deux. On a également des informations sur la qualité de l'air des deux villes considérées. 
 ## STRUCTURE 
- ``main`` ordonne l'execution di code de manière chronologique et appelle les fonctions principales, et empêche un crash en cas de keyboard interrupt, tout en supprimant systématiquement les fichiers temporaires générés. 
- ``ask_user`` guide l'utilisateur à travers l'utilisation de l'interface et lui permet de naviguer le code, appelant de manière transparente et automatique les sous fonctiona appropriées pour répondre à ses choix.
- ``sort_dataframe`` permet de manipuler les informations des données conformémént aux demandes de l'utilisateurs, et applle de multiples fonctions auxiliaires en conséquence.
- ``parameter_definition`` slectionne la fonction appropriée lorsque l'utilisateur souhaite générer un graphique à partir des données.
- ``graph2`` et ``graph3`` tracent le graphique, graph 2 se différencie de graph 3 en rassemblant les données par interval d'heure.
- ``Aeroport`` permet à l'utilisateur d'fficher des informations variées concernat les aéroports.
- ``plot_frequentation`` calcule la fréquentation journalière maximale des aéroports.
- ``weather_info`` récupère la météo en tempe réel.
- ``count_planes_by_hour`` compte les avions pour chaque aéroports pour chaque heure.
- ``peak_frequency`` identifie pour chaque aéroport la fréquence maximale d'avions et l'heure à laquelle elle se produit, et affiche le graphique de  fréquentation des différents aéroports.
- ``nouvellecarte`` affiche le graphique d'une ligne de vol, et pour chacun des deux aéroports concernés la météo, et la qualité estimée de l'air.

Fonctions auxiliaires

- ``answer_protection`` : permet à l'utilisateur de re-saisir une réponse si la réponse n'est pas conforme aux besoins du script, évitant ainsi un crash, comportement inattendu ou dysfonctionnement du script.
- ``date_and_naming`` : permet de générer des noms de fichiers automatiquement.
- ``manipulation_fichier`` : permet de réaliser diverses opérations de lecture et d'écriture de fichiers dans le système.
- ``remove`` : supprime les divers fichiers temporaires générés après chaque execution du code.