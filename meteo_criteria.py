# Importer les bibliothèques nécessaires
import pandas as pd
import math

# Définir une fonction pour assigner des critères en fonction d'une valeur et d'un ensemble de bins et de labels
def assign_criteria(value, bins, labels):
    for i in range(len(bins)):
        # Vérifier si la valeur se situe dans l'intervalle courant et si elle n'est pas infinie
        if bins[i][0] <= value <= bins[i][1] and not math.isinf(value):
            # Si c'est le cas, retourner le label correspondant à cet intervalle
            return labels[i]
    # Si aucune condition n'est satisfaite, retourner None
    return None

# Définir une fonction pour calculer des critères en fonction de la fréquentation totale et de la météo
def criteria(total_frequentation, meteo):
    # Définir les bins pour la fréquentation, la température et la couleur
    freq_bins = [(0, 80), (80, 150), (150, float('inf'))]
    temp_bins = [(-273, 15), (15, 25), (25, float('inf'))]
    color_bins = [(1, 3), (3, 6), (6, 9)]

    # Définir les labels pour les nombres et les couleurs
    number_labels = [1, 2, 3]
    color_labels = ['green', 'orange', 'red']

    # Assigner un nombre à chaque valeur de 'Count' dans total_frequentation en utilisant les bins de fréquentation
    total_frequentation['Number'] = total_frequentation['Count'].apply(assign_criteria, bins=freq_bins,labels=number_labels)
    # Assigner un nombre à chaque valeur de 'Température (°C)' dans meteo en utilisant les bins de température
    meteo['Number'] = meteo['Température (°C)'].apply(assign_criteria, bins=temp_bins, labels=number_labels)

    # Créer un nouveau dataframe avec la ville et la couleur, calculée en multipliant le nombre de total_frequentation par le nombre de meteo
    dfc = pd.DataFrame({
        'Ville': meteo['Ville'],
        'Couleur': total_frequentation['Number'] * meteo['Number']
    })
    # Assigner un label de couleur à chaque valeur de 'Couleur' dans dfc en utilisant les bins de couleur
    dfc['Color Label'] = dfc['Couleur'].apply(assign_criteria, bins=color_bins, labels=color_labels)
    # Retourner le dataframe final
    return dfc
