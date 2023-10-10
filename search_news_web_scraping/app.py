import requests                  #instalado com: pip3 install requests
from bs4 import BeautifulSoup    #instalado com: pip install bs4
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')

# print('Status.code: ', response.status_code)
# print('Header')
# print(response.headers)
# print(response.content)

content = response.content
site = BeautifulSoup(content, 'html.parser')

# print(site.prettify())   #Forma mais organizada para visualizar

# pega o HTML da noticia
noticias = site.findAll('div', attrs={'class' : 'feed-post-body'})

for noticia in noticias:
    #pega o titulo
    titulo = noticia.find('a', attrs={'class' : 'feed-post-link'})
    print(titulo.text)

    #pega o subtitulo
    subtitulo = noticia.find('li', attrs={'class':'bstn-relateditem'})
    if(subtitulo):
        print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])

    print(titulo['href'])
    print()

news = pd.DataFrame(lista_noticias, columns=[ 'Titulo', 'Subtitulo', 'Link'])
news.to_excel('noticias.xlsx', index=False)
print(news)