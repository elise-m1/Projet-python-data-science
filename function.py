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

    colonnes_sup = [
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