# Abaixo Bibliotecas usadas
from bs2json import bs2json #Converte tags HTML da classe BeautifulSoup em dados JSON.
from bs4 import BeautifulSoup
import requests
 
def getMetas(url):
    # Extração de dados de arquivo html.
    requisicao = requests.get(url)
    html = requisicao.text # Pegando a url como text
    soup = BeautifulSoup(html,'lxml') # Extração de dados de arquivo lxml

    # Convertendo tags HTML de BeautifulSoup para JSON.
    converter = bs2json()
    tags = soup.findAll('meta') 
    json = converter.convertAll(tags,join=True)
    print("Json:\n", json)
# Passando o URL
getMetas('URL') #Insira a sua url aqui!