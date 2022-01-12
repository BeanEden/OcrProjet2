
from fonctions_extraction_categories import liste_noms_categories
from fonction_soup import soup_function


def extraction_tableau(soup):
    """Extraction de l'upc, des prix (avec et sans taxes), et des stocks
    Argument : soup
    Retourne une liste"""

    liste_informations = []

    for x in soup.find_all("td", ):
        liste_informations.append(x.string)

    del liste_informations[-1]
    del liste_informations[4]
    del liste_informations[1]

    return liste_informations


def extraction_description(soup):
    """Extraction de la description (en liste pour uniformisation de l'encodage)"""
    description_string = ""
    for links in soup.find_all("p", class_=None):
        description_string = links.string
    description_val = [description_string]
    return description_val


def extraction_categorie(soup):
    """Extraction de la catégorie"""
    categorie_string = ""
    liste_ariane = []
    boxCategory = soup.find('ul', class_="breadcrumb")

    for liens in boxCategory("a", href_=""):
        liste_ariane.append(liens.string)

    liste = liste_noms_categories()
    for lien in liste_ariane:
        if lien in liste:
            categorie_string = lien
    return categorie_string


def extraction_rating(soup):
    """Extraction de la notation
    Comparatif avec une liste et retour d'une valeur définie"""

    review_rating_string = ""
    ratings = ("One", "Two", "Three", "Four", "Five")
    boxRating = soup.find('div', class_="col-sm-6 product_main")
    for a in ratings:
        if boxRating.find('p', class_=a) is not None:
            review_rating_string = a
    return review_rating_string


def extraction_titre(soup):
    """Extraction du titre
    Argument : soup
    Retourne une string"""
    titre_livre_string = soup.h1.string
    return titre_livre_string


def extraction_url_image(soup):
    # Extraction et insertion de l'url de l'image
    box_image = soup.find("div", class_="item active")
    url_image_string = ""
    for val in box_image.find_all("img"):
        interm = val.get("src")
        url_image_string = interm.replace("../../", "http://books.toscrape.com/")
    return url_image_string


def construction_titre_image(liste):
    liste_nom = liste[2]
    titre_livre = liste_nom[0:25]
    titre_image = titre_livre + '.jpg'
    return titre_image




### Les éléments ci-dessous servent à tester le fichier indépendemment d'une création de fichier excel

url = "http://books.toscrape.com/catalogue/orange-the-complete-collection-1-orange-the-complete-collection-1_914/index.html"
urlcategorie = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

# print(categorieFinder())
# print(len(lectureCategorie(urlcategorie)))
# print(len(urlLivresCategorie(urlcategorie)))
# # print(len(bouclePagination(urlcategorie)))
# # print(etlPage())
# print(etlValeurs(url))
# print(etlValeurs(url)[2])
