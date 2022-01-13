### Le présent fichier exécute le programme d'extraction des données du site "bookstoscrape.com"
# Les fonctions nécessaires à l'exécution du programme sont importées depuis le fichier P02_01_01_functions.py

import time
from P02_01_01_functions import *

start = int(time.time())
cwd_data = chemin_acces()
urls_cat = liste_url_categories()

with concurrent.futures.ThreadPoolExecutor() as executor:
    tables = list(executor.map(lambda x: creation_dossier_categorie(cwd_data,x), urls_cat))
end = int(time.time())
time = end - start
print(time)
