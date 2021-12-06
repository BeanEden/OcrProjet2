import requests
from bs4 import BeautifulSoup as bs
import csv
from extractFonctions import *

url = "http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html"
# url2 =


#
# with open('dataCat.csv', 'w', newline="") as csv_file:
#     ligneXcel = csv.writer(csv_file, delimiter=',')
#     ligneXcel.writerow(etlPage())
#     for livres in bouclePagination(url):
#         ligneXcel.writerow(etlValeurs(livres))

#
# print(len(bouclePagination(url)))
# print(urlLivresCategorie(url))

print(bouclePagination(url))