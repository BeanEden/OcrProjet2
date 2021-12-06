import requests
from bs4 import BeautifulSoup as bs
import csv
from extractFonctions import *

url = "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
# url2 = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"


#
with open('dataCat.csv', 'w', newline="", encoding="utf-8-sig") as csv_file:
    ligneXcel = csv.writer(csv_file, delimiter=',')
    ligneXcel.writerow(etlPage())
    for livres in bouclePagination(url):
        ligneXcel.writerow(etlValeurs(livres))

#
# print(len(bouclePagination(url)))
# print(urlLivresCategorie(url))

# print(bouclePagination(url))
# print(len(bouclePagination(url)))