import pandas as pd
from openpyxl import load_workbook
import answer_protection as q

def ecrire_excel(data_frame, fichier_sortie):
    # Le DataFrame est écrit dans un fichier Excel avec le nom spécifié.
    # L'option index=False est utilisée pour empêcher l'écriture des indices de DataFrame dans le fichier.
    data_frame.to_excel(str(fichier_sortie), index=False)
    # Un message est affiché pour informer l'utilisateur que le fichier Excel a été généré.
    print('.excel généré')

# utilisé pour écrire les fichiers temp, ne laisse pas le code s'exécuter tant que le fichier temp n'a pas été écrit.
# si le fichier ne peut pas être écrit, le programme retentera d'écrire le fichier au signal de l'utilisateur
def ecrire_excel_p(data_frame, fichier_sortie):
    # Le DataFrame est écrit dans un fichier Excel avec le nom spécifié.
    # L'option index=False est utilisée pour empêcher l'écriture des indices de DataFrame dans le fichier.
    valid = q.can_write_file(fichier_sortie)
    if valid:
        data_frame.to_excel(str(fichier_sortie), index=False)
        # Un message est affiché pour informer l'utilisateur que le fichier Excel a été généré.
        print('.excel temp généré')
    if not valid:
        print("Une erreur empêche l'écriture d'un fichier temporaire. Résolvez l'erreur puis entrez 'A' pour rééssayer.")
        print("Alternativement, entrez 'B' pour terminer l'exécution du programme")
        ans = str(input())
        ans,verif = q.answer_protection_A_B(ans)
        if verif:
            ecrire_excel_p(data_frame, fichier_sortie)
        if not verif:
            exit()

def display_dataframe(data_frame):
    # Configuration des options de visualisation de DataFrame pour afficher toutes les colonnes, toutes les lignes et pour une largeur de 1000.
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)
    # Affiche le DataFrame avec les options de visualisation configurées ci-dessus.
    print(data_frame)

def lire_excel(filepath):
    # Charger le fichier Excel avec openpyxl
    wb = load_workbook(filename=filepath, read_only=True)

    # Sélectionner la première feuille du classeur
    ws = wb.active

    # Lire les données dans une liste de listes, chaque sous-liste représente une ligne
    data_rows = []
    for row in ws:
        data_cols = []
        for cell in row:
            data_cols.append(cell.value)
        data_rows.append(data_cols)

    # Créer un DataFrame à partir des données
    df = pd.DataFrame(data_rows)

    # Utiliser la première ligne comme en-têtes des colonnes
    df.columns = df.iloc[0]
    df = df.iloc[1:]

    return df