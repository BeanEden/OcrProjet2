import requests
from bs4 import BeautifulSoup as bs
import csv
from extractFonctions import *

url = "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
# url2 = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"


#
with open('dataFull.csv', 'w', newline="", encoding="utf-8-sig") as csv_file:
    ligneXcel = csv.writer(csv_file, delimiter=',')
    ligneXcel.writerow(etlPage())
    for categories in categorieFinder():
        for livres in bouclePagination(categories):
            ligneXcel.writerow(etlValeurs(livres))
        print(categories)