import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'

buscarPais = input("Por favor, el pais que quieres buscar:")
guardarPais=""

response = requests.get(url)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    
    news_elements = soup.find_all('h3', class_='country-name')  
    
    titles = [element.text.strip() for element in news_elements]
    
    print(f'Lista de paises')
    
    for i, title in enumerate(titles, start=1):
        print(f'Paises {i}: {title}')
        if buscarPais == title:
            guardarPais=title
            
else:
    print('Error al acceder a la página web.')

if guardarPais!="":
    print(f'Se encontro el pais :El pais que buscabas era {guardarPais}')

else:
   print(f'No se encontro pais') 
