import requests
import csv
from pymongo import MongoClient
import sys
from bs4 import BeautifulSoup

# Classe do produto

class Product:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name}"

# Função de busca

def prodSearch(name, store):
    if store.lower() == 'kabum':
        req = requests.get('https://www.kabum.com.br/busca/{}'.format(name.replace(' ','%20')))
    soup = BeautifulSoup(req.text, 'html.parser')
    with open('soup.html', "w", encoding="utf-8") as f:
        f.write(req.text)
    all_tag_span = soup.find_all('span')
    for tag_span in all_tag_span:
        class_span = tag_span.get('class')
        if 'sc-' in str(class_span):
            print(tag_span.text)

############ MAIN
name = input('Hardware a ser buscado:')
product = Product(name)
prodSearch(product.name, 'kabum')
