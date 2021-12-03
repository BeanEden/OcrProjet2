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
    soup = bs(page, "html.parser")

# def etlInformations(soup):
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

    return informations

def etlValeurs(urlPageVal):
    reponse = requests.get(urlPageVal)
    page = reponse.content
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

    return informationsVal


def urlLivresCategorie(urlCategorie):
    # root = url.replace("index.html","")
    root = "http://books.toscrape.com/catalogue/"
    reponse = requests.get(urlCategorie)
    page = reponse.content
    soup = bs(page, "html.parser")

    # print(soup)

    # html = '''<a href="some_url">next</a>
    # <span class="class"><a href="another_url">later</a></span>'''
    #
    # soup = BeautifulSoup(html)

    boxLivres = soup.find('ol', class_='row')
    listeCategorieIntermediaire = []

    for a in boxLivres.find_all('a', href=True):
        # print("Found the URL:", a['href'])
        listeCategorieIntermediaire.append(a['href'])

    def noDoublon(x):
        return list(dict.fromkeys(x))

    listeCategorie = noDoublon(listeCategorieIntermediaire)

    print(listeCategorie)

    def fullUrl(x):
        listeUrl = []
        for livres in x:
            listeUrl.append(livres.replace("../../../", root))
            # listeUrl.append(root+livres)
            # listeCategorie.replace("../../../",root)
        return listeUrl

    print(fullUrl(listeCategorie))

# print(etlPage(url))
# print(etlValeurs(url))