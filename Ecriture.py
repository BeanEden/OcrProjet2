import time

import requests
from bs4 import BeautifulSoup as bs
import csv
import shutil
import os
import genericpath
from fonctions_extraction_categories import *
from fonctions_extraction_livres import *
from Construction import *


def chemin_acces():
    cwd = os.getcwd()
    cwd_data = cwd + "/data/"
    return cwd_data


def creation_dossier_data(cwd_data):
    """Création d'un dossier data si non existant"""
    if genericpath.isdir(cwd_data) is not True:
        os.mkdir(cwd_data)


# for categories in liste_url_categories():  # passage en revue de toute les catégories
def creation_dossier_categorie(cwd_data, categories):
    """Création d'un dossier par categorie si non existant"""
    nom_dossier_categorie = nom_categorie(categories)  # génération des noms nécessaires (dossier, fichier, path actuel, path pour les fichiers à créer)
    directory = cwd_data + nom_dossier_categorie + '/'
    if genericpath.isdir(directory) is not True:  # Vérification de l'existence d'un dossier pour la catégorie
        os.mkdir(directory)  # Création d'un dossier si non existant
        print("Dossier " + nom_dossier_categorie + ' créé')
    else:
        print("Dossier " + nom_dossier_categorie + " déjà existant")
#
    start = int(time.time())
def creation_csv(cwd_data, nom_dossier_categorie):
    nom_csv = nom_dossier_categorie + '.csv'
    directory = cwd_data + nom_dossier_categorie + '/'
    with open(os.path.join(directory + nom_csv), 'w', newline="", encoding="utf-8-sig") as csv_file:
        ligneXcel = csv.writer(csv_file, delimiter=',')
        ligneXcel.writerow(EN_TETE_COLONNES)
        for livres in liste_tous_livres_categorie(categories):
            informations = creation_un_livre(livres)
            ligneXcel.writerow(creation_un_livre(livres))
            telechargement_images(directory, informations)
    end = int(time.time())
    print(nom_dossier_categorie + ' terminé')
    print(str(end - start) + ' secondes écoulées')

def telechargement_images(directory, liste):
    with open(os.path.join(directory + construction_titre_image(liste)),'wb') as f:
        r = requests.get(liste[-1], stream=True)
        shutil.copyfileobj(r.raw, f)


