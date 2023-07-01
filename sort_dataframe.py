# On importe le module qui contient les fonctions de manipulation de fichier
import manipulation_fichier as f
import answer_protection as q

# Cette fonction trie un dataframe selon des critères spécifiques
def sort_dataframe(fichier_in, criteria):
    # On lit le fichier Excel et on le transforme en dataframe
    df = f.lire_excel(fichier_in)
    # On définit une liste de critères disponibles
    criteria_list = ['Cie aérienne', 'Avion', 'Statut', 'Heure Départ', "Heure Arrivée", 'Ville départ', "Ville Arrivée"]
    # On obtient le nom de colonne en fonction du critère sélectionné par l'utilisateur
    column_name = criteria_list[criteria - 1]
    # On obtient les valeurs uniques de cette colonne
    unique_values = df[column_name].unique()
    # On trie ces valeurs sans tenir compte de la casse (sinon erreur)
    sorted_values = sorted(unique_values, key=lambda x: x.lower())
    # On affiche chaque valeur triée pour l'utilisateur
    for value in sorted_values:
        print(value)
    # On demande à l'utilisateur de choisir les critères qu'il souhaite utiliser
    print("Quels critères souhaitez-vous utiliser ? (séparez les critères par des virgules)")
    # On récupère la saisie de l'utilisateur, on supprime les espaces supplémentaires et on divise la chaine en fonction des virgules
    criteria_input = input().strip()
    column = criteria-1
    criteria_input = q.answer_protction_elements_in_nth_column(df, column, criteria_input)
    criteria_list = [c.strip() for c in criteria_input.split(",")]
    # On écrit les critères sélectionnés dans un fichier
    with open("critères.txt", "a") as fichier:
        chaine = "\n".join("    " + critere for critere in criteria_list)
        fichier.write(chaine + "\n")
    # On filtre le dataframe pour ne garder que les lignes où le critère correspond à ce qui a été sélectionné par l'utilisateur
    filtered_df = df[df[column_name].str.strip().isin(criteria_list)]
    # On trie le dataframe filtré
    sorted_df = filtered_df.sort_values(by=column_name, key=lambda x: x.str.lower())
    # On affiche le dataframe trié
    f.display_dataframe(sorted_df)
    # On demande à l'utilisateur s'il souhaite supprimer des lignes
    print("Souhaitez-vous supprimer des lignes dans ces données ? (répondez 'OUI' ou 'NON')")
    supp = str(input())
    supp = q.answer_protction_bool(supp)
    # Si l'utilisateur répond "OUI", on lui demande les lignes à supprimer et on supprime ces lignes du dataframe
    while supp == 'OUI':
        print("Entrez les lignes que vous souhaitez supprimer, séparées d'un espace")
        indices = str(input())
        indices=q.answer_protction_elements_in_rows(sorted_df, indices)
        indices = [float(item.strip()) for item in indices.split(" ")]
        sorted_df = sorted_df.drop(indices)
        f.display_dataframe(sorted_df)
        print("Souhaitez-vous supprimer d'autres lignes dans ces données ? (répondez 'OUI' ou 'NON')")
        supp = str(input())
        supp = q.answer_protction_bool(supp)
    # On retourne le dataframe final après avoir appliqué toutes les modifications
    return sorted_df