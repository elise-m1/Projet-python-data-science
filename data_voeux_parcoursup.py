# stats descriptives sur la base de données "Parcoursup 2024
# - vœux de poursuite d'études et de réorientation dans
#  l'enseignement supérieur et réponses des établissements"

import pandas as pd

url_parcoursup2024 = "https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-parcoursup/exports/csv?use_labels=true"
parcoursup2024 = pd.read_csv(url_parcoursup2024,sep=";")
# print(parcoursup2024.columns)

# on supprime les colonnes dont on a pas besoin
parcoursup2024 = parcoursup2024.drop(columns=['Lien de la formation sur la plateforme Parcoursup'])

# stats descriptives
print(f"Il y a {parcoursup2024['Filière de formation détaillée'].count()} formations proposées sur parcoursup en 2024.")
print(f"{parcoursup2024.loc[parcoursup2024['Sélectivité'] =="formation sélective"]['Filière de formation détaillée'].count()} d'entre elles sont sélectives.")

parcoursup2024["pourcentage admis de la même académie"] = parcoursup2024["Dont effectif des admis issus de la même académie"]/parcoursup2024["Effectif total des candidats ayant accepté la proposition de l’établissement (admis)"]
print(f"En moyenne, {parcoursup2024["pourcentage admis de la même académie"].mean()}% des admis proviennent de la même académie.")
# pb avec le chiffre, 0.51% c'est pas crédible  