import date_and_naming as d

def graph_name(c1,c2,extension):
    with open("critères.txt", "r") as file: # Ouverture du fichier "critères.txt" en mode lecture
        text = "Critères de sélection" + "\n" + file.read() # Lecture du contenu du fichier et l'ajout au texte "Critères de séléction"
    text = d.clean_text(text) + ' ' + d.get_current_date() # Nettoyage du texte avec la fonction clean_text et l'ajout de la date courante
    name = 'plot_frequency_count_by_'+str(c1)+'_by_'+str(c2)+' '+text+extension # Construction du nom du graphique
    return name # Retourne le nom du graphique