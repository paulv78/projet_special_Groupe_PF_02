import os
def remove():
    os.remove("critères.txt")
    # Obtenir le chemin du répertoire courant
    repertoire_courant = os.getcwd()
    print('Fichier temporaire de nomenclature supprimé')

    # Parcourir tous les fichiers du répertoire courant
    for nom_fichier in os.listdir(repertoire_courant):
        # Vérifier si le fichier a 'temp' dans son nom
        if 'temp' in nom_fichier:
            # Construire le chemin complet du fichier
            chemin_fichier = os.path.join(repertoire_courant, nom_fichier)
            # Supprimer le fichier
            os.remove(chemin_fichier)

    for nom_fichier in os.listdir(repertoire_courant):
        # Vérifier si le fichier a 'temp' dans son nom
        if 'teble_temp' in nom_fichier:
            # Construire le chemin complet du fichier
            chemin_fichier = os.path.join(repertoire_courant, nom_fichier)
            # Supprimer le fichier
            os.remove(chemin_fichier)

    print('Fichiers temporaires supprimés')