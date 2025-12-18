import pandas as pd
import numpy as np
# from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import matplotlib.pyplot as plt

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
                        'Dont effectif des candidates admises',
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

# Création de la variable qu'on cherche à expliquer, la part d'entrants issus d'une autre académie 

parcoursup2024["nb_entrants"] = parcoursup2024["nb_admis"] - parcoursup2024["nb_admis_ac"]
parcoursup2024["part_entrants"] = parcoursup2024["nb_entrants"] / parcoursup2024["nb_admis"]*100

#parcoursup2024.dropna()
Y = parcoursup2024[["part_entrants"]]


parcoursup2024 = sm.add_constant(parcoursup2024) #ajout d'une colonne constante pour faire les regressions


# ---------- Sélectivité -----------------------

# on crée une variable indicatrice de la sélectivité
parcoursup2024["selec_b"] = 0
parcoursup2024.loc[parcoursup2024["selec"] == "formation sélective","selec_b"] = 1

"""
reg = LinearRegression()
X = parcoursup2024[["constante","selec_b"]]
Y = parcoursup2024[["part_bac_ac"]]
model = reg.fit(X,Y)
coeffs = model.coef_ #[[0.         0.30819445]]
R2 = model.score(X,Y) #1.9197839825957352e-05
"""
# sklearn ne calcule pas les p-values, donc on va utiliser autrechose


#X = parcoursup2024["selec_b"]
#X = sm.add_constant(X)

X = parcoursup2024[['const', "selec_b"]]


model = sm.OLS(Y, X, missing='drop')
results = model.fit()
results.params
# const      54.063682
# selec_b    -7.778608 -> être une formation sélective diminue le nb d'entrants issus d'une autre
#                         académie 
# dtype: float64
results.rsquared
# 0.015332468741064864
results.pvalues
# const      0.000000e+00
# selec_b    1.142956e-48 -> coefficient significatif à 1%
# dtype: float64

# ----------------- Paris ----------------
# on teste si le fait que la formation soit à Paris joue un rôle
parcoursup2024["paris"] = 0
parcoursup2024.loc[parcoursup2024["academie"] == "Paris","paris"] = 1

X = parcoursup2024[['const', "paris"]]

model = sm.OLS(Y, X, missing='drop')
results = model.fit()
results.params
# const    45.381442
# paris    37.569449 -> être dans paris augmente bcp le nb d'entrants issus d'une autre académie
# dtype: float64
results.rsquared
# 0.13448989797577926
results.pvalues
# const    0.0
# paris    0.0 -> coefficient significatif à 1%
# dtype: float64