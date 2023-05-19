# Ultilizando a API PyCEPCorreios para busca de CEP integrado ao serviços dos Correios,
#  API OpenWeather de previsão do tempo e a bibliateca Requests
from pycep_correios import get_address_from_cep, WebService
import requests

# Função de recebe um CEP como parâmetro 
def getTemperature(cep, API_KEY):
    # Verifica tamanho de numeros do cep
    if len(cep) == 8: 
        # Retorna dados do CEP, usando webservice dos correios
        logradouro = get_address_from_cep(cep, webservice=WebService.CORREIOS)
        cidade = logradouro['cidade']

        # Usando o nome da cidade e a chave da API como parametros
        link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

        # Guardando informações em um dicionário usando json, extraindo a
        # temperatura atual e convertendo-a de kelvin para celsius.
        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        temperatura = requisicao_dic['main']['temp'] - 273.15
        print(f"Cidade: {logradouro['cidade']}")
        print(f"Temperatura: {temperatura:.0f}ºC")
    else:
        print("CEP inválido, teve ser de 8 digitos ou retire o  hífen (-) caso tenha usado!")

# Passando o CEP
getTemperature('CEP', "API KEY") # Insira o CEP e a Chave da API aqui