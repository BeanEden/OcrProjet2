README du Projet 2 OpenClassrooms
par Jean-Corentin Loirat
le 07/12/2021 (mis à jour le 13/01/2022)

Lien du repository git hub :
https://github.com/BeanEden/OcrProjet2.git


Contenu principaux : 
- fichier P02_01_01_execution.py
- fichier P02_01_01_functions.py
- fichier P02_01_liengithub
- fichier P02_01_02_requirements.txt
- fichier P02_01_03_README.md

Description :
Il s'agit d'un script permettant d'extraire du site : http://books.toscrape.com/index.html des informations et images concernant des livres.
Le script récupère, pour chaque livre présent sur le site, les informations suivantes :
 - product_page_url
 - universal_ product_code (upc)
 - title
 - price_including_tax
 - price_excluding_tax
 - number_available
 - product_description
 - category
 - review_rating
 - image_url 
Ces informations sont extraites catégorie par catégorie (exemple : Travel, Mystery...) et écrites dans un fichier csv par catégorie.
Les images des livres sont également récupérées.

L'ensemble de ces données est intégré dans un nouveau dossier "data".
Chaque catégorie dispose ensuite de son propre dossier (exemple : le dossier ../data/Travel contient le Csv et les images de la catégorie Travel).


Utilisation :
1 - Importez dans votre environnement virtuel les packages nécessaires au script (requests, bs4, csv, future3), tels que présents dans le fichier requirements.txt
Il est possible d'utiliser la ligne de commande "pip install -r P02_01_02_requirements.txt",
ou d'installer les packages un par un : "pip install requests"

2 - Exécutez le script "P02_01_01_execution.py" via la ligne de commande "python P02_01_01_execution.py",
ou via pyCharm, Visual Studio Code ... (ou tout autre logiciel)



Fonctionnement :
Le fichier "P02_01_01_functions.py" contient les fonctions d'extractions du contenu.
"P02_01_01_execution.py" génère les dossiers des catégories et appelle les fonctions de "fonctionsExtraction.py" afin d'écrire les informations souhaitées dans les CSV et télécharger les images.


En savoir plus :
Les fonctions de "P02_01_01_functions.py" sont documentées via docstrings avec leurs utilisations, arguments et retours.

