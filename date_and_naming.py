import datetime
import re

# Fonction pour obtenir la date actuelle
def get_current_date():
    # Obtenir la date et l'heure actuelles
    current_date = datetime.datetime.now()
    # Formater la date et l'heure actuelles au format "année, mois, jour"
    formatted_date = current_date.strftime("%Y, %m, %d")
    # Renvoyer la date formatée
    return formatted_date

# Fonction pour nettoyer un texte
def clean_text(text):
    # Remplacer les sauts de ligne par un espace
    text = text.replace('\n', ' ')
    # À ce stade, il peut y avoir des espaces multiples entre certains mots.
    # Utiliser une expression régulière pour remplacer tous les espaces multiples par un seul espace.
    text = re.sub(' +', ' ', text)
    # Renvoyer le texte nettoyé
    return text
