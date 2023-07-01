# Importe les bibliothèques nécessaires
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import date_and_naming as d
import answer_protection as q

# Convertit une colonne spécifique d'un DataFrame en une liste
def column_to_list(df, column_name):
    return df[column_name].tolist() # Renvoie la liste des valeurs de la colonne

# Supprime les vols annulés du DataFrame
def remove_cancelled_flights(df):
    df = df[df['Statut'] != 'Annulé'] # Filtre le DataFrame pour exclure les vols annulés
    return df.reset_index(drop=True) # Réinitialise l'index et retourne le DataFrame modifié

# Compte le nombre de vols par heure
def count_planes_by_hour(df):
    df['Heure'] = df['Heure Départ'].str.extract(r'(\d{2})h') # Extrait l'heure du temps de départ
    flight_counts_d = df.groupby(['Ville départ', 'Heure']).size().reset_index(name='Count') # Compte le nombre de vols pour chaque ville de départ et chaque heure
    flight_counts_d=create_hours(flight_counts_d,'Ville départ') # Ajoute les heures manquantes pour chaque ville de départ

    df['Heure'] = df['Heure Arrivée'].str.extract(r'(\d{2})h') # Extrait l'heure du temps d'arrivée
    flight_counts_a = df.groupby(['Ville Arrivée', 'Heure']).size().reset_index(name='Count') # Compte le nombre de vols pour chaque ville d'arrivée et chaque heure
    flight_counts_a = create_hours(flight_counts_a,'Ville Arrivée') # Ajoute les heures manquantes pour chaque ville d'arrivée

    df1 = flight_counts_d
    df2 = flight_counts_a

    df3 = pd.DataFrame({
        'Ville': df1['Ville'], # Copie la colonne 'Ville'
        'Heure': df1['Heure'], # Copie la colonne 'Heure'
        'Count': df1['Count'] + df2['Count'] # Ajoute les comptes de vols de départ et d'arrivée
    })

    df3 = remove_nan_rows(df3) # Supprime les lignes avec des valeurs NaN
    return df3

# Supprime les lignes contenant des valeurs NaN
def remove_nan_rows(dataframe):
    dataframe.dropna(axis=0, inplace=True) # Supprime les lignes avec des valeurs NaN
    return dataframe

# Ajoute les heures manquantes pour chaque ville
def create_hours(df,parameter):
    df['Heure'] = df['Heure'].astype(int) # Convertit la colonne 'Heure' en entier
    df = df.set_index([parameter, 'Heure']).unstack(fill_value=0).stack().reset_index() # Ajoute les heures manquantes avec une fréquence de zéro pour chaque ville
    df = df.rename(columns={parameter: 'Ville'}) # Renomme la colonne en 'Ville'
    return(df)

# Affiche un graphique de la fréquentation par heure pour chaque ville
def plot_frequentation(df3, display_graph):
    if not display_graph: # Si l'utilisateur ne souhaite pas afficher le graphique
        return

    for ville in df3['Ville'].unique(): # Pour chaque ville unique dans le DataFrame
        data = df3[df3['Ville'] == ville] # Filtre le DataFrame pour une seule ville
        plt.plot(data['Heure'], data['Count'], label=ville) # Trace un graphique pour cette ville

    plt.xlabel('Heure') # Ajoute un libellé à l'axe des x
    plt.ylabel('Fréquentation') # Ajoute un libellé à l'axe des y
    plt.title('Fréquentation des villes en fonction de l\'heure') # Ajoute un titre au graphique
    plt.legend() # Ajoute une légende au graphique

    print("Voulez-vous enregistrer les données du graphique dans un fichier png ? (répondez 'OUI' ou 'NON')")
    ans = str(input())
    ans = q.answer_protction_bool(ans)
    if ans == 'OUI': # Si l'utilisateur souhaite enregistrer le graphique
        print("Voulez-vous choisir le nom du fichier ? nom = [text you enter].png (répondez 'OUI' ou 'NON')")
        ans = input(str())
        ans = q.answer_protction_bool(ans)
        if ans == 'OUI': # Si l'utilisateur souhaite choisir un nom de fichier
            print("Entrez le nom que vous choisissez")
            text = str(input()) # L'utilisateur entre le nom du fichier
            name = text + '.png' # Ajoute l'extension .png au nom du fichier
        if ans == 'NON':
            name = 'frequentation Canada '+d.get_current_date()+'.png' # Utilise une chaîne de caractères prédéfinie et la date actuelle pour nommer le fichier
        valid = q.can_write_file(name)
        if valid:
            plt.savefig(name) # Enregistre le graphique sous le nom choisi
            print(f"Données du graphique enregistrées dans le fichier : {name}")

    plt.show() # Affiche le graphique

# Identifie l'heure de pointe pour chaque ville
def peak_frequency(df3, print_info):
    peak_hours = df3.groupby('Ville')['Count'].idxmax() # Identifie l'heure avec le plus grand nombre de vols pour chaque ville
    peak_values = df3.loc[peak_hours, 'Count'] # Identifie le nombre maximum de vols à l'heure de pointe pour chaque ville

    if print_info: # Si l'utilisateur souhaite imprimer les informations
        for ville, heure, valeur in zip(df3.loc[peak_hours, 'Ville'], df3.loc[peak_hours, 'Heure'], peak_values): # Pour chaque ville, heure de pointe, et valeur de fréquentation maximale
            print(f"Ville : {ville}, Heure du pic : {heure}h, Fréquentation : {valeur} Appareils") # Imprime les informations

    return pd.DataFrame({
        'Ville': df3.loc[peak_hours, 'Ville'], # Renvoie le nom de la ville
        'Heure du pic': df3.loc[peak_hours, 'Heure'], # Renvoie l'heure de pointe
        'Fréquentation': peak_values # Renvoie la fréquentation à l'heure de pointe
    })

# Calcule la fréquentation pour chaque aéroport
def frequentation(dataframe):
    df = remove_cancelled_flights(dataframe) # Supprime les vols annulés
    lst = column_to_list(df, 'Ville départ') + column_to_list(df, 'Ville Arrivée') # Crée une liste de toutes les villes de départ et d'arrivée
    counts = Counter(lst) # Compte le nombre de vols pour chaque ville
    counts_df = pd.DataFrame.from_dict(counts, orient='index', columns=['Count']).reset_index() # Convertit le compteur en un DataFrame
    counts_df.columns = ['Aeroport', 'Count'] # Renomme les colonnes du DataFrame
    return counts_df # Renvoie le DataFrame