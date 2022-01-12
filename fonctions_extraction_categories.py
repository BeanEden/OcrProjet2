

from fonction_soup import soup_function


def liste_url_categories():
    """Création de la liste des url de catégorie
    Cette fonction ne requiert aucun argument et génère la liste suivante [urlcategorie1, urlcategorie2,...]
    Elle se base sur la page d'accueil du site, extrait les url et les corrige (ajoute http://books.toscrape.com au début des url)"""
    url = "http://books.toscrape.com/index.html"
    complet_url = "http://books.toscrape.com/"
    soup = soup_function(url)

    url_categories = []
    box_livres = soup.find('ul', class_='nav')

    for a in box_livres.find_all('a', href=True):
        url_categories.append(complet_url + a['href'])
    del url_categories[0]       # retrait de l'url "books" qui n'est pas une categorie à étudier

    return(url_categories)


def liste_noms_categories():
    url = "http://books.toscrape.com/index.html"
    soup = soup_function(url)

    titre_categories = []
    box_noms = soup.find('ul', class_='nav')

    for a in box_noms.find_all('a', href=True):
        titre = a.get_text()
        titre_categories.append(titre.strip('\n                            \n                        '))
    del titre_categories[0]

    return titre_categories


def liste_url_livres_categorie(url_categorie):
    """Extrait les url de tous les livres présent sur UNE page catégorie
    Argument : URL d'une page de catégorie (pas de différence page 1 ou page 2)
    Retourne une liste"""

    root = "http://books.toscrape.com/catalogue/"
    soup = soup_function(url_categorie)

    boxLivres = soup.find('ol', class_='row')
    liste_categorie_intermediaire = []

    for a in boxLivres.find_all('a', href=True):
        liste_categorie_intermediaire.append(a['href'])

    liste_url_livres_categorie = list(dict.fromkeys(liste_categorie_intermediaire))

    liste_finale_url_livres = []
    for livres in liste_url_livres_categorie :
        liste_finale_url_livres.append(livres.replace("../../../", root))

    return liste_finale_url_livres


def verification_page_2(urlPage):
    """Verifie l'existence d'une seconde page dans la categorie"""
    soup = soup_function(urlPage)

    box_page = soup.find('li', class_='next')
    page_index = ""
    if box_page is not None :
       for a in box_page.find_all('a', href=True):
            page_index = (a['href'])
    else :
        page_index = None
    return(page_index)


def liste_tous_livres_categorie(url_page_index_categorie):
    """Recupère l'ensemble des url des livres de la categorie (sur toutes les pages)"""
    liste_toutes_pages = liste_url_livres_categorie(url_page_index_categorie)
    pageN = verification_page_2(url_page_index_categorie)

    if url_page_index_categorie.find("page-1") >= -1 :         # correction du cas particulier "page-1")
        url_page_index_categorie = url_page_index_categorie.replace("page-1.html","index.html")

    while pageN is not None:        # boucle selon la pagination (tant qu'il existe une page suivante, on continue)
        url_new_page = url_page_index_categorie.replace("index.html", pageN)
        pageN = verification_page_2(url_new_page)
        liste_toutes_pages.extend(liste_url_livres_categorie(url_new_page))

    return liste_toutes_pages

def nom_categorie(url):
    # categorieListe = []
    # for titre in categorieFinder():
    soup = soup_function(url)
    nom_categorie = (soup.h1.string)
    return nom_categorie


# url = "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
# # print(liste_url_categories())
# # print(liste_noms_categories())
# # print(liste_url_livres_categorie(url))
# # print(liste_tous_livres_categorie(url))
# # print(len(liste_tous_livres_categorie(url)))
# print(nom_categorie(url))