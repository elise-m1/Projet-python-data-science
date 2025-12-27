# Il s'agit du fichier dans lequel nous pouvons écrire toutes nos fonctions que nous appelerons dans le notebook

#Importation des librairies qui vont nous servir
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# ---- Fonctions pour nettoyer la base de données -----------

def simplification_statut(val):
    """
    Transforme le statut détaillé en Privé/Public/Autre
    """

    statut = str(val).lower() #robustesse
    if "public" in statut :
        return "Public"
    elif "priv" in statut :
        return "Privé"
    else :
        return "Autre"

#Nettoyage de la base de données
def nettoyage_base(df):
    """
    Supprime les colonnes unutiles et renomme les variables
    """

    #Suppression des colonnes
    colonnes_suppr = [
        "Session",
        'Filière de formation.1',
        'Filière de formation détaillée bis',
        'Filière de formation très détaillée',
        'Dont effectif des candidates pour une formation',
        'Effectif total des candidats en phase principale',
        'Dont effectif des candidats ayant postulé en internat',
        'Effectif des candidats néo bacheliers généraux en phase principale',
        'Dont effectif des candidats boursiers néo bacheliers généraux en phase principale',
        'Effectif des candidats néo bacheliers technologiques en phase principale',
        'Dont effectif des candidats boursiers néo bacheliers technologiques en phase principale',
        'Effectif des candidats néo bacheliers professionnels en phase principale',
        'Dont effectif des candidats boursiers néo bacheliers professionnels en phase principale',
        'Effectif des autres candidats en phase principale',
        'Effectif des candidats néo bacheliers généraux en phase complémentaire', 'Effectif des candidats néo bacheliers technologique en phase complémentaire', 'Effectif des candidats néo bacheliers professionnels en phase complémentaire',
        'Effectifs des autres candidats en phase complémentaire',
        'Effectif des candidats classés par l’établissement en internat (CPGE)',
        'Effectif des candidats classés par l’établissement hors internat (CPGE)',
        'Effectif des candidats néo bacheliers généraux classés par l’établissement',
        'Dont effectif des candidats boursiers néo bacheliers généraux classés par l’établissement',
        'Effectif des candidats néo bacheliers technologiques classés par l’établissement', 'Dont effectif des candidats boursiers néo bacheliers technologiques classés par l’établissement',
        'Effectif des candidats néo bacheliers professionnels classés par l’établissement',
        'Dont effectif des candidats boursiers néo bacheliers professionnels classés par l’établissement',
        'Effectif des autres candidats classés par l’établissement',
        'Dont effectif des candidates admises',
        "Dont effectif des admis ayant reçu leur proposition d’admission à l'ouverture de la procédure principale",
        "Dont effectif des admis ayant reçu leur proposition d’admission avant le baccalauréat",
        "Dont effectif des admis ayant reçu leur proposition d’admission avant la fin de la procédure principale",
        "Dont effectif des admis en internat",
        "Dont effectif des admis boursiers néo bacheliers",
        "Effectif des admis néo bacheliers technologiques",
        "Effectif des admis néo bacheliers professionnels",
        "Effectif des autres candidats admis",
        "Effectif des admis néo bacheliers généraux ayant eu une mention au bac",
        "Effectif des admis néo bacheliers technologiques ayant eu une mention au bac",
        "Effectif des admis néo bacheliers professionnels ayant eu une mention au bac",
        "Dont effectif des admis issus du même établissement (BTS/CPGE)",
        "Dont effectif des admises issues du même établissement (BTS/CPGE)",
        "% d’admis ayant reçu leur proposition d’admission à l'ouverture de la procédure principale",
        "% d’admis ayant reçu leur proposition d’admission avant le baccalauréat",
        "% d’admis ayant reçu leur proposition d’admission avant la fin de la procédure principale",
        "% d’admis néo bacheliers issus du même établissement (BTS/CPGE)",
        "% d’admis néo bacheliers boursiers",
        "% d’admis néo bacheliers",
        "% d’admis néo bacheliers sans information sur la mention au bac",
        "% d’admis néo bacheliers sans mention au bac",
        "% d’admis néo bacheliers avec mention Assez Bien au bac",
        "% d’admis néo bacheliers avec mention Bien au bac",
        "% d’admis néo bacheliers avec mention Très Bien au bac",
        "% d’admis néo bacheliers avec mention Très Bien avec félicitations au bac",
        "Dont % d’admis avec mention (BG)",
        "% d’admis néo bacheliers technologiques",
        "Dont % d’admis avec mention (BT)",
        "% d’admis néo bacheliers professionnels",
        "Dont % d’admis avec mention (BP)",
        "Effectif des candidats en terminale générale ayant reçu une proposition d’admission de la part de l’établissement",
        "Dont effectif des candidats boursiers en terminale générale ayant reçu une proposition d’admission de la part de l’établissement",
        "Effectif des candidats en terminale technologique ayant reçu une proposition d’admission de la part de l’établissement",
        "Dont effectif des candidats boursiers en terminale technologique ayant reçu une proposition d’admission de la part de l’établissement",
        "Effectif des candidats en terminale professionnelle ayant reçu une proposition d’admission de la part de l’établissement",
        "Dont effectif des candidats boursiers en terminale générale professionnelle ayant reçu une proposition d’admission de la part de l’établissement",
        "Effectif des autres candidats ayant reçu une proposition d’admission de la part de l’établissement",
        "Regroupement 1 effectué par les formations pour les classements",
        "Rang du dernier appelé du groupe 1",
        "Regroupement 2 effectué par les formations pour les classements",
        "Rang du dernier appelé du groupe 2",
        "Regroupement 3 effectué par les formations pour les classements",
        "Rang du dernier appelé du groupe 3",
        "Concours communs et banque d'épreuves",
        "Lien de la formation sur la plateforme Parcoursup",
        "Part des terminales générales qui étaient en position de recevoir une proposition en phase principale",
        "Part des terminales technologiques qui étaient en position de recevoir une proposition en phase principale",
        "Part des terminales professionnelles qui étaient en position de recevoir une proposition en phase principale",
        "etablissement_id_paysage",
        "composante_id_paysage"
    ]
    df = df.drop(columns = [c for c in colonnes_suppr if c in df.columns], errors = "ignore")

    #Renommage
    dict_noms = {
        "Statut de l’établissement de la filière de formation (public, privé…)": "statut",
        "Code UAI de l'établissement": "code_UAI", #identifie chaque établissement de manière unique
        "Code départemental de l’établissement": "code_dep",
        "Département de l’établissement": "dep",
        "Région de l’établissement": "region",
        "Académie de l’établissement": "academie",
        "Commune de l’établissement": "commune",
        "Filière de formation": "filiere",
        "Sélectivité": "selec",
        "Filière de formation très agrégée": "filiere_agr",
        "Filière de formation détaillée": "filiere_det",
        "Coordonnées GPS de la formation": "coord_GPS",
        "Capacité de l’établissement par formation": "nb_places",
        "Effectif total des candidats pour une formation": "nb_can_tot",
        "Effectif total des candidats en phase complémentaire": "nb_can_cmp",
        "Effectif total des candidats classés par l’établissement en phase principale":"nb_candidats_classes_prin",
        "Effectif des candidats classés par l’établissement en phase complémentaire":"nb_candidats_classes_comp",
        "Effectif total des candidats ayant reçu une proposition d’admission de la part de l’établissement":"nb_candidats_prop",
        "Effectif total des candidats ayant accepté la proposition de l’établissement (admis)":"nb_admis",
        "Effectif des admis en phase principale":"nb_admis_prin",
        "Effectif des admis en phase complémentaire":"nb_admis_comp",
        "Effectif des admis néo bacheliers":"nb_admis_bac",
        "Effectif des admis néo bacheliers généraux":"nb_admis_bacg",
        "Dont effectif des admis issus de la même académie":"nb_admis_ac",
        "Dont effectif des admis issus de la même académie (Paris/Créteil/Versailles réunies)":"nb_admis_ac_pcv",
        "% d’admis néo bacheliers issus de la même académie":"part_bac_ac",
        "% d’admis néo bacheliers issus de la même académie (Paris/Créteil/Versailles réunies)":"part_bac_ac_pcv",
        "% d’admis néo bacheliers généraux":"part_bacg",
        "list_com":"appel", #appel commun à plusieurs formations ou propre à cette formation
        "tri":"type_etablissement", #lycee, univ ou autre
        "cod_aff_form":"code_form",
        "Dont effectif des admis néo bacheliers sans mention au bac" : "nb_admis_sans_mention",
        "Dont effectif des admis néo bacheliers avec mention Assez Bien au bac" : "nb_admis_assez_bien",
        "Dont effectif des admis néo bacheliers avec mention Bien au bac" : "nb_admis_bien",
        "Dont effectif des admis néo bacheliers avec mention Très Bien au bac" : "nb_admis_tres_bien",
        "Dont effectif des admis néo bacheliers avec mention Très Bien avec félicitations au bac" : "nb_admis_felicitations",
        "% d’admis dont filles" : "part_filles",
        "Taux d’accès":"taux_acces"
        }
        
    df = df.rename(columns=dict_noms)

    # On filtre pour ne garder que les formations ayant au moins 1 admis
    print(f"Nombre de formations avant filtrage : {len(df)}")

    df = df[df["nb_admis"]>0]

    print(f"Nombre de formations après filtrage : {len(df)}")
    return df
    

def enrichir_donnees(df) :
    """"
    Création de nouvelles variables pour effectuer les analyses
    """
    
    if "taux_acces" in df.columns : 
        #remplacement de la virgule et conversion en numérique
        df["taux_acces_clean"] = pd.to_numeric(
            df["taux_acces"].astype(str).str.replace(",", "."),
            errors="coerce"
        )

    if "part_filles" in df.columns : 
        df["categorie_genre"] = pd.cut(
            df["part_filles"],
            bins=[-1, 40, 60, 101],
            labels=["Dominante masculine", "Mixte", "Dominante féminine"]
        )

    if {"nb_admis_tres_bien", "nb_admis_felicitations", "nb_admis_bac"}.issubset(df.columns):
        df["tb_eleves"] = ((df["nb_admis_tres_bien"].fillna(0) + df["nb_admis_felicitations"].fillna(0))/ df["nb_admis_bac"])*100

        df["niveau_formation"] = pd.cut(
            df["tb_eleves"],
            bins=[-1,0, 10, 30, 1000],
            labels=["Faible (0%)", "Moyen (0-10%)", "Bon (10-30%)", "Très Bon (>30%)"]
        )

    if "statut" in df.columns :
        df["statut_public_prive"] = df["statut"].apply(simplification_statut)

    return df


def charger_donnees(url):
    """
    Fonction exécutant les trois fonctions précédentes afin d'avoir directement accès à une base complète et nettoyée
    """

    print("Chargement du fichier...")
    df = pd.read_csv(url, sep=";") #permet de charger le csv
    df = nettoyage_base(df)
    df = enrichir_donnees(df)

    print(f"Succès {len(df)} lignes prêtes")
    return df

# ------- Fonctions pour faire les statistiques descriptives ------------ 

def q1(x):
    """
    calcule le 1er quartile (25%)
    """
    return x.quantile(0.25)

def q3(x):
    """
    calcule le 3ème quartile (75%)
    """
    return x.quantile(0.75)

def decrire_donnees(df, categorie, col):
    """
    Génère un tableau décrivant les données avec l'effectif, Q1, la médiane, Q3 et la moyenne
    pour une colonne donnée, groupée selon une catégorie.

    df (data frame): dataframe
    categorie (str) : colonne catégorielle
    col (str) : colonne numérique à analyser

    return un tableau formaté et trié 
    """

    #Création du tableau
    tableau = df.groupby(categorie)[col].agg(
        nombre="count",
        Q1=q1,
        médiane="median",
        Q3=q3,
        moyenne="mean"
    )

    #Tri selon la médiane
    tableau = tableau.sort_values("médiane")

    #Arrondi
    return tableau.round(1)

# --------- Fonctions pour faire les régressions ------------


def regression(data, x_col, y_col):
    """
    Effectue une régression simple par la méthode des moindres carrés ordinaires et affiche 
    les coefficients obtenus, le r2 et les p-valeurs
    data (df) = les données sur lesquelles on fait la régression
    x_col (str) = la variable sur laquelle on fait la régression
    y_col (str)= la variable qu'on cherche à expliquer par la régression
    """
    data = sm.add_constant(data)
    X = data[['const', x_col]]
    Y = data[y_col]
    model = sm.OLS(Y, X, missing='drop')
    results = model.fit()
    coeffs = results.params
    std = results.bse
    p = results.pvalues
    print("Les coefficients de la régression sont :")
    print(f"constante : {coeffs.iloc[0]:.3f} +/- {std.iloc[0]:.3f}")
    print(f"{x_col} : {coeffs.iloc[1]:.3f} +/- {std.iloc[1]:.3f}")
    print(f"Le R^2 obtenu est {results.rsquared:.3f}.")
    print("Les p-valeurs sont :")
    print(f"constante : {p.iloc[0]:.10f}")
    print(f"{x_col} : {p.iloc[0]:.10f}")


def visualisation_reg(data, x_col, y_col):
    """
    Effectue une régression simple par la méthode des moindres carrés ordinaires et
    affiche le graphique correspondant
    data (df) = les données sur lesquelles on fait la régression
    x_col (str) = la variable sur laquelle on fait la régression
    y_col (str)= la variable qu'on cherche à expliquer par la régression
    """
    import matplotlib.pyplot as plt
    data = sm.add_constant(data)
    X = data[['const', x_col]]
    Y = data[y_col]
    model = sm.OLS(Y, X, missing='drop')
    results = model.fit()
    coeffs = results.params
    X_reg = data[x_col]
    Y_reg = coeffs.iloc[0] + coeffs.iloc[1] * X_reg
    plt.figure(figsize=(12, 10))
    plt.plot(X_reg, Y, 'o')
    plt.plot(X_reg, Y_reg, '-')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"Régression simple de {y_col} sur {x_col}")
    plt.show()

#C'est la fonction pour générer les cartes, j'ai dû la modifier pour respecter le critère de dominante, je sais pas si elle marche telle quelle
#Donc je vais la remodifier si elle marche pas
def Gender_card(df):
    df = df.dropna(subset=["coord_GPS"])
    df[['lat', 'lon']] = df["coord_GPS"].str.split(',', expand=True).astype(float)
    df_metro = df[(df['lon'] > -5.5) & (df['lon'] < 10) & (df['lat'] > 41) & (df['lat'] < 51.5)]
    geometry = [Point(xy) for xy in zip(df_metro['lon'], df_metro['lat'])]
    gdf = gpd.GeoDataFrame(df_metro, geometry=geometry, crs="EPSG:4326")
    df_metro = df[(df['lon'] > -5.5) & (df['lon'] < 10) & (df['lat'] > 41) & (df['lat'] < 51.5)]
    geometry = [Point(xy) for xy in zip(df_metro['lon'], df_metro['lat'])]
    gdf = gpd.GeoDataFrame(df_metro, geometry=geometry, crs="EPSG:4326")
    fig, ax = plt.subplots(figsize=(14, 14))
    try:
        path = geodatasets.get_path("naturalearth.lowres")
        world = gpd.read_file(path)
        france = world[world.name == "France"]
        france.plot(ax=ax, color='#f4f4f4', edgecolor='black', linewidth=1, zorder=1)
    except:
        print("Fond de carte non disponible, affichage des points uniquement.")
    colors = {'Dominante féminine': "#E6D410", 'Dominante masculine': "#5FE909",'Mixte': "#6B449C"} 
    for ctype, data in gdf.groupby('categorie_genre'):
        color = colors.get(ctype, 'grey')
        label = f"categorie_genre {ctype}"
        data.plot(ax=ax, markersize=5, color=color, alpha=0.6,label=label,zorder=2)
    plt.title("Répartition des formations selon la dominante de genre (Parcoursup 2024)", fontsize=16)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend(title="Répartition", loc='upper right', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.savefig('carte_parcoursup_genre.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("Carte générée : carte_parcoursup_genre.png")

#La fonction pour les cartes par filière, pareil, j'ai adapté aux modifs de cariables, mais pas sûr que ça marche 
def Gender_card_by_way(df):
    df = df.dropna(subset=["coord_GPS"])
    df[['lat', 'lon']] = df["coord_GPS"].str.split(',', expand=True).astype(float)
    df_metro = df[(df['lon'] > -5.5) & (df['lon'] < 10) & (df['lat'] > 41) & (df['lat'] < 51.5)]
    geometry = [Point(xy) for xy in zip(df_metro['lon'], df_metro['lat'])]
    gdf = gpd.GeoDataFrame(df_metro, geometry=geometry, crs="EPSG:4326")
    df_metro = df[(df['lon'] > -5.5) & (df['lon'] < 10) & (df['lat'] > 41) & (df['lat'] < 51.5)]
    geometry = [Point(xy) for xy in zip(df_metro['lon'], df_metro['lat'])]
    gdf = gpd.GeoDataFrame(df_metro, geometry=geometry, crs="EPSG:4326")
    fig, ax = plt.subplots(figsize=(14, 14))
    try:
        path = geodatasets.get_path("naturalearth.lowres")
        world = gpd.read_file(path)
        france = world[world.name == "France"]
        france.plot(ax=ax, color='#f4f4f4', edgecolor='black', linewidth=1, zorder=1)
        has_map = True
    except:
        print("Fond de carte non disponible, affichage des points uniquement.")
        has_map = False
    filieres = df['filiere_agr'].dropna().unique()
    for filiere in filieres:
        df_filiere = df[df['filiere_agr'] == filiere].copy()
        df_metro = df_filiere[(df_filiere['lon'] > -5.5) & (df_filiere['lon'] < 10) & (df_filiere['lat'] > 41) & (df_filiere['lat'] < 51.5)]
        if df_metro.empty:
            print(f" -> Pas de données en métropole pour {filiere}, on passe.")
            continue
        geometry = [Point(xy) for xy in zip(df_metro['lon'], df_metro['lat'])]
        gdf = gpd.GeoDataFrame(df_metro, geometry=geometry, crs="EPSG:4326")
        fig, ax = plt.subplots(figsize=(12, 12))
        if has_map:
            france.plot(ax=ax, color='#f4f4f4', edgecolor='black', linewidth=1, zorder=1)
        colors = {'Dominante féminine': "#E6D410", 'Dominante masculine': "#5FE909",'Mixte': "#6B449C"} 
        for ctype, data in gdf.groupby('Dominante'):
            color = colors.get(ctype, 'grey')
            data.plot(ax=ax, 
                  markersize=15, 
                  color=color, 
                  alpha=0.7, 
                  label=f"Majorité {ctype}",
                  zorder=2)
        plt.title(f"Répartition par genre - Filière : {filiere}", fontsize=15)
        plt.legend(loc='upper right')
        plt.axis('off') 
        safe_name = re.sub(r'[^\w\-_\. ]', '_', str(filiere))
        filename = f"carte_genre_{safe_name}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.show()
        plt.close() 
    
