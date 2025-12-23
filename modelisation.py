import pandas as pd
import numpy as np
# from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Remarques générales sur la modélisation :
#  - on fait des régressions linéaires, c'est des sciences sociales donc les R^2 sont
#    pas ouf, c'est pas très grave, ce qui compte c'est que les coefficients soient significatifs
#  - c'est des régressions non causales, on montre juste une corrélation, je pense pas qu'avec nos 
#    données on ait de quoi montrer une causalité




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

# ---------- Sélectivité -----------------------

# on crée une variable indicatrice de la sélectivité
parcoursup2024["selec_b"] = 0
parcoursup2024.loc[parcoursup2024["selec"] == "formation sélective", "selec_b"] = 1

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

# Avec Y_pcv

X = parcoursup2024[['const', "selec_b"]]
model = sm.OLS(Y_pcv, X, missing='drop')
results = model.fit()
# print("Sélectivité")
results.params
# const      48.669630
# selec_b    -6.813565
# dtype: float64
results.rsquared
# 0.012708295496910549
results.pvalues
# const      0.000000e+00
# selec_b    4.762516e-41 -> coefficient significatif à 1%
# dtype: float64

# ----------------- Formation privée ou non ---------------------------------------

parcoursup2024["privé"] = 0
parcoursup2024.loc[parcoursup2024["statut"] == "Privé enseignement supérieur", "privé"] = 1
parcoursup2024.loc[parcoursup2024["statut"] == "Privé hors contrat", "privé"] = 1
parcoursup2024.loc[parcoursup2024["statut"] == "Privé sous contrat d'association", "privé"] = 1

X = parcoursup2024[['const', "privé"]]

model = sm.OLS(Y, X, missing='drop')
results = model.fit()
results.params
# const    46.997787
# privé     2.297553
# dtype: float64
results.rsquared
# 0.0012539818315291384
results.pvalues
# const    0.000000
# privé    0.000026
# dtype: float64

# Avec Y_pcv

X = parcoursup2024[['const', "privé"]]
model = sm.OLS(Y_pcv, X, missing='drop')
results = model.fit()
#print("Privé ou public")
results.params
# const    42.960289
# privé     2.030672
# dtype: float64
results.rsquared
# 0.0010912869317789564
results.pvalues
# const    0.000000
# privé    0.000088
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


# ----------------- Lille ----------------
# on teste si le fait que la formation soit à Lille joue un rôle
# c'est juste pour vérifier que c'est pas significatif, je pense pas que ce soit pertinent de
# le mettre dans le notebook
parcoursup2024["lille"] = 0
parcoursup2024.loc[parcoursup2024["academie"] == "Lille","lille"] = 1

X = parcoursup2024[['const', "lille"]]

model = sm.OLS(Y, X, missing='drop')
results = model.fit()
results.params
# const    48.441591
# lille    -5.587874
# dtype: float64
results.rsquared
# 0.0028806639776992604
results.pvalues
# const    0.000000e+00
# lille    2.373457e-10
# dtype: float64

# ---------- Part de femmes dans la formation ---------------

# on régresse sur la part de femmes admises, idéalement faudrait le faire sur la part
# de l'année précedente car c'est l'information que les étudiants avaient au moment de
# faire leur choix
# rq : en fait c'est pas si grave, ça serait un pb si on voulait faire une regression causale
# mais c'est pas le cas donc ça va

parcoursup2024["part_femmes"] = parcoursup2024["nb_admis_f"] / parcoursup2024["nb_admis"]

X = parcoursup2024[['const', "part_femmes"]]

model = sm.OLS(Y, X, missing='drop')
results = model.fit()
results.params
# const          37.425020
# part_femmes    21.003344 -> plus il y a de femmes, plus il y a d'entrants issus d'une autre
#                             académie => les femmes partent plus loin pour leurs études ???
# dtype: float64
results.rsquared
# 0.05423288919040925
results.pvalues
# const           0.000000e+00
# part_femmes    1.041141e-170 -> coefficient significatif à 1%
# dtype: float64


# Avec Y_pcv

X = parcoursup2024[['const', "part_femmes"]]
model = sm.OLS(Y_pcv, X, missing='drop')
results = model.fit()
# print("part de femmes")
results.params
# const          34.404845
# part_femmes    18.783875
# dtype: float64
results.rsquared
# 0.048192042392423584
results.pvalues
# const           0.000000e+00
# part_femmes    1.893585e-151
# dtype: float64

# -------- Régression sur plusieurs variables ----------


X = parcoursup2024[['const', "selec_b", "part_femmes", "paris", "lille"]]

model = sm.OLS(Y, X, missing='drop')
results = model.fit()
results.params
# const          40.568450
# selec_b        -3.938353
# part_femmes    16.189131
# paris          35.023012
# lille          -2.322822
# dtype: float64
results.rsquared
# 0.17613669670997978
results.pvalues
# const           0.000000e+00
# selec_b         2.810674e-15
# part_femmes    1.908268e-110
# paris           0.000000e+00
# lille           3.856399e-03
# dtype: float64

# ---------- Régression sur le nb d'admis ----------------------------


X = parcoursup2024[['const', "nb_admis"]]

model = sm.OLS(Y, X, missing='drop')
results = model.fit()
results.params
# const       47.765668
# nb_admis     0.006246  # coeff très faible, effet pas très important
# dtype: float64
results.rsquared
# 0.0003272245125022222
results.pvalues
# const       0.000000
# nb_admis    0.032862  -> coefficient significatif à 5% 
# dtype: float64

# Avec Y_pcv

X = parcoursup2024[['const', "nb_admis"]]

model = sm.OLS(Y_pcv, X, missing='drop')
results = model.fit()
results.params
# const       43.489069
# nb_admis    -0.001954
# dtype: float64
results.rsquared
# 3.4498013420480866e-05
results.pvalues
# const       0.000000
# nb_admis    0.485888 -> coefficient non significatif
# dtype: float64


# ---------- Régression sur le log du nb d'admis ----------------------------


parcoursup2024["log_admis"] = parcoursup2024["nb_admis"].apply(np.log)
# on se débarrasse des formations avec 0 admis
parcoursup2024.loc[parcoursup2024["nb_admis"] == 0, "log_admis"] = np.nan 
X = parcoursup2024[['const', "log_admis"]]

model = sm.OLS(Y, X, missing='drop')
results = model.fit()

print("paris, créteil et versailles séparées")
print(results.params)
# const        48.481451
# log_admis    -0.129970
# dtype: float64
print(results.rsquared)
# 2.6166065853039377e-05
print(results.pvalues)
# const        0.000000
# log_admis    0.546285 -> coefficient pas significatif
# dtype: float64


# Avec Y_pcv

X = parcoursup2024[['const', "log_admis"]]

model = sm.OLS(Y_pcv, X, missing='drop')
results = model.fit()

print("paris, créteil et versailles regroupées")
print(results.params)
# const        48.219445
# log_admis    -1.319296
# dtype: float64
print(results.rsquared)
# 0.0029954300783467946
print(results.pvalues)
# const        0.000000e+00
# log_admis    1.046033e-10 -> coefficient significatif à 1 %
# dtype: float64


# ---------- def d'une fonction pour faire les régressions afin de simplifier le code ------


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
    print(f"constante : {coeffs[0]:.3f} +/- {std[0]:.3f}")
    print(f"{x_col} : {coeffs[1]:.3f} +/- {std[1]:.3f}")
    print(f"Le R^2 obtenu est {results.rsquared:.3f}.")
    print("Les p-valeurs sont :")
    print(f"constante : {p[0]:.3f}")
    print(f"{x_col} : {p[0]:.3f}")

def visualisation_reg(data, x_col, y_col):
    """
    Effectue une régression simple par la méthode des moindres carrés ordinaires et
    affiche le graphique correspondant
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
    X_reg = data[x_col]
    Y_reg = coeffs[0] + coeffs[1] * X_reg
    plt.figure(figsize=(12, 10))
    plt.plot(X_reg, Y, 'o')
    plt.plot(X_reg, Y_reg, '-')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"Régression simple de {y_col} sur {x_col}")
    plt.show()
