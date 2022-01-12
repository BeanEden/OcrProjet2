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
from Ecriture import *
from futures3.thread import ThreadPoolExecutor
from futures3.process import ProcessPoolExecutor
import concurrent.futures
import urllib.request

cwd_data = chemin_acces()
creation_dossier_data(cwd_data)

for categorie in liste_url_categories():  # passage en revue de toute les catégories
    creation_dossier_categorie(cwd_data, categorie)
    # creation_csv(cwd_data, categorie)


#
# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#     # Start the load operations and mark each future with its URL
#     future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
#     for future in concurrent.futures.as_completed(future_to_url):
#         url = future_to_url[future]
#         try:
#             data = future.result()
#         except Exception as exc:
#             print('%r generated an exception: %s' % (url, exc))
#         else:
#             print('%r page is %d bytes' % (url, len(data)))