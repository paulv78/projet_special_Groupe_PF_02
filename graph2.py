# Importer le module pandas sous l'alias pd
import pandas as pd
# Importer le module matplotlib.pyplot sous l'alias plt
import matplotlib.pyplot as plt
# Importer le module graph_name sous l'alias g
import graph_name as g
import answer_protection as q

# Définir la liste des critères utilisés dans le programme
CRITERIA_LIST = ['Cie aérienne', 'Avion', 'Statut', 'Heure Départ', "Heure Arrivée", 'Ville départ', "Ville Arrivée"]


# Définition de la fonction prompt_user pour interroger l'utilisateur avec une requête donnée
def prompt_user(query):
    # Afficher la requête
    print(query)
    # Retourner True si la réponse de l'utilisateur est 'OUI', sinon False
    return input().upper() == 'OUI'


# Définition de la fonction pour extraire et formater l'heure d'une colonne donnée d'un DataFrame
def extract_hour_format(df, c1):
    # Extraire l'heure au format 'HHhMM' de la colonne c1
    df[c1] = df[c1].str.extract(r'(\d{2}h\d{2})')
    # Convertir la chaîne extraite en un objet datetime
    df[c1] = pd.to_datetime(df[c1], format='%Hh%M')
    # Créer une nouvelle colonne 'Heure' avec seulement l'heure de la colonne c1
    df['Heure'] = df[c1].dt.hour


# Définition de la fonction pour tracer le nombre d'avions par heure en fonction de deux critères
def plot_frequency_count_by_hour_by_c2(dataframe, c1, c2):
    # Récupération des critères réels à partir des indices
    c1 = CRITERIA_LIST[int(c1) - 1]
    c2 = CRITERIA_LIST[int(c2) - 1]

    # Créer une copie du DataFrame original pour ne pas le modifier
    df = dataframe.copy()
    # Extraire et formater l'heure de la colonne c1
    extract_hour_format(df, c1)

    # Compter le nombre d'occurrences par heure et par critère c2
    counts = df.groupby(['Heure', c2]).size().reset_index(name='Count')
    # Créer un tableau croisé à partir des comptages
    pivot_table = counts.pivot(index='Heure', columns=c2, values='Count').fillna(0)

    # Demander à l'utilisateur s'il souhaite enregistrer les données dans un fichier Excel
    if prompt_user("Voulez-vous enregistrer les données du graphique dans un fichier Excel ?"):
        # Demander le nom du fichier ou en générer un automatiquement
        print("Voulez-vous choisir le nom du fichier ? nom = [text you enter].xlsx (répondez 'OUI' ou 'NON')")
        ans = input(str())
        ans = q.answer_protction_bool(ans)
        if ans == 'OUI':
            print("Entrez le nom que vous choisissez")
            text = str(input())
            name = text + '.xlsx'
            name = q.is_valid_filename(name, "xlsx")
        if ans == 'NON':
            name = g.graph_name(c1, c2, '.xlsx')
        # Ajouter une colonne pour les valeurs ordonnées
        pivot_table['Valeurs Ordonnées'] = pivot_table.sum(axis=1)
        # Enregistrer le DataFrame dans le fichier Excel
        valid = q.can_write_file(name)
        if valid:
            pivot_table.to_excel(name)
            print(f"Données du graphique enregistrées dans le fichier : {name}")
        # Supprimer la colonne des valeurs ordonnées du DataFrame
        pivot_table = pivot_table.drop('Valeurs Ordonnées', axis=1)

    # Afficher un message que le graphique est généré
    print('Graphique généré')
    # Créer le graphique à barres à partir du tableau croisé
    ax = pivot_table.plot(kind='bar', ax=plt.gca())
    # Définir les labels des axes et le titre du graphique
    plt.xlabel(c1)
    plt.ylabel("Nombre d'avions")
    plt.title(f'Nombre d\'avions par {c1} par {c2}')

    # Lire les critères à partir du fichier et les ajouter à la légende du graphique
    with open("critères.txt", "r") as file:
        text = "Critères de séléction:" + "\n" + file.read()
    ax.legend(title=text + '\n' + c2)

    # Demander à l'utilisateur s'il souhaite enregistrer le graphique dans un fichier png
    if prompt_user("Voulez-vous enregistrer les données du graphique dans un fichier png ?"):
        # Demander le nom du fichier ou en générer un automatiquement
        print("Voulez-vous choisir le nom du fichier ? nom = [text you enter].png (répondez 'OUI' ou 'NON')")
        ans = input(str())
        ans = q.answer_protction_bool(ans)
        if ans == 'OUI':
            print("Entrez le nom que vous choisissez")
            text = str(input())
            name = text + '.png'
            name = q.is_valid_filename(name, "png")
        if ans == 'NON':
            name = g.graph_name(c1, c2, '.png')
        valid = q.can_write_file(name)
        if valid:
            # Enregistrer le graphique dans le fichier png
            plt.savefig(name)
            print(f"Données du graphique enregistrées dans le fichier : {name}")

    # Afficher le graphique
    plt.show()
