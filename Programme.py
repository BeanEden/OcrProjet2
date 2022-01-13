from functions import *

# test_liste_url_categories = liste_url_categories()
# test_liste_noms_categories = liste_noms_categories()

# print(len(test_liste_url_categories))
# print(len(test_liste_noms_categories))
#
# url_livre = "http://books.toscrape.com/catalogue/orange-the-complete-collection-1-orange-the-complete-collection-1_914/index.html"
# url_categorie = "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
#
# soup = soup_function(url_livre)
#
# # # print(extraction_tableau(soup))
# # # print(extraction_description(soup))
# # # print(extraction_categorie(soup))
# # print(extraction_rating(soup))
# # # print(extraction_titre(soup))
# # # print(extraction_url_image(soup))
# # print(extraction_titre(soup))
#
# liste_livre = creation_un_livre(url_livre)
# print(liste_livre)
# print(construction_titre_image(liste_livre))
#
# liste_cat = liste_tous_livres_categorie(url_categorie)
#
# print(liste_cat)
# print(thread_creation(liste_cat))

start = int(time.time())
cwd_data = chemin_acces()
creation_dossier_data(cwd_data)
urls_cat = liste_url_categories()

with concurrent.futures.ThreadPoolExecutor() as executor:
    tables = list(executor.map(lambda x: creation_dossier_categorie(cwd_data,x), urls_cat))
end = int(time.time())
time = end - start
print(time)