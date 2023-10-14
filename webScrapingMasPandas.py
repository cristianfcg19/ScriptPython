
import requests
from bs4 import BeautifulSoup
import pandas as pd



def verListaProjectosCsv():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)  
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    try:
        df = pd.read_csv('listaPaises.csv')
        print("Lista de paises en el archivo csv")
        print(df)
    except Exception as e:
        print(f"Error: {e} - No se encuentra el archivo.")
            
 
        

def verlistaPaiseScraping(url):
    
    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        news_elements = soup.find_all('h3', class_='country-name')

        titles = [element.text.strip() for element in news_elements]

        print(f'Lista de paises')

        for i, title in enumerate(titles, start=1):
            print(f'Paises {i}: {title}')
            
    else:
        print('Error al acceder a la página web.')

def CrearArchivoCSVPaises(url):

    lista_paises = []


    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        news_elements = soup.find_all('h3', class_='country-name')

        titles = [element.text.strip() for element in news_elements]

        print(f'Lista de paises')

        for i, title in enumerate(titles, start=1):
            print(f'Paises {i}: {title}')
            lista_paises.append(title)
           

    else:
        print('Error al acceder a la página web.')

   

    df = pd.DataFrame(lista_paises)

    df.to_csv('listaPaises.csv', index=False)
    print("Se crea el Archivo CSV con la lista de paises ")

def BuscarPaises(url):

    lista_paises = []

    buscarPais = input("Por favor, el pais que quieres buscar:")
    guardarPais = ""

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        news_elements = soup.find_all('h3', class_='country-name')

        titles = [element.text.strip() for element in news_elements]

        print(f'Lista de paises')

        for i, title in enumerate(titles, start=1):
            print(f'Paises {i}: {title}')
            lista_paises.append(title)
            if buscarPais == title:
                guardarPais = title

    else:
        print('Error al acceder a la página web.')

    if guardarPais != "":
        print(f'Se encontro el pais :El pais que buscabas era {guardarPais}')
    else:
        print(f'No se encontro pais')

   


def menu():
    print("1. Ver lista de países (scraping)")
    print("2. Ver lista de proyectos (desde archivo CSV)")
    print("3. Buscar países")
    print("4. Crear archivo CSV de países")
    print("5. Salir")

while True:
    menu()
    SeleccioneUnaOpcion = input("Seleccione una opción: ")

    if SeleccioneUnaOpcion=="1":
        url = 'https://www.scrapethissite.com/pages/simple/'
        verlistaPaiseScraping(url)
    elif SeleccioneUnaOpcion=="2":
        verListaProjectosCsv()
    elif SeleccioneUnaOpcion=="3":
        url = 'https://www.scrapethissite.com/pages/simple/'
        BuscarPaises(url)
    elif SeleccioneUnaOpcion=="4":
        url = 'https://www.scrapethissite.com/pages/simple/'
        CrearArchivoCSVPaises(url)
    elif SeleccioneUnaOpcion=="5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")