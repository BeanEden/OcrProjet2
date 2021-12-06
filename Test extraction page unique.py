import requests
from bs4 import BeautifulSoup as bs
import csv
from extractFonctions import *

url = "http://books.toscrape.com/catalogue/1000-places-to-see-before-you-die_1/index.html"

with open('dataOne.csv', 'w', newline="") as csv_file:
    ligneXcel = csv.writer(csv_file, delimiter=',')
    ligneXcel.writerow(etlPage())
    ligneXcel.writerow(etlValeurs(url))
