import requests
import csv
from pymongo import MongoClient
import sys
from bs4 import BeautifulSoup

# Classe do produto

class Product:
    def __init__(self, name):
        self.name = name

# Função de busca

def prodSearch(name):
    name = name.replace(' ','+')
    req = requests.get('https://www.kabum.com.br/busca?query={}'.format(name))
    soup = BeautifulSoup(req.text, 'html.parser')
    print(soup)




name = input('Hardware a ser buscado:')

product = Product(name)




