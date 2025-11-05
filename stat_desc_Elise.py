import pandas as pd

# Importation du dataset
url = "https://www.data.gouv.fr/api/1/datasets/r/93ae799e-520d-412a-9b4a-29a979318aa3"
data = pd.read_csv(url, sep=';')

data.head()
data.info()

# 0   Année du Baccalauréat                                                           17420 non-null  int64  
# 1   Enseignements de spécialité                                                     17420 non-null  object 
# 2   Formation                                                                       17420 non-null  object 
# 3   Nombre de candidats bacheliers ayant confirmé au moins un vœu                   17420 non-null  int64  
# 4   Nombre de candidats bacheliers ayant reçu au moins une proposition d'admission  17420 non-null  float64
# 5   Nombre de candidats bacheliers ayant accepté une proposition d'admission        17420 non-null  int64 

data.isna().sum() #Aucune valeur manquante

# On renomme les colonnes pour rendre leur analyse plus facile
data = data.rename(columns={
    "Année du Baccalauréat":"Annee_bac",
    "Enseignements de spécialité":"Specialite",
    "Formation":"Formation",
    "Nombre de candidats bacheliers ayant confirmé au moins un vœu":"Nb_candidats",
    "Nombre de candidats bacheliers ayant reçu au moins une proposition d'admission":"Nb_proposition",
    "Nombre de candidats bacheliers ayant accepté une proposition d'admission":"Nb_acceptation"
})
#On renomme aussi les spécialités car le nom est trop long

data["Specialite"].unique()[:30]

remplacements = {
    r"[Mm]ath[ée]matiques": "Maths",
    r"[Pp]hysique[- ]?[Cc]himie": "PC",
    r"[Nn]um[ée]rique.*[Ii]nformatiques": "NSI",
    r"[Ss]ciences[ ]?[Ee]conomiques.*[Ss]ociales": "SES",
    r"[Ss]ciences de la vie.*[Tt]erre": "SVT",
    r"[Hh]istoire.*[Pp]olitiques": "HGGSP",
    r"[Hh]umanit[ée]s.*[Pp]hilosophie": "HLP",
    r"[Ll]angues.*[Rr][ée]gionales": "LLCER",
    r"[Aa]rt": "Art",
    r"[Bb]iologie.?[Ee]cologie": "B/E",
    r"[Ss]ciences de l'ing[ée]nieur": "SI",
    r"[ÉE]ducation.*[Ss]portives": "EPS",
    r"[Ll]itt[ée]rature.*[Aa]ntiquit[ée]": "LLCA"
}

data["Specialite"] = data["Specialite"].replace(remplacements, regex=True)
data["Specialite"].unique()[:20]
#Cela ne m'affiche pas ce que je veux, les spécialités sont encore entières.

data["Specialite"].head()
#ça marche pas :(


#Statistiques générales
data["Annee_bac"].describe()
# count    17420.000000
# mean      2022.589552
# std          1.117817
# min       2021.000000
# 25%       2022.000000
# 50%       2023.000000
# 75%       2024.000000
# max       2024.000000

data["Nb_proposition"].describe()
# count    17420.000000
# mean       309.952124
# std       2125.829872
# min          0.000000
# 25%          0.000000
# 50%          4.000000
# 75%         40.000000
# max      81107.000000

data["Nb_candidats"].describe()
# count    17420.000000
# mean       514.460505
# std       2812.364045
# min          0.000000
# 25%          1.000000
# 50%          9.000000
# 75%        100.000000
# max      83495.000000

data["Nb_acceptation"].describe()
# count    17420.000000
# mean       151.926406
# std       1665.951039
# min          0.000000
# 25%          0.000000
# 50%          1.000000
# 75%         13.000000
# max      75485.000000

pd.set_option('display.max_rows', None)
data["Specialite"].unique()

# Ratios => taux de proposition et d'acceptation 
data["Taux_proposition"] = data["Nb_proposition"]/data["Nb_candidats"]
data["Taux_proposition"].describe()
# count    13326.000000
# mean         0.464701
# std          0.297230
# min          0.000000
# 25%          0.241437
# 50%          0.483871
# 75%          0.675830
# max          1.000000

data["Taux_acceptation"] = data["Nb_acceptation"]/data["Nb_proposition"]
data["Taux_acceptation"].describe()
# count    11672.000000
# mean         0.334187
# std          0.272209
# min          0.000000
# 25%          0.142857
# 50%          0.289876
# 75%          0.484415
# max          1.000000

#Statistiques par spécialités
data.groupby("Specialite")[["Taux_proposition"]].mean().sort_values("Taux_proposition", ascending=False)
#                                                    Taux_proposition
# Specialite                                                          
# Littérature et langues et cultures de l'Antiqui...          0.807692
# Littérature et langues et cultures de l'Antiqui...          0.640345
# Biologie/Ecologie,Langues, littératures et cult...          0.587793
# Mathématiques Spécialité,Physique-Chimie Spécia...          0.576480
# Littérature et langues et cultures de l'Antiqui...          0.562835

data.groupby("Specialite")[["Taux_acceptation"]].mean().sort_values("Taux_acceptation", ascending=False)
#                                                    Taux_acceptation
# Specialite                                                          
# Biologie/Ecologie,Sciences de la vie et de la T...          1.000000
# Biologie/Ecologie,Numérique et Sciences Informa...          0.681818
# Art,Art                                                     0.666667
# Art,Biologie/Ecologie                                       0.666667
# Littérature et langues et cultures de l'Antiqui...          0.666667

Statistiques par années
data.groupby("Annee_bac")[["Taux_proposition"]].mean()
#           Taux_proposition
# Annee_bac                  
# 2021               0.435838
# 2022               0.551975
# 2023               0.429844
# 2024               0.449483

data.groupby("Annee_bac")[["Taux_acceptation"]].mean()
#2021               0.360685
#2022               0.340489
#2023               0.327487
# 2024               0.311768

data.groupby(["Annee_bac","Specialite"])[["Nb_candidats", "Nb_proposition", "Nb_acceptation"]].sum() 
#                                                              Nb_candidats  Nb_proposition  Nb_acceptation
#Annee_bac Specialite                                                                                      
#2021      Art,Art                                                        9             3.0               2
#          Art,Histoire-Géographie, Géopolitique et Scienc...         14631          8200.0            4498
#          Art,Humanités, Littérature et Philosophie                  16676          9757.0            5174
#          Art,Langues, littératures et cultures étrangère...         28932         16927.0            9230
#          Art,Mathématiques Spécialité                                8004          4404.0            2264
#          Art,Numérique et Sciences Informatiques                     1899           923.0             484