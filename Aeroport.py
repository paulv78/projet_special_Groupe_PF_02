import remove as r
import airport_frequentation as xc
import APImeteo as ac
import nouvellecarte as ncc
import meteo_criteria as mc
import answer_protection as q


# Fonction pour convertir une chaîne de caractères en booléen
def str_to_bool(string):
    string = q.answer_protction_bool(string)
    # Si la chaîne est 'OUI', la convertir en True
    if string == 'OUI':
        string = True
    # Sinon, la convertir en False
    else:
        string = False
    # Renvoyer la valeur booléenne
    return string


# Fonction principale pour gérer les informations des aéroports
def aeroports(data_frame):
    # Demander à l'utilisateur s'il souhaite afficher des informations en lien avec la fréquentation actuelle des aéroports
    print(
        "Voulez-vous afficher des informations en lien avec la fréquentation actuelle des aéroports ? (répondez 'OUI' ou 'NON')")
    # Enregistrer la réponse de l'utilisateur
    ans = str(input())
    ans = q.answer_protction_bool(ans)
    # Si la réponse est 'OUI'
    if ans == 'OUI':
        # Obtenir la fréquentation totale des aéroports
        total_frequentation = xc.frequentation(data_frame)

        # Demander à l'utilisateur s'il souhaite afficher la météo de chaque aéroport
        print("Voulez-vous afficher la météo de chaque aéroport ? (répondez 'OUI' ou 'NON')")
        ans = str(input())
        ans = q.answer_protction_bool(ans)
        # Convertir la réponse de l'utilisateur en booléen
        ans = str_to_bool(ans)
        # Obtenir les informations météo
        meteo = ac.weather_info(ans)

        # Compter le nombre d'avions par heure pour chaque aéroport
        df3 = xc.count_planes_by_hour(data_frame)

        # Demander à l'utilisateur s'il souhaite afficher la fréquentation de chaque aéroport
        print("Voulez-vous afficher la fréquentation de chaque aéroport ? (répondez 'OUI' ou 'NON')")
        ans = str(input())
        ans = q.answer_protction_bool(ans)
        # Convertir la réponse de l'utilisateur en booléen
        ans = str_to_bool(ans)
        # Afficher la fréquentation de chaque aéroport
        xc.plot_frequentation(df3, ans)

        # Demander à l'utilisateur s'il souhaite afficher la fréquentation maximale de chaque aéroport
        print("Voulez-vous afficher la fréquentation maximale de chaque aéroport ? (répondez 'OUI' ou 'NON')")
        ans = str(input())
        ans = q.answer_protction_bool(ans)
        # Convertir la réponse de l'utilisateur en booléen
        ans = str_to_bool(ans)
        # Afficher la fréquentation maximale de chaque aéroport
        xc.peak_frequency(df3, ans)

        # Fusionner la fréquentation totale des aéroports et les informations météo
        dfc = mc.criteria(total_frequentation, meteo)

        # Demander à l'utilisateur s'il souhaite enregistrer une carte montrant un trajet entre deux aéroports choisis, ainsi que la qualité de l'air dans ces deux aéroports
        print("Voulez-vous générer une carte montrant un trajet entre deux aéroports que vous pourrez choisir, ainsi que la qualité de l'air dans ces deux aéroports ?")
        ans = str(input())
        ans = q.answer_protction_bool(ans)
        if ans == 'OUI':
            print("Une carte montrant un trajet entre deux aéroports que vous pourrez choisir, ainsi que la qualité de l'air dans ces deux aéroports sera générée. Souhaitez-vous l'enregistrer ? (répondez 'OUI' ou 'NON')")
            enregistrer = str(input())
            enregistrer = q.answer_protction_bool(enregistrer)
            # Générer et éventuellement enregistrer la carte
            ncc.carte(meteo, dfc, enregistrer)

    # Supprimer les fichiers temporaires
    r.remove()
    # Quitter le programme
    exit()