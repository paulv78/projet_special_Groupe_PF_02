# Importation des modules nécessaires pour la génération des graphiques
import graph2
import graph3

# Définition des critères disponibles pour la construction du graphique
CRITERIA_LIST = ['Companie', 'Avion', 'Satut', 'Heure de départ', "Heure d'arrivée", 'Ville de départ', "Ville d'arrivée"]

# Fonction pour demander à l'utilisateur de choisir les critères de son graphique
def prompt_for_criteria():
    # Expliquer la structure du graphique à l'utilisateur
    print ("Le graphique aura la structure suivante : Nombre d'avions par c1 par c2")
    # Demander à l'utilisateur de choisir ses critères
    print("Choississez c1 et c2 en les entrant, séparés par un un espace dans la liste suivante :")
    print("Compagnie (1), Avion (2), Statut (3), Heure de départ (4), Heure d'arrivée (5), Ville de départ (6), Ville d'arrivée (7)")
    # Enregistrer les critères choisis par l'utilisateur
    c1, c2 = input().split()
    # Rappeler à l'utilisateur les critères qu'il a choisis
    print (f"Le graphique aura la structure suivante : Nombre d'avions par {CRITERIA_LIST[int(c1)-1]} par {CRITERIA_LIST[int(c2)-1]}")
    # Renvoyer les critères choisis
    return c1, c2

# Fonction pour définir les paramètres du graphique en fonction des critères choisis par l'utilisateur
def parameter_definition(dataframe):
    # Demander à l'utilisateur de choisir ses critères
    c1, c2 = prompt_for_criteria()
    # Définir les critères qui nécessitent un traitement particulier
    combinations = {'4', '5'}
    # Vérifier si l'un des critères choisis nécessite un traitement particulier
    if c1 in combinations or c2 in combinations:
        # Si c'est le cas, générer le graphique avec le module approprié
        if c1 in combinations:
            graph2_cleaned.plot_frequency_count_by_hour_by_c2(dataframe, c1, c2)
        else:
            graph2_cleaned.plot_frequency_count_by_hour_by_c2(dataframe, c2, c1)
    # Si aucun des critères choisis ne nécessite un traitement particulier
    else:
        # Générer le graphique avec le module standard
        graph3_cleaned.plot_frequency_count_by_c1_by_c2(dataframe, c1, c2)