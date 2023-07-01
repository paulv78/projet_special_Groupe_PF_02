# Importer les bibliothèques nécessaires
import matplotlib.pyplot as plt
import graph_name as g
import answer_protection as q

# Initialiser la liste des critères
CRITERIA_LIST = ['Cie aérienne', 'Avion', 'Statut', 'Heure Départ', "Heure Arrivée", 'Ville départ', "Ville Arrivée"]

def prompt_user(query):
    print(query)
    # On demande une réponse à l'utilisateur, si sa réponse est "oui" (insensible à la casse), la fonction retourne True, sinon elle retourne False
    return input().upper() == 'OUI'

def plot_frequency_count_by_c1_by_c2(dataframe, c1, c2):
    # On récupère les critères à partir de la liste des critères en utilisant c1 et c2 comme indices (après avoir décrémenté de 1 pour correspondre à l'indexation basée sur zéro en Python)
    c1 = CRITERIA_LIST[int(c1) - 1]
    c2 = CRITERIA_LIST[int(c2) - 1]

    # Créer une copie du dataframe original pour éviter toute modification accidentelle des données originales
    df = dataframe.copy()

    # Regrouper le dataframe par c1 et c2, calculer la taille de chaque groupe et réinitialiser l'index du résultat
    counts = df.groupby([c1, c2]).size().reset_index(name='Count')
    # Pivoter le dataframe pour avoir c1 comme index, c2 comme colonnes et 'Count' comme valeurs, remplir les valeurs manquantes par 0
    pivot_table = counts.pivot(index=c1, columns=c2, values='Count').fillna(0)

    # Demander à l'utilisateur s'il souhaite enregistrer le tableau dans un fichier excel
    if prompt_user("Voulez-vous enregistrer les données du graphique dans un fichier excel ?"):
        # Demander le nom du fichier ou le générer automatiquement
        print("Voulez-vous choisir le nom du fichier ? nom = [text you enter].xlsx (répondez 'OUI' ou 'NON')")
        ans = input(str())
        ans = q.answer_protction_bool(ans)
        # Si l'utilisateur veut choisir le nom du fichier, demander le nom et ajouter l'extension '.xlsx'
        if ans == 'OUI':
            print("Entrez le nom que vous choisissez")
            text = str(input())
            name = text + '.xlsx'
            name = q.is_valid_filename(name, "xlsx")
        # Si l'utilisateur ne veut pas choisir le nom du fichier, générer le nom du fichier automatiquement
        if ans == 'NON':
            name = g.graph_name(c1, c2, '.xlsx')
        # Ajouter une colonne pour les valeurs ordonnées et sauvegarder le tableau dans un fichier excel
        pivot_table['Valeurs Ordonnées'] = pivot_table.sum(axis=1)
        valid = q.can_write_file(name)
        if valid:
            pivot_table.to_excel(name)
            print(f"Données du graphique enregistrées dans le fichier : {name}")
        # Supprimer la colonne des valeurs ordonnées
        pivot_table = pivot_table.drop('Valeurs Ordonnées', axis=1)

    # Informer l'utilisateur que le graphique est généré
    print('Graphique généré')

    # Créer le graphique à barres
    ax = pivot_table.plot(kind='bar')
    # Définir les labels des axes et le titre du graphique
    ax.set_xlabel(c1)
    ax.set_ylabel("Nombre d'avions")
    ax.set_title(f"Nombre d'avions par {c1} par {c2}")
    # Configurer les paramètres des labels de l'axe x
    ax.tick_params(axis='x', labelrotation=90, labelsize=6)

    # Lire le fichier "critères.txt" et utiliser son contenu comme titre de la légende
    with open("critères.txt", "r") as file:
        text = "Critères de séléction:"+"\n"+file.read()
    ax.legend(title=text+'\n'+c2)

    # Demander à l'utilisateur s'il souhaite enregistrer le graphique dans un fichier png
    if prompt_user("Voulez-vous enregistrer les données du graphique dans un fichier png ?"):
        # Demander le nom du fichier ou le générer automatiquement
        print("Voulez-vous choisir le nom du fichier ? nom = [text you enter].png (répondez 'OUI' ou 'NON')")
        ans = input(str())
        ans = q.answer_protction_bool(ans)
        # Si l'utilisateur veut choisir le nom du fichier, demander le nom et ajouter l'extension '.png'
        if ans == 'OUI':
            print("Entrez le nom que vous choisissez")
            text = str(input())
            name = text + '.png'
            name = q.is_valid_filename(name, "png")
        # Si l'utilisateur ne veut pas choisir le nom du fichier, générer le nom du fichier automatiquement
        if ans == 'NON':
            name = g.graph_name(c1, c2, '.png')
        valid = q.can_write_file(name)
        if valid:
            # Sauvegarder le graphique dans un fichier png
            plt.savefig(name)
            print(f"Données du graphique enregistrées dans le fichier : {name}")

    # Afficher le graphique
    plt.show()