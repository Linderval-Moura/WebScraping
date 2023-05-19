# Abaixo Bibliotecas usadas
import json
import requests
from bs4 import BeautifulSoup 
 
def getMetas(url):
    requisicao = requests.get(url) # Pegando a url do site
    requisicao_bytes = requisicao.content # Pegando a url como class bytes
    site = BeautifulSoup(requisicao_bytes, 'html.parser') # Extração de dados de arquivo HTML
    tags = site.find_all('meta') # HTML da notícia
    
    array = []
    # Percorrendo as tags, verificando-as e concatenando em um array
    for tag in tags: 
        if 'name' in tag.attrs.keys():
            a = {('name:',tag.attrs['name'].lower()), ('content:',tag.attrs['content'])}
            array += a
    # Convertendo para json com .dumps, e mudando para uma melhor aprensentação com .loads
    json_string = json.dumps(array)
    json_list = json.loads(json_string)
    print("json:\n",json_list)
# Passando o URL
getMetas('URL') #Insira a sua url aqui!