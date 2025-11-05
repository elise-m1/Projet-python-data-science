# stats descriptives sur la base de données "Parcoursup 2024
# - vœux de poursuite d'études et de réorientation dans
#  l'enseignement supérieur et réponses des établissements"

import pandas as pd

url_parcoursup2024 = "https://www.data.gouv.fr/api/1/datasets/r/1d916b7c-bd4c-4951-845a-70f7ad7c17db"
parcoursup2024 = pd.read_csv(url_parcoursup2024 , sep=";")




# on supprime les colonnes dont on a pas besoin
# à modifier éventuellement par la suite
parcoursup2024 = parcoursup2024.drop(columns=["Session",
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


# on renomme les colonnes pour rendre leur analyse plus facile
parcoursup2024 = parcoursup2024.rename(columns={"Statut de l’établissement de la filière de formation (public, privé…)": "statut",
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


# ----------------Statistiques générales-------------------------

# nb de formations
parcoursup2024["filiere_det"].count()
# 14079

# nb de formations sélectives
parcoursup2024.loc[parcoursup2024["selec"] == "formation sélective"]["filiere_det"].count()
# 10891

# nb d'admis
parcoursup2024["nb_admis"].describe()
# count    14079.000000
# mean        46.135876
# std         76.027243
# min          0.000000
# 25%         14.000000
# 50%         25.000000
# 75%         46.000000
# max       1482.000000

# nb d'admis de la même académie
parcoursup2024["nb_admis_ac"].describe()
# count    14079.000000
# mean        23.604801
# std         44.947603
# min          0.000000
# 25%          5.000000
# 50%         13.000000
# 75%         24.000000
# max       1083.000000

#nb d'admis de la même académie en regroupant Paris, Créteil et Versailles
parcoursup2024["nb_admis_ac_pcv"].describe()
# count    14079.000000
# mean        26.226366
# std         49.873991
# min          0.000000
# 25%          6.000000
# 50%         14.000000
# 75%         27.000000
# max       1083.000000

# % d'admis de la même académie
parcoursup2024["part_bac_ac"].describe()
# count    14079.000000
# mean        67.397756
# std         29.439829
# min          0.000000
# 25%         50.000000
# 50%         75.000000
# 75%         92.000000
# max        100.000000

# % d'admis de la même académie en regroupant Paris, Créteil et Versailles
parcoursup2024["part_bac_ac_pcv"].describe()
# count    14079.000000
# mean        73.134314
# std         26.792194
# min          0.000000
# 25%         60.000000
# 50%         81.000000
# 75%         94.000000
# max        100.000000

"""
#pour les années prédédentes, des fois qu'on on en ait besoin
url_parcoursup2023 = "https://www.data.gouv.fr/api/1/datasets/r/6f622444-6596-424c-bca2-3e2fa763579e"
parcoursup2023 = pd.read_csv(url_parcoursup2023, sep =";")

url_parcoursup2022 = "https://www.data.gouv.fr/api/1/datasets/r/1401805b-7996-46d4-8770-8ecc424668f1"
parcoursup2022 = pd.read_csv(url_parcoursup2022, sep =";")

url_parcoursup2021 = "https://www.data.gouv.fr/api/1/datasets/r/52c41cd5-ce79-4052-8a07-bae0ecf0f36b"
parcoursup2021 = pd.read_csv(url_parcoursup2021, sep =";")
"""