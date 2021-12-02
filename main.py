# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup as bs


url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
reponse = requests.get(url)
page = reponse.content
soup = bs(reponse.content,"html.parser")


### Wished Columns
# product_page_url
# universal_product_code
# title
# price_including_tac
# price_excluding_tax
# number_available
# product_description
# category
# review_rating
# image_url


elements = dict(product_page_url=url, universal_product_code="UPC", title=soup.title.string, price_including_tax=0,
                price_excluding_tax=0, number_available=0, product_description=1, category="ae", review_rating=4,
                image_url="a")

### Définition des listes finales
# informations = liste des catégories/colonnes souhaitées
# informationsVal = valeur des catégories
# tableauFinal = mise en forme dictionnaire des 2 listes pour usage de DicReader
informations = []
informationsVal = []
tableauFinal={}

# Ajout de la première valeur aux listes : l'url
informations.append("product_page_url")
informationsVal.append(url)


# Extration des informations présentes dans le tableau "Product information" de la page web
colonnes = soup.find_all("th",)
contenu = soup.find_all("td",)

# Mise en forme liste
for classes in colonnes:
    informations.append(classes.string)

for x in contenu:
    informationsVal.append(x.string)



# Retrait des éléments non pertinent pour le projet : "Product Type", "Tax" et "Number of reviews"
# Retrait en deux temps : 1-> Valeur via index 2->informations via strings
indexRemoveProductType = informations.index("Product Type")
del informationsVal[indexRemoveProductType]

indexRemoveTax = informations.index("Tax")
del informationsVal[indexRemoveTax-1]

indexRemoveNumberOfReviews = informations.index("Number of reviews")
del informationsVal[indexRemoveNumberOfReviews-2]

informations.remove("Product Type")
informations.remove("Tax")
informations.remove("Number of reviews")

# Extraction du titre
titreLivre = soup.h1.string

# Ajout du titre aux listes en troisième position
informations.insert(2,"title")
informationsVal.insert(2,titreLivre)

# Extraction de la description
descriptionHtml = soup.find_all("p",)

descriptionListe = []

for links in descriptionHtml:
    descriptionListe.append(links.string)
descriptionVal = descriptionListe[3]

# Ajout de la description
informations.append("product_description")
informationsVal.append(descriptionVal)

# Extraction de la catégorie
filArianeDeCategorie = soup.find_all("a",href_="")
listeAriane = []

for liens in filArianeDeCategorie :
    listeAriane.append(liens.string)

categoryVal = listeAriane[-1]

# Ajout de la catégorie aux listes
informations.append("category")
informationsVal.append(categoryVal)

# Fake star rating
reviewRatingVal = "Tree"

informations.append("review_rating")
informationsVal.append(reviewRatingVal)


# Extraction de l'image aux listes
imageSoup=soup.find_all("img",)

informations.append("image_url")
informationsVal.append(imageSoup)


for clés, valClés in zip(informations, informationsVal):
    tableauFinal[clés] = valClés

print(informations)
print(informationsVal)
print(tableauFinal)