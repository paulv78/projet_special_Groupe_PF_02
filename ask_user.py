import sort_dataframe as s
import manipulation_fichier as f
import parameter_definition as pc
import Aeroport as y
import date_and_naming as d
import answer_protection as q

# Définition de la fonction 'ask_user'

"""
Si mode n'est pas égal à 'Sort' ou 'Graph', la fonction ne fait rien. Il serait judicieux de s'assurer que mode a 
toujours une valeur valide, ou d'ajouter une clause else pour gérer les cas où mode a une valeur inattendue.

Si ask_manual_selection est False, la fonction ask_user ne fait rien non plus. Il pourrait être préférable d'avoir un 
comportement par défaut ou un message d'erreur lorsque ask_manual_selection est False.

Dans la partie où ask_for_save est vérifiée, si save est 'NON' et que ask_for_save est True, un fichier temporaire est 
créé. Cependant, il n'y a aucune indication que ce fichier est ensuite utilisé pour quelque chose. Si ce n'est pas le 
cas, il peut être inutile de créer ce fichier.

En fin de compte, la fonction peut sortir sans retour explicite, ce qui signifie qu'elle retournera None. Si le code 
appelant s'attend à un certain retour de la fonction ask_user, cela pourrait causer des problèmes.
"""
def ask_user(input_file, ask_manual_selection, ask_for_save, mode, original_file, data_frame, ask_1):

    # Initialiser la variable 'ans' avec 'OUI'
    ans = 'OUI'
    # Initialiser le compteur 'n' à 1
    n = 1

    # Vérifie si l'utilisateur a demandé une sélection manuelle
    if ask_manual_selection == True:
        if mode == 'Sort':
            # Demande à l'utilisateur s'il souhaite effectuer une sélection manuelle des données
            print("Souhaitez-vous faire une sélection manuelle dans ces données (répondez 'OUI' ou 'NON')")
        if mode == 'Graph' and ask_1 is True:
            # Demande à l'utilisateur s'il souhaite générer un graphique à partir des données
            print("Souhaitez-vous générer un graphique à partir des données ? (répondez 'OUI' ou 'NON')")
            # Enregistre la réponse de l'utilisateur
            ans = str(input())
            ans = q.answer_protction_bool(ans)
            if ans == 'OUI':
                # Si l'utilisateur souhaite générer un graphique, demande s'il souhaite effectuer un tri préalable des données
                print("Souhaitez-vous un tri préalable des donnée avant la création du graphique (répondez 'OUI' ou 'NON')")
            elif ans == 'NON' :
                # Si l'utilisateur ne souhaite pas générer un graphique, renvoie le fichier original et False
                return original_file, False
        elif mode == 'Graph' and ask_1 is False:
            # Si l'utilisateur ne souhaite pas générer un graphique, demande s'il souhaite effectuer un tri préalable des données
            print("Souhaitez-vous un tri préalable des données avant la création du graphique (répondez 'OUI' ou 'NON')")
        # Enregistre la réponse de l'utilisateur
        ans = str(input())
        ans = q.answer_protction_bool(ans)

    # Si l'utilisateur a répondu 'OUI' à la question précédente
    if ans == 'OUI':
        # Demande à l'utilisateur de choisir le critère de filtrage des données
        print("Par quel critère souhaitez-vous filtrer les données ? Options possibles : Compagnie (1), Avion (2), Statut (3), "
              "Heure de départ (4), Heure d'arrivée (5), Ville de départ (6), Ville d'arrivée (7)")
        # Définit la liste des critères possibles
        criteria_list = ['Companie', 'Avion', 'Statut', 'Heure de départ', "Heure d'arrivée", 'Ville de départ',"Ville d'arrivée"]
        # Enregistre le(s) critère(s) choisi(s) par l'utilisateur
        criteria = input("Entrez les chiffres séparés par des espaces : ")
        criteria = q.answer_protction_number_list(criteria)
        # Convertit la réponse de l'utilisateur en une liste d'entiers
        criteria_int = [int(c.strip()) for c in criteria.split(" ")]

        # Crée une chaîne de caractères avec les critères choisis par l'utilisateur
        criteria_names = ', '.join(criteria_list[criteria - 1] for criteria in criteria_int)
        # Informe l'utilisateur que la recherche sera effectuée selon les critères qu'il a choisis
        print(f"Une recherche sera effectuée pour les critères suivants : {criteria_names}")

        # Parcourt la liste des critères choisis par l'utilisateur
        for i in range(0, len(criteria_int)):
            # Ajoute chaque critère choisi par l'utilisateur dans un fichier nommé 'critères.txt'
            with open("critères.txt", "a") as fichier:
                chaine = "".join(criteria_list[criteria_int[i] - 1]+"\n")
                fichier.write(chaine)

            # Informe l'utilisateur que la recherche sera effectuée pour le critère en cours
            print(f"Une recherche sera effectuée pour le critère suivant : {criteria_list[criteria_int[i]-1]}.")
            print("Les critères disponibles sont :")
            # Trie le dataframe selon le critère en cours
            df = s.sort_dataframe(input_file, criteria_int[i])
            # Crée un nom temporaire pour le fichier
            temp_name = 'temp' + str(i) + '.xlsx'
            # Écrit le dataframe trié dans un fichier Excel temporaire
            f.ecrire_excel_p(df, temp_name)
            # Met à jour le nom du fichier d'entrée
            input_file = temp_name

        # Vérifie si l'utilisateur a demandé à sauvegarder les résultats
        if ask_for_save == True:
            # Demande à l'utilisateur s'il souhaite enregistrer la table générée dans un fichier Excel
            print ("Souhaitez-vous enregistrer la table générée dans un fichier excel ? (répondez 'OUI' ou 'NON')")
            # Enregistre la réponse de l'utilisateur
            save = str(input())
            save = q.answer_protction_bool(save)
            if save == 'OUI':
                # Demande à l'utilisateur s'il souhaite choisir le nom du fichier
                print("Voulez-vous choisir le nom du fichier ? nom = [text you enter].xlsx (répondez 'OUI' ou 'NON')")
                # Enregistre la réponse de l'utilisateur
                ans = input(str())
                ans = q.answer_protction_bool(ans)
                if ans == 'OUI':
                    # Demande à l'utilisateur d'entrer le nom qu'il a choisi
                    print("Entrez le nom que vous choisissez")
                    # Enregistre le nom choisi par l'utilisateur
                    text = str(input())
                    # Crée le nom du fichier
                    name = text + '.xlsx'
                    name = q.is_valid_filename(name, "xlsx")
                if ans == 'NON':
                    # Si l'utilisateur ne souhaite pas choisir le nom du fichier, utilise les critères de sélection comme nom du fichier
                    with open("critères.txt", "r") as file:
                        text = "Critères de sélection" + "\n" + file.read()
                        # Nettoie le texte et ajoute la date courante
                        text = d.clean_text(text) + ' ' + d.get_current_date()
                    # Crée le nom du fichier
                    name = 'table ' + str(n) + ' ' + text + '.xlsx'
                # Écrit le dataframe dans un fichier Excel avec le nom choisi
                valid = q.can_write_file(name)
                if valid:
                    f.ecrire_excel(df, name)
                    # Informe l'utilisateur que les données filtrées ont été enregistrées dans le fichier
                    print(f"Les données filtrées ont été enregistrées dans le fichier '{name}'.")
            else:
                # Si l'utilisateur ne souhaite pas enregistrer les données, crée un nom temporaire pour le fichier
                name = 'table_temp' + str(n) + '.xlsx'
                # Écrit le dataframe dans un fichier Excel avec le nom temporaire
                f.ecrire_excel_p(df, name)
        else:
            # Si l'utilisateur n'a pas demandé à sauvegarder les résultats, crée un nom temporaire pour le fichier
            name = 'table_temp' + str(n) + '.xlsx'
            # Écrit le dataframe dans un fichier Excel avec le nom temporaire
            f.ecrire_excel_p(df, name)

        # Demande à l'utilisateur s'il souhaite effectuer une sélection supplémentaire dans les données
        print("souhaitez-vous faire une sélection supplémentaire dans ces données (répondez 'OUI' ou 'NON')")
        # Enregistre la réponse de l'utilisateur
        answer = str(input())
        answer = q.answer_protction_bool(answer)
        if answer == 'OUI':
            # Si l'utilisateur souhaite effectuer une sélection supplémentaire, rappelle la fonction 'ask_user' avec les nouveaux paramètres
            ask1 = True
            if mode == 'Sort':
                n = n + 1
                return ask_user(name, False, True, 'Sort', original_file, data_frame, ask1)
            if mode == 'Graph':
                return ask_user(name, False, False, 'Graph', original_file, data_frame, ask1)

        if answer == 'NON' and mode == 'Sort':
            # Si l'utilisateur ne souhaite pas effectuer une sélection supplémentaire et si le mode est 'Sort'
            print("Souhaitez-vous générer un graphique à partir des données ? (répondez 'OUI' ou 'NON')")
            # Enregistre la réponse de l'utilisateur
            rep = str(input())
            rep = q.answer_protction_bool(rep)
            if rep == 'OUI':
                # Si l'utilisateur souhaite générer un graphique, demande s'il souhaite utiliser les données déjà modifiées pour tracer le graphique
                print("Voulez-vous utiliser les données déjà mofifiées pour tracer le graphique ? (répondez 'OUI' ou 'NON')")
                # Enregistre la réponse de l'utilisateur
                answer = str(input())
                answer = q.answer_protction_bool(answer)
                if answer == 'OUI':
                    # Si l'utilisateur souhaite utiliser les données déjà modifiées pour tracer le graphique, renvoie le nom du fichier et False
                    return name, False
                if answer == 'NON':
                    # Si l'utilisateur ne souhaite pas utiliser les données déjà modifiées pour tracer le graphique, renvoie le nom du fichier original et False pour ne pas redemander deux fois d'affilée
                    name = original_file
                    # Réinitialise le fichier des critères
                    with open("critères.txt", "w") as fichier:
                        chaine = "".join("")
                        fichier.write(chaine)
                    return name, False
            else:
                # Si l'utilisateur ne souhaite pas générer un graphique, appelle la fonction 'aeroports' avec le dataframe en paramètre
                y.aeroports(data_frame)

        if answer == 'NON' and mode == 'Graph':
            # Si l'utilisateur ne souhaite pas effectuer une sélection supplémentaire et si le mode est 'Graph'
            # Lit le fichier Excel et stocke le dataframe résultant
            df = f.lire_excel(name)
            # Définit les paramètres pour le graphique
            pc.parameter_definition(df)

    # Si l'utilisateur a répondu 'NON' à la première question et si le mode est 'Sort'
    if ans == 'NON' and mode == 'Sort':
        # Demande à l'utilisateur s'il souhaite générer un graphique à partir des données
        print("Souhaitez-vous générer un graphique à partir des données ? (répondez 'OUI' ou 'NON')")
        # Enregistre la réponse de l'utilisateur
        rep = str(input())
        rep = q.answer_protction_bool(rep)
        if rep == 'OUI':
            name = original_file
            # Réinitialise le fichier des critères
            with open("critères.txt", "w") as fichier:
                chaine = "".join("")
                fichier.write(chaine)
            return name, False
        else:
            # Si l'utilisateur ne souhaite pas générer un graphique, appelle la fonction 'aeroports' avec le dataframe en paramètre
            y.aeroports(data_frame)

    # Si l'utilisateur a répondu 'NON' à la première question et si le mode est 'Graph'
    if ans == 'NON' and mode == 'Graph':
        # Lit le fichier Excel et stocke le dataframe résultant
        df = f.lire_excel(input_file)
        # Définit les paramètres pour le graphique
        pc.parameter_definition(df)
    # Si l'utilisateur sort de la fonction
    y.aeroports(data_frame)