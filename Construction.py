from fonctions_extraction_livres import *
from fonction_soup import soup_function
from fonctions_extraction_categories import *

EN_TETE_COLONNES = (
    "product_page_url",
    "universal_product_code (upc)",
    "title",
    "price_excluding_tax",
    "price_including_tax",
    "number available",
    "product_description",
    "category",
    "review_rating",
    "image_url"
)

def creation_un_livre(url_page_livre):
    soup = soup_function(url_page_livre)

    liste_informations_livre = []
    liste_informations_livre.append(url_page_livre)
    liste_informations_livre.extend(extraction_tableau(soup))
    liste_informations_livre.insert(2,extraction_titre(soup))
    liste_informations_livre.extend(extraction_description(soup))
    liste_informations_livre.append(extraction_categorie(soup))
    liste_informations_livre.append(extraction_rating(soup))
    liste_informations_livre.append(extraction_url_image(soup))

    return liste_informations_livre




url = "http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
print(EN_TETE_COLONNES)
print(creation_un_livre(url))
#
# url_cat = "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
#
# for livre in liste_tous_livres_categorie(url_cat):
#     print(creation_un_livre(livre))