print('Chargement du code en cours ... ')

import manipulation_fichier as f
import ask_user
import answer_protection as q
import remove
import os # Voir ligne 37

try:

    chemin_excel = 'Liste-des-vols.xlsx'
    data_frame = f.lire_excel(chemin_excel)

    with open("critères.txt", "w") as fichier:
        chaine = "".join("")
        fichier.write(chaine)

    # PART1
    print('Code chargé !')
    print("Voulez-vous afficher le dataframe initial ? (répondez 'OUI' ou 'NON')")
    ans = input()
    ans = q.answer_protction_bool(ans)
    if ans == 'OUI':
        f.display_dataframe(data_frame)

    # PART2
    ask_1 = True
    name, ask_1 = ask_user.ask_user(chemin_excel, True, True, 'Sort', chemin_excel, data_frame, ask_1)

    # PART3/4
    ask_user.ask_user(name, True, False, 'Graph', chemin_excel, data_frame, ask_1)

    pass
except KeyboardInterrupt:
    print("\nProgramme interrompu par l'utilisateur.")
    remove.remove()
except (OSError, IOError):
    print("Erreur inconnue. Veuillez essayer de relancer le programme.")