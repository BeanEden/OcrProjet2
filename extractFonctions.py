import requests
from bs4 import BeautifulSoup as bs

url = "http://books.toscrape.com/catalogue/1000-places-to-see-before-you-die_1/index.html"
urlcategorie = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"



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
def categorieFinder():
    url = "http://books.toscrape.com/index.html"
    completURL = "http://books.toscrape.com/"
    reponse = requests.get(url)
    page = reponse.content
    soup = bs(page.decode('utf-8'), "html.parser")
    #
    # print(soup.prettify())

    listeCategorie = []
    boxLivres = soup.find('ul', class_='nav')

    for a in boxLivres.find_all('a', href=True):
        # print("Found the URL:", a['href'])
        listeCategorie.append(completURL + a['href'])
    del listeCategorie[0]
    return(listeCategorie)

#défini la liste de categorie
# def listeCategorie():
#     categorieListe = []
#     for titre in categorieFinder():
#         reponse = requests.get(titre)
#         page = reponse.content
#         soup = bs(page, "html.parser")
#         categorieListe.append(soup.h1.string)
#     return categorieListe
#
# categorieList = listeCategorie()

categorieList = ['Travel', 'Mystery', 'Historical Fiction', 'Sequential Art', 'Classics', 'Philosophy', 'Romance', 'Womens Fiction', 'Fiction', 'Childrens', 'Religion', 'Nonfiction', 'Music', 'Default', 'Science Fiction', 'Sports and Games', 'Add a comment', 'Fantasy', 'New Adult', 'Young Adult', 'Science', 'Poetry', 'Paranormal', 'Art', 'Psychology', 'Autobiography', 'Parenting', 'Adult Fiction', 'Humor', 'Horror', 'History', 'Food and Drink', 'Christian Fiction', 'Business', 'Biography', 'Thriller', 'Contemporary', 'Spirituality', 'Academic', 'Self Help', 'Historical', 'Christian', 'Suspense', 'Short Stories', 'Novels', 'Health', 'Politics', 'Cultural', 'Erotica', 'Crime']

def fpageIndex(urlPage):
    reponse = requests.get(urlPage)
    page = reponse.content
    soup = bs(page, "html.parser")
    boxPage = soup.find('li', class_='next')
    pageIndex = ""
    if boxPage is not None :
       for a in boxPage.find_all('a', href=True):
            pageIndex = (a['href'])
    else :
        pageIndex = None
    return(pageIndex)

def urlLivresCategorie(urlCategorie):
    # root = url.replace("index.html","")
    root = "http://books.toscrape.com/catalogue/"
    reponse = requests.get(urlCategorie)
    page = reponse.content
    soup = bs(page.decode('utf-8'), "html.parser")

    boxLivres = soup.find('ol', class_='row')
    listeCategorieIntermediaire = []

    for a in boxLivres.find_all('a', href=True):
        # print("Found the URL:", a['href'])
        listeCategorieIntermediaire.append(a['href'])

    def noDoublon(x):
        return list(dict.fromkeys(x))

    listeCategorie = noDoublon(listeCategorieIntermediaire)

    def fullUrl(x):
        listeUrl = []
        for livres in x:
            listeUrl.append(livres.replace("../../../", root))
        return listeUrl

    listetotale = (fullUrl(listeCategorie))

    return listetotale


def bouclePagination(urlpagination):

    listetotale = urlLivresCategorie(urlpagination)
    pageN = fpageIndex(urlpagination)

    if urlpagination.find("page-1") >= -1 :
        urlpagination = urlpagination.replace("page-1.html","index.html")

    while pageN is not None:
        urlNewPage = urlpagination.replace("index.html", pageN)
        pageN = fpageIndex(urlNewPage)
        listetotale.extend(urlLivresCategorie(urlNewPage))

    return listetotale

# def lectureCategorie(urlCatFull):
#     urlPage1 = urlLivresCategorie(urlCatFull)
#     urlPages = bouclePagination(urlCatFull)
#     completeList = urlPage1 + urlPages
#     return completeList

def etlPage():
    urlInfos = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    informations = []
    reponse = requests.get(urlInfos)
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
    soup = bs(page.decode('utf-8'), "html.parser")
    informationsVal = []
    for x in soup.find_all("td", ):
        informationsVal.append(x.string)

    # Extraction de la description
    descriptionString = ""
    for links in soup.find_all("p", class_=None):
        descriptionString = links.string
    # if descriptionString.index(";") == True:
    #     while descriptionString.index(";") == True:
    #         descriptionString = descriptionString.replace(";", ",")
    descriptionVal = [descriptionString]

    # Extraction de la catégorie
    categorieVal = ""
    listeAriane = []
    boxCategory = soup.find('ul', class_="breadcrumb")
    for liens in boxCategory("a", href_=""):
        listeAriane.append(liens.string)
    for lien in listeAriane:
        if lien in categorieList:
            categorieVal = lien

    # Fake star rating
    reviewRatingVal = ""
    ratings = ["One", "Two", "Three", "Four", "Five"]
    boxRating = soup.find('div', class_="col-sm-6 product_main")
    for a in ratings:
        if boxRating.find('p', class_=a) is not None:
            reviewRatingVal = a


    for liens in soup.find_all("a", href_=""):
        listeAriane.append(liens.string)

    informationsVal.insert(0,urlPageVal)
    informationsVal.insert(2, (soup.h1.string))    # Ajout du titre aux listes en troisième position
    informationsVal.extend((descriptionVal, categorieVal, reviewRatingVal))
# Image
    boxImage = soup.find("div", class_="item active")
    for val in boxImage.find_all("img"):
        interm = val.get("src")
        informationsVal.append(interm.replace("../../", "http://books.toscrape.com/"))

    del informationsVal[3]
    del informationsVal[5]
    del informationsVal[6]

    return informationsVal



# # print(categorieFinder())
# print(len(lectureCategorie(urlcategorie)))
# print(len(urlLivresCategorie(urlcategorie)))
# print(len(bouclePagination(urlcategorie)))
print(etlPage())
print(etlValeurs(url))
