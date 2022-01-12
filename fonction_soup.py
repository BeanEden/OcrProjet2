

import requests
from bs4 import BeautifulSoup as bs


def soup_function(urlsoup):
    """Automatisation du parsage html
    # on peut gagner une ligne, au détriment de la lisibilité en skippant la variable "page" > soup = (reponse.content.decode('utf-8'), "html.parser")"""
    reponse = requests.get(urlsoup)
    page = reponse.content
    soup = bs(page.decode('utf-8'), "html.parser")
    return(soup)



