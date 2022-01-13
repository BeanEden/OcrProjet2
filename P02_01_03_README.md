README du Projet 2 OpenClassrooms
par Jean-Corentin Loirat
le 07/12/2021

Lien du repository git hub :
https://github.com/BeanEden/OcrProjet2.git


Contenu principaux : 
- fichier README.md
- fichier requirements.txt
- fichier Ecriture.py
- fichier fonctionsExtraction.py


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
Ces informations sont extraites catégories par catégories (exemple : Travel, Mystery...) et écrites dans un fichier csv par catégorie.
Les images des livres sont également récupérées.

L'ensemble de ces données est intégré dans un nouveau dossier "data".
Chaque catégorie dispose ensuite de son propre dossier (exemple : le dossier ../data/Travel contient le Csv et les images de la catégorie Travel).


Utilisation :
1 - importez les packages nécessaires au script (requests, bs4, csv, shutil, os, genericpath), présents dans le fichier requirements.txt
il est possible d'utiliser la ligne de commande "pip install -r requirements.txt"
ou d'installer les packages un par un : "pip install requests", "pip install bs4", "pip install shutil", "pip install os", "pip install shutil", "pip install csv23" 

2 - exécuter le script "ecriture.py"
via pyCharm, Visual Studio Code ... (ou tout autre logiciel)
ou via la ligne de commande "python ecriture.py"


Fonctionnement :
Le fichier "fonctionsExtraction.py" contient les fonctions d'extractions du contenu.
"ecriture.py" génère les dossiers des catégories
"ecriture.py" utilise les fonctions de "fonctionsExtraction.py" afin d'écrire les informations souhaitées dans les CSV et télécharger les images.


En savoir plus :
Le fonctionnement précis du script est docummenté directement dans le code des fichiers "ecriture.py" et "fonctionsExtraction.py" via des annotations###

