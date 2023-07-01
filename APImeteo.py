import requests
import pandas as pd

def weather_info(print_info):
    base_url = "http://api.openweathermap.org/data/2.5/forecast?" # Base de l'URL pour l'API OpenWeatherMap
    api_key = "00b37b40233b39117011b56a022a88ba" # Clé de l'API OpenWeatherMap
    villes = ["Montréal", "Ottawa", "Toronto", "Vancouver"] # Liste des villes pour lesquelles nous voulons des informations météorologiques

    weather_data = [] # Liste vide pour stocker les informations météorologiques
    for ville in villes: # Pour chaque ville dans la liste des villes
        data = requests.get(f"{base_url}q={ville}&appid={api_key}").json() # Faire une requête à l'API OpenWeatherMap pour obtenir des informations météorologiques
        couverture_nuageuse = data["list"][0]["weather"][0]["description"] # Obtenir la description de la couverture nuageuse
        temperature = data["list"][0]["main"]["temp"] - 273.15 # Convertir la température de Kelvin à Celsius

        if print_info: # Si l'utilisateur veut imprimer les informations météorologiques
            print(f"Ville : {ville}\nCouverture nuageuse : {couverture_nuageuse}\nTempérature : {temperature:.1f}°C\n-----------------------------") # Imprimer les informations météorologiques

        weather_data.append({ # Ajouter les informations météorologiques à la liste des données météorologiques
            "Ville": ville,
            "Couverture nuageuse": couverture_nuageuse,
            "Température (°C)": temperature
        })

    return pd.DataFrame(weather_data) # Retourner les données météorologiques sous forme de DataFrame pandas
