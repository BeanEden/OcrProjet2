# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup as bs
import csv
from etlsplit import etlPage
from etlsplit import etlValeurs
from etlsplit import urlLivresCategorie
from etlsplit import categorieFinder
from etlsplit import fpageIndex
from etlsplit import


url = "http://books.toscrape.com/catalogue/sharp-objects_997/index.html"
urlcategorie = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
# reponse = requests.get(url)
# page = reponse.content
# soup = bs(reponse.content,"html.parser")

# print(etlValeurs(url))
# print(urlLivresCategorie(urlcategorie))
# Mystery = urlLivresCategorie(urlcategorie)
#
# print(etlValeurs((Mystery[0])))
#
# # print(len(etlValeurs((Mystery[0]))))
# for i in urlLivresCategorie(urlcategorie):
#     print(etlValeurs(i))

# with open('data.csv', 'w', newline="") as csv_file:
#     ligneXcel = csv.writer(csv_file, delimiter=',')
#     ligneXcel.writerow(etlPage(url))
#         for livres in urlLivresCategorie(urlcategorie):
#         ligneXcel.writerow(etlValeurs(livres))


with open('data.csv', 'w', newline="") as csv_file:
    ligneXcel = csv.writer(csv_file, delimiter=',')
    ligneXcel.writerow(etlPage(url))
    for categorie in categorieFinder():
        for livres in urlLivresCategorie(categorie):
            ligneXcel.writerow(etlValeurs(livres))

    # dw = csv.DictWriter(csv_file, delimiter=',', fieldnames=informations)
    # dw.writeheader()
    # dw.writerow(tableauFinal)

# print(url.etlPage())
#
# for i in listeUrl :
#     print(i.etlPage())
#     print(i.etlValeurs())