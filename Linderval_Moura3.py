# Abaixo Bibliotecas usadas
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os
# Função de recebe URL, níveis de procura e nome do arquivo
def getLinks(url, depth, fileName):
    if not url or len(url) < 1: # Verifica se URL é válida
        raise Exception("INFO: URL Invalida!")
    # Parâmetro do final da URL, Se é um link possivel link
    _fim = url.find('.com') 

    siteLegivel = url[_fim].strip() # Guarda nome legivel das urls 
    
    response = requests.get(url) # Pegando a url do site
    content = response.content # Pegando a url como class bytes

    site = BeautifulSoup(content, 'html.parser') # Extração de dados de arquivo HTML

    lista_links = []

    if depth == 0: #nível de procura 0

        for link in site.find_all('a', href=True): # Percorre tags com href
            if siteLegivel in link.get('href'): # Verifica se link é legivel 
                atualTime = datetime.now().time() # Obtem hora que o link foi encontrado
                lista_links.append([link['href'], atualTime]) # Concatena link e hora na lista
                  
    print("\n\nlista_links:\n",lista_links) # Imprimindo para acompanhar no terminal

    if depth == 1: #nível de procura 1
        
        for link in site.find_all('a', href=True): # FAZ O MESMO QUE O DO NÍVEL 0    
            if siteLegivel in link.get('href'):
                print("\n\nlink:\n",link.get('href'))
                atualTime = datetime.now().time()
                lista_links.append([link['href'], atualTime])
                  
        print("\n\nlista_links:\n",lista_links) # Imprimindo para acompanhar no terminal

        # O LAÇO ABAIXO PERCORRE TODOS OS LINKS DA LISTA DE LINKS ANTERIOR 
        for link in site.find_all('a', href=True): # Percorre tags com href
            if siteLegivel in link.get('href'): # Verifica se link é legivel 
                
                nova_response = requests.get(link.get('href')) # Pegando a url de cada link anterior
                nova_content = nova_response.content
                novo_site = BeautifulSoup(nova_content, 'html.parser')
                
                for link2 in novo_site.find_all('a', href=True): # Faz o mesmo que o nível 0, mas em cada link da     
                    if siteLegivel in link2.get('href'):         # lista anterior
                        atualTime = datetime.now().time() 
                        lista_links.append([link2['href'], atualTime])

        print("\n\nNOVA lista_links:\n",lista_links) # Imprimindo listado nível de procura 1

    if os.path.exists(fileName): # Verifique se o arquivo já existe, se sim, o exclui
        os.remove(fileName)
    # Estrutura de dados com duas colunas
    df = pd.DataFrame(lista_links, columns=['link', 'atualTime'])
    df = df.drop_duplicates(subset=['link']) # Remover duplicatas em coluna específica
    df.to_excel(fileName, index=False) # Salvando em arquivo xls

    print(df)

# Passando o URL, nível de procura e nome do arquivo
getLinks('URL', 0, 'fileName') #Insira a url, nível de procura e nome do arquivo a ser salvo aqui!
    