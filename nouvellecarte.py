import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.patheffects as pe
import date_and_naming as d
import answer_protection as q

PROVINCES = {
    'Alberta': (53, -115),
    'Colombie-Britannique': (53, -127),
    'Manitoba': (54, -97),
    'Nouveau-Brunswick': (47, -66),
    'Terre-Neuve-et-Labrador': (53, -58),
    'Nouvelle-Écosse': (45, -63),
    'Ontario': (50, -85),
    'Île-du-Prince-Édouard': (46, -63),
    'Québec': (52, -72),
    'Saskatchewan': (53, -106),
    'Territoires du Nord-Ouest': (66, -119),
    'Nunavut': (68, -93),
    'Yukon': (64, -134)
}

VILLES = {
    'Ottawa': (45.4215, -75.6919),
    'Toronto': (43.6532, -79.3832),
    'Montréal': (45.5017, -73.5673),
    'Vancouver': (49.2827, -123.1207)
}

VILLES_LIGNES = {
    1: ['Montréal', 'Vancouver'],
    2: ['Vancouver', 'Toronto'],
    3: ['Montréal', 'Toronto'],
    4: ['Ottawa', 'Toronto'],
    5: ['Ottawa', 'Vancouver'],
    6: ['Ottawa', 'Montréal']
}

Vols = ['Montréal_Vancouver',
        'Vancouver_Toronto',
        'Montréal_Toronto',
        'Ottawa_Toronto',
        'Ottawa_Vancouver',
        'Ottawa_Montréal']

def get_color(city, dfc):
    color = dfc.loc[dfc['Ville'] == city, 'Color Label'].values
    return color[0] if len(color) > 0 else 'City not found'


def get_informations_meteo(meteo):
    return {
        row['Ville']: {
            'temperature': round(row['Température (°C)'], 2),
            'couverture_nuageuse': row['Couverture nuageuse']
        } for _, row in meteo.iterrows()
    }


def draw_map():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1)
    carte = Basemap(llcrnrlon=-140, llcrnrlat=40, urcrnrlon=-50, urcrnrlat=70, resolution='l', projection='merc', ax=ax)
    carte.fillcontinents(color='#FFEECC', lake_color='#DDEEFF', zorder=1)
    carte.drawmapboundary(fill_color='lightblue')
    carte.drawcountries(linewidth=0.5, color='black')
    carte.drawcoastlines(linewidth=0.5, color='black')
    carte.drawstates(linewidth=0.5, color='gray')
    carte.drawparallels(range(40, 80, 10), linewidth=0.5, labels=[1, 0, 0, 0], color='black', fontsize=6)
    carte.drawmeridians(range(-180, 181, 20), linewidth=0.5, labels=[0, 0, 0, 1], color='black', fontsize=6)
    return carte


def afficher_villes_ligne(carte, num_ligne, dfc, informations_meteo):
    ligne = VILLES_LIGNES[num_ligne]
    for ville in ligne:
        color = get_color(ville, dfc)
        lat, lon = VILLES[ville]
        x, y = carte(lon, lat)
        carte.plot(x, y, 'o', markersize=8, markerfacecolor='white', markeredgecolor='red')
        plt.text(x, y, ville, color='white', fontsize=10, ha='center', va='center',
                 bbox=dict(facecolor=color, edgecolor='black', boxstyle='round'))

        effet_de_contour = [pe.Stroke(linewidth=1.5, foreground='black'), pe.Normal()]
        effet_ombre = pe.withStroke(linewidth=2, foreground='gray')
        plt.text(x, y - 400000, f"Température: {informations_meteo[ville]['temperature']}°C", color='white',
                 weight='bold', fontsize=8, ha='center', va='center', path_effects=[effet_ombre] + effet_de_contour)
        plt.text(x, y - 590000, f"Couverture nuageuse: {informations_meteo[ville]['couverture_nuageuse']}",
                 color='white', weight='bold', fontsize=8, ha='center', va='center',
                 path_effects=[effet_ombre] + effet_de_contour)


def carte(meteo, dfc, enregistrer):
    carte = draw_map()

    for province, (lat, lon) in PROVINCES.items():
        x, y = carte(lon, lat)
        text = plt.text(x, y, province, fontsize=6, color='black', ha='center', va='center', style='italic')
        text.set_path_effects([pe.withStroke(linewidth=0.5, foreground='grey')])

    informations_meteo = get_informations_meteo(meteo)

    print("Choisissez la ligne que vous souhaitez emprunter:")
    for num_ligne, villes_ligne in VILLES_LIGNES.items():
        print(f"{num_ligne}. {villes_ligne[0]} - {villes_ligne[1]}")

    num_ligne = str(input("Entrez le numéro de la ligne : "))
    num_ligne=q.answer_protection_1_6(num_ligne)
    afficher_villes_ligne(carte, num_ligne, dfc, informations_meteo)

    ligne_coord = [(VILLES[ville][1], VILLES[ville][0]) for ville in VILLES_LIGNES[num_ligne]]
    carte.drawgreatcircle(*ligne_coord[0], *ligne_coord[1], linewidth=2, color='red', linestyle='dashed')

    titre = 'Date actuelle : ' + d.get_current_date()
    plt.title(titre)

    legend_labels = {
        'bon': 'Vert - Faible Pollution',
        'moyen': 'Orange - Pollution Moyenne',
        'mauvais': 'Rouge - Forte Pollution'
    }
    plt.legend(handles=[
        plt.Line2D([], [], color='green', marker='s', linestyle='None', markersize=10),
        plt.Line2D([], [], color='orange', marker='s', linestyle='None', markersize=10),
        plt.Line2D([], [], color='red', marker='s', linestyle='None', markersize=10)
    ], labels=[legend_labels['bon'], legend_labels['moyen'], legend_labels['mauvais']])

    if enregistrer == 'OUI':
        print("Voulez-vous choisir le nom du fichier ? nom = [text you enter].png (répondez 'OUI' ou 'NON')")
        ans = str(input())
        if ans == 'OUI':
            print("Entrez le nom que vous choisissez")
            text = str(input())
            name = text + '.png'
            name = q.is_valid_filename(name, "png")
        elif ans == 'NON':
            name = str(Vols[num_ligne-1])+''+d.get_current_date()+'.png'
        valid=q.can_write_file(name)
        if valid:
            plt.savefig(name)
            print(f"Carte enregistrée dans le fichier {name}")

    plt.show()