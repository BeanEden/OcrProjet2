import requests
from bs4 import BeautifulSoup as bs

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

informations = []
informationsVal = []
tableauFinal = {}

# Correction des listes
# def deleteIndex(index):
#     del informations[index]
#     del informationsVal[index]

# Intégration dans le fichier CSV
# def écriture():
#     with open('data.csv', 'w', newline="") as csv_file:
#     dw = csv.DictWriter(csv_file, delimiter=',', fieldnames=informations)
#     dw.writeheader()
#     dw.writerow(tableauFinal)

def etlPage(urlPage):
    reponse = requests.get(urlPage)
    page = reponse.content

    # transforme (parse) le HTML en objet BeautifulSoup
    soup = bs(page, "html.parser")
#
# def etlInformations(soup):
    # Extration des informations présentes dans le tableau "Product information" de la page web
    # Mise en forme liste
    for classes in soup.find_all("th", ):
        informations.append(classes.string)

    # Ajout de la première valeur aux listes : l'url
    informations.insert(0,"product_page_url")
    informations.insert(2, "title")
    # Ajout de la catégorie aux listes
    informations.extend(("product_description","category", "review_rating", "image_url"))
    informations.remove("Product Type")
    informations.remove("Tax")
    informations.remove("Number of reviews")
    print(informations)
    return

def etlValeurs(urlPage):
    reponse = requests.get(urlPage)
    page = reponse.content

    # transforme (parse) le HTML en objet BeautifulSoup
    soup = bs(page, "html.parser")

    for x in soup.find_all("td", ):
        informationsVal.append(x.string)

    # Extraction de la description
    descriptionListe = []

    for links in soup.find_all("p", ):
        descriptionListe.append(links.string)
    descriptionVal = descriptionListe[3]

    # Extraction de la catégorie
    listeAriane = []
    # Fake star rating
    reviewRatingVal = "Tree"
    # Extraction de l'image aux listes

    for liens in soup.find_all("a", href_=""):
        listeAriane.append(liens.string)

    informationsVal.insert(0,url)
    informationsVal.insert(2, (soup.h1.string))    # Ajout du titre aux listes en troisième position
    informationsVal.extend((descriptionVal, listeAriane[-1], reviewRatingVal))

    for val in soup.find_all("img"):
        # print(val.get('src'))
        informationsVal.append(val.get("src"))
    del informationsVal[3]
    del informationsVal[5]
    del informationsVal[6]

    print(informationsVal)
    return

print(etlPage(url))
print(etlValeurs(url))