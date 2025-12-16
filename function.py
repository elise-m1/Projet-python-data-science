# Il s'agit du fichier dans lequel nous pouvons écrire toutes nos fonctions que nous appelerons dans le notebook

#Importation des librairies qui vont nous servir
import numpy as np
import pandas as pd

def simplification_statut(val):
    """Transforme le statut détaillé en Privé/Public/Autre"""
    statut = str(val).lower() #robustesse
    if public in statut :
        return "Public"
    elif privé in statut :
        return "Privé"
    else :
        return "Autre"