import requests
from bs4 import BeautifulSoup as bs
import csv
from extractFonctions import *

url = "http://books.toscrape.com/catalogue/1000-places-to-see-before-you-die_1/index.html"
url2 = "http://books.toscrape.com/catalogue/sharp-objects_997/index.html"
url3 = "http://books.toscrape.com/catalogue/batman-europa_668/index.html"

with open('dataOne.csv', 'w', newline="") as csv_file:
    ligneXcel = csv.writer(csv_file, delimiter=',')
    ligneXcel.writerow(etlPage())
    ligneXcel.writerow(etlValeurs(url))
    ligneXcel.writerow(etlValeurs(url2))
    ligneXcel.writerow((etlValeurs(url3)))
