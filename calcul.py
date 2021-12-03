# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup as bs
import csv
from etlsplit import etlPage
from etlsplit import etlValeurs




informations = []
informationsVal = []
tableauFinal = {}

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
# reponse = requests.get(url)
# page = reponse.content
# soup = bs(reponse.content,"html.parser")

listeUrl = [url]


print(etlPage(url))
print(etlValeurs(url))


# print(url.etlPage())
#
# for i in listeUrl :
#     print(i.etlPage())
#     print(i.etlValeurs())




