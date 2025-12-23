# on fait ici la régression du taux d'entrants sur la population 
# du département

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import requests


# -------- importation et nettoyage de la base de données principales ------------------
url_parcoursup2024 = "https://www.data.gouv.fr/api/1/datasets/r/1d916b7c-bd4c-4951-845a-70f7ad7c17db"
parcoursup2024 = pd.read_csv(url_parcoursup2024, sep=";")

def drop_parcoursup(df): # suppprime les colonnes dont on a pas besoin
    df = df.drop(columns=["Session",
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
                        "Dont effectif des admis ayant reçu leur proposition d’admission à l'ouverture de la procédure principale",
                        "Dont effectif des admis ayant reçu leur proposition d’admission avant le baccalauréat",
                        "Dont effectif des admis ayant reçu leur proposition d’admission avant la fin de la procédure principale",
                        "Dont effectif des admis en internat",
                        "Dont effectif des admis boursiers néo bacheliers",
                        "Effectif des admis néo bacheliers technologiques",
                        "Effectif des admis néo bacheliers professionnels",
                        "Effectif des autres candidats admis",
                        "Dont effectif des admis néo bacheliers sans information sur la mention au bac",
                        "Dont effectif des admis néo bacheliers sans mention au bac",
                        "Dont effectif des admis néo bacheliers avec mention Assez Bien au bac",
                        "Dont effectif des admis néo bacheliers avec mention Bien au bac",
                        "Dont effectif des admis néo bacheliers avec mention Très Bien au bac",
                        "Dont effectif des admis néo bacheliers avec mention Très Bien avec félicitations au bac",
                        "Effectif des admis néo bacheliers généraux ayant eu une mention au bac",
                        "Effectif des admis néo bacheliers technologiques ayant eu une mention au bac",
                        "Effectif des admis néo bacheliers professionnels ayant eu une mention au bac",
                        "Dont effectif des admis issus du même établissement (BTS/CPGE)",
                        "Dont effectif des admises issues du même établissement (BTS/CPGE)",
                        "% d’admis ayant reçu leur proposition d’admission à l'ouverture de la procédure principale",
                        "% d’admis ayant reçu leur proposition d’admission avant le baccalauréat",
                        "% d’admis ayant reçu leur proposition d’admission avant la fin de la procédure principale",
                        "% d’admis dont filles",
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
                        "Taux d’accès",
                        "Part des terminales générales qui étaient en position de recevoir une proposition en phase principale",
                        "Part des terminales technologiques qui étaient en position de recevoir une proposition en phase principale",
                        "Part des terminales professionnelles qui étaient en position de recevoir une proposition en phase principale",
                        "etablissement_id_paysage",
                        "composante_id_paysage"])
    return df


def rename_parcoursup(df): # renomme les colonnes qu'on garde pour faciliter l'analyse
    df = df.rename(columns={"Statut de l’établissement de la filière de formation (public, privé…)": "statut",
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
                            'Dont effectif des candidates admises':"nb_admis_f",
                            "Dont effectif des admis issus de la même académie":"nb_admis_ac",
                            "Dont effectif des admis issus de la même académie (Paris/Créteil/Versailles réunies)":"nb_admis_ac_pcv",
                            "% d’admis néo bacheliers issus de la même académie":"part_bac_ac",
                            "% d’admis néo bacheliers issus de la même académie (Paris/Créteil/Versailles réunies)":"part_bac_ac_pcv",
                            "% d’admis néo bacheliers généraux":"part_bacg",
                            "list_com":"appel", #appel commun à plusieurs formations ou propre à cette formation
                            "tri":"type_etablissement", #lycee, univ ou autre
                            "cod_aff_form":"code_form"})
    return df

parcoursup2024 = drop_parcoursup(parcoursup2024)
parcoursup2024 = rename_parcoursup(parcoursup2024)

# pour la Corse, code_dep est vide donc on fixe une valeur :
parcoursup2024.loc[parcoursup2024["dep"] == "Haute-Corse", "code_dep"] = 100
parcoursup2024.loc[parcoursup2024["dep"] == "Corse-du-Sud", "code_dep"] = 101


# Création de la variable qu'on cherche à expliquer, la part d'entrants issus d'une autre académie 

parcoursup2024["nb_entrants"] = parcoursup2024["nb_admis"] - parcoursup2024["nb_admis_ac"]
parcoursup2024["part_entrants"] = parcoursup2024["nb_entrants"] / parcoursup2024["nb_admis"]*100
parcoursup2024.loc[parcoursup2024["nb_admis"] == 0, "part_entrants"] = 0 # pour les formations avec aucun admis
                                                                         # on fixe arbitrairement le taux d'entrants à 0
                                                                         # pour éviter d'avoir des NaN
# rq = on peut aussi choisir de supprimer complétement ces formations, à voir
Y = parcoursup2024[["part_entrants"]]


parcoursup2024 = sm.add_constant(parcoursup2024) #ajout d'une colonne constante pour faire les regressions

# Regroupement des académies de Paris, Créteil et Versailles
parcoursup2024["academie_pcv"] = parcoursup2024["academie"]
parcoursup2024["academie_pcv"] = parcoursup2024["academie"].replace(
    ["Paris", "Créteil", "Versailles"], "Paris-Créteil-Versailles")

# Création d'un autre Y correspondant à ce nouveau taux d'entrants
parcoursup2024["nb_entrants_pcv"] = parcoursup2024["nb_admis"] - parcoursup2024["nb_admis_ac_pcv"]
parcoursup2024["part_entrants_pcv"] = parcoursup2024["nb_entrants_pcv"] / parcoursup2024["nb_admis"]*100
parcoursup2024.loc[parcoursup2024["nb_admis"] == 0, "part_entrants_pcv"] = 0 # pour les formations avec aucun admis
                                                                         # on fixe arbitrairement le taux d'entrants à 0
                                                                         # pour éviter d'avoir des NaN
# rq = on peut aussi choisir de supprimer complétement ces formations, à voir
Y_pcv = parcoursup2024[["part_entrants_pcv"]]


# ------- Importation et nettoyage de la base de données de population par département ---------

url_pop_dep = "https://api.insee.fr/melodi/data/DS_ESTIMATION_POPULATION?TIME_PERIOD=2024&SEX=_T&AGE=_T&EP_MEASURE=POP&GEO=DEP"
req_api = requests.get(url_pop_dep).json()
clean_req = req_api.get('observations') # on obtient une liste de dictionnaire
                                        # un dictionnaire = une observation

# j'ai pas trouvé de manière rapide qui fonctionne pour transformer en dataframe donc 
# on va le faire en force brute
Geo = []
Annee = []
Pop = []
for d in clean_req :
    Geo.append(d['dimensions']['GEO'])
    Annee.append(d['dimensions']['TIME_PERIOD'])
    Pop.append(d['measures']['OBS_VALUE_NIVEAU']['value'])

Geo = pd.Series(Geo)
Annee = pd.Series(Annee)
Pop = pd.Series(Pop)
pop_dep = pd.DataFrame(zip(Geo, Annee, Pop), columns=['Niveau géographique', 'Année', 'Population'])

# fonction pour convertir 'Niveau géographique' en le numéro du département
def conversion(chaine):
    n = len(chaine)
    if n == 12: #départements d'outre-mer
        return float(chaine[n-3:n])
    elif chaine[n-2:n] == "2A": #haute-corse
        return 100.0
    elif chaine[n-2:n] == "2B": #corse du sud
        return 101.0
    else:
        return float(chaine[n-2:n])


pop_dep['Département'] = pop_dep['Niveau géographique'].apply(conversion)

# ----------------- Merge des deux bases ---------------------------

parcoursup2024 = parcoursup2024.merge(pop_dep,
                                      left_on="code_dep", right_on="Département", how='left')


# ------------------- Régression ---------------------------------------

# Avec Y
X = parcoursup2024[['const', "Population"]]
model = sm.OLS(Y, X, missing='drop')
results = model.fit()
print("paris, créteil et versailles séparées")
results.params
# const         38.474381
# Population     0.000008
# dtype: float64
results.rsquared
# 0.037787996801807666
results.pvalues
# const          0.000000e+00
# Population    3.851574e-119
# dtype: float64

# Avec Y_pcv
X = parcoursup2024[['const', "Population"]]
model = sm.OLS(Y_pcv, X, missing='drop')
results = model.fit()
print("paris, créteil et versailles regroupées")
results.params
# const         41.903216
# Population     0.000001
# dtype: float64
results.rsquared
# 0.0012754667968392086
results.pvalues
# const         0.000000
# Population    0.000024
# dtype: float64