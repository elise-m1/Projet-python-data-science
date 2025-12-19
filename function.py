# Il s'agit du fichier dans lequel nous pouvons écrire toutes nos fonctions que nous appelerons dans le notebook

#Importation des librairies qui vont nous servir
import numpy as np
import pandas as pd

def simplification_statut(val):
    """
    Transforme le statut détaillé en Privé/Public/Autre
    """

    statut = str(val).lower() #robustesse
    if public in statut :
        return "Public"
    elif privé in statut :
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
        "Dont effectif des admis néo bacheliers avec mention Très Bien avec félicitations au bac" : "nb_admis_felicitations"
        }

    return df.rename(columns=dict_noms)

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

    if "part_fille" in df.columns : 
        df["categorie_genre"] = pd.cut(
            df["part_fille"],
            bins=[-1, 40, 60, 101],
            labels=["Dominante masculine", "Mixte", "Dominante féminine"]
        )

    if {"nb_admis_tres_bien", "nb_admis_felicitation", "nb_admis_bac"}.issubset(df.columns):
        df["tb_eleves"] = ((df["nb_admis_tres_bien"].fillna(0) + df["nb_admis_felicitation"].fillna(0))/ df["nb_admis_bac"])*100

