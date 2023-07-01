"""
Les fonctions de cette classe permettent à l'utilisateur de re-saisir une réponse si la réponse n'est pas conforme aux
besoins du script, évitant ainsi un crash, comportement inattendu ou dysfonctionnement du script.
"""
import re
import os #(see line 143)
import tempfile

#checks if the answer is either oui ou non
def answer_protction_bool(ans):
    ask_again = True
    while ask_again:
        if ans.lower() == 'oui':
            return str('OUI')
        elif ans.lower() == 'non':
            return str('NON')
        else:
            print(f"Réponse non valide, répondez par 'OUI' ou 'NON' s'il-vous plaît")
            ans = str(input("Entrez votre réponse : "))

#verifies if the number given is between 1 and 7
def answer_protction_number_list(ans):
    # remove spaces at the beginning and the end of the string
    input_string = ans.strip()
    # split the string by spaces
    values = input_string.split(" ")
    # go through all values and check them
    for value in values:
        # try to convert each value to an integer
        try:
            value_int = int(value)
        except ValueError:
            # if it's not possible, return "no"
            print("Réponse non valide. Format invalide ou chiffres inexistants dans la liste")
            ans = str(input("Entrez les chiffres (1-7) séparés par des espaces : "))
            return answer_protction_number_list(ans)
        # check if the value is within the range 1-7
        if not 1 <= value_int <= 7:
            # if it's not, return "no"
            print("Réponse non valide. Format invalide ou chiffres inexistants dans la liste")
            ans = str(input("Entrez les chiffres (1-7) séparés par des espaces : "))
            return answer_protction_number_list(ans)
    # if all values have passed the checks, return "yes"
    return ans

#checks if the elements entered are in the given column of the dataframe
def answer_protction_elements_in_nth_column(df,column, input_string):
    up=False
    if column !=0:
        column=column+1 #mapps the column from list column to dataframe column
        up=True

    # Split the input string by commas
    values = input_string.split(",")

    # Remove leading and trailing whitespace from each value
    values = [value.strip() for value in values]

    # Get the values of the nth column
    column_values = df.iloc[:, column].astype(str).str.strip().values.tolist()

    # Check if all the values in input_string exist in the column values
    if all(value in column_values for value in values):
        return input_string
    else:
        print(f"Réponse non valide. Format invalide ou élément inexistant")
        ans = str(input("Entrez les paramètres séparés par des espaces : "))
        if up:
            return answer_protction_elements_in_nth_column(df,column-1, ans)
            #if the number was uped by one to be mapped to the df, it's unmapped
            # so that it's not mapped twice when the function is called again
        if not up:
            return answer_protction_elements_in_nth_column(df, column, ans)

#checks if the rows entered are in the given dataframe
def answer_protction_elements_in_rows(df, input_string):

    # Split the input string by spaces
    row_numbers = input_string.split()

    # Check if all the row numbers are integers
    if all(row_number.isdigit() for row_number in row_numbers):
        # Check if all the row numbers exist in the DataFrame index
        if all(int(row_number) in df.index for row_number in row_numbers):
            return input_string
        else:
            print("Réponse non valide. Format invalide ou ligne inexistante")
            ans = str(input("Entrez les lignes séparées par des espaces : "))
            return answer_protction_elements_in_rows(df, ans)
    else:
        print("Réponse non valide. Format invalide ou ligne inexistante")
        ans = str(input("Entrez les lignes séparées par des espaces : "))
        return answer_protction_elements_in_rows(df, ans)

#checks if a difit between 1 and 6 is entered
def answer_protection_1_6(input_str):
    pattern = r'^\s*[1-6]\s*$'
    if re.match(pattern, input_str):
        return int(input_str)
    else:
        print("Numéro de ligne invalide. Format invalide ou ligne inexistante")
        ans = str(input("Veuillez entrer un nombre entre 1 et 6 : "))
        return answer_protection_1_6(ans)

# vérifie si l'utilisateur a bien rentré 'A' ou 'B'
def answer_protection_A_B(ans):
    ask_again = True
    while ask_again:
        if ans.lower() == 'a':
            return str('A'),True
        elif ans.lower() == 'b':
            return str('B'),False
        else:
            print(f"Réponse non valide, répondez par 'A' ou 'B' s'il-vous plaît")
            ans = str(input("Entrez votre réponse : "))

#checks if the user created a valid filename
def is_valid_filename(filename, extension):
    pattern = r'^[\w\-. ]+\.' + extension + '$'
    if 'table_temp' in filename.lower():
        print("Nom choisi invalide")
        print("Le nom ne doit pas contenir le mot 'table_temp'.")
        ans = str(input("Veuillez entrer un nouveau nom : "))
        ans = ans + '.' + extension  # adds the extension to the new name
        return is_valid_filename(ans, extension)
    elif 'temp' in filename.lower():
        print("Nom choisi invalide")
        print("Le nom ne doit pas contenir le mot 'temp'.")
        ans = str(input("Veuillez entrer un nouveau nom : "))
        ans = ans + '.' + extension  # adds the extension to the new name
        return is_valid_filename(ans, extension)
    elif re.match(pattern, filename):
        return filename
    else:
        print("Nom choisi invalide")
        print("Le nom ne doit contenir que des caractères alphanumériques, des traits d'union ou des espaces.")
        ans = str(input("Veuillez entrer un nouveau nom : "))
        ans = ans + '.' + extension  # adds the extension to the new name
        return is_valid_filename(ans, extension)

# Si un fichier demandé par l'utilisateur n'a pas pu être écrit, la fonction notifie n'utilisateur
# et le script continue de s'executer
def can_write_file(filename):
    try:
        # Essaie de créer un fichier temporaire pour vérifier si le fichier peut être créé dans le répertoire courant
        with tempfile.NamedTemporaryFile(dir='.', prefix=filename, delete=True):
            pass
        return True
    except (OSError, IOError):
        print("Le fichier n'a pas pu être écrit.")
        return False