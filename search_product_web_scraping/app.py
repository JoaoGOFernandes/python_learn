import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

produto = input('Qual produto você deseja?')

response = requests.get(url_base + produto)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16'})

for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
    link = produto.find('a', attrs={'class': 'ui-search-link'})

    real = produto.find('span',attrs={'class':'andes-money-amount__fraction'})
    centavos = produto.find('span',attrs={'class':'andes-money-amount__cents'})

    print(titulo.text)
    print(link['href'])
    print('R$ ' + real.text + ',' + centavos.text)

    print('\n\n')


# print(produto.prettify())