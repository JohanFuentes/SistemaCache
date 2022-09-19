from asyncio.windows_events import NULL
from time import time
from unicodedata import decimal, name
import requests
from bs4 import BeautifulSoup

# ------------------- READ_TXT ------------------- #
def read_csv(path, max_lines=None):
    
    with open(path, 'r') as f:
        cont = 0
        lines = f.readlines()[1:]
        f = open("DatosDB.txt", "w", encoding='utf-8', errors='ignore')
        f.write("CREATE TABLE Items(Id INT, Title VARCHAR(100), Description VARCHAR(100), Keywords VARCHAR(300), URL VARCHAR(100));\n")
        
        for line in lines:
            
            if (cont == max_lines):
                return
            tab = line.split('\t')

            # ------------------Evitamos las url en blanco. Es \n porque es el último término antes de un salto de linea.------------------ #
            if tab[4] == '\n':
                continue
            url = tab[4]
            
            # ------------------Evitamos el salto de linea.------------------ #
            c_url = url[:-1]
        
            data = getDataFromUrl(c_url, tab[1])
            
            if data is not None:
                f.write("INSERT INTO items(Id, Title, Description, Keywords, URL) VALUES (" + str(cont+1) + "," + repr(data["title"]) + "," + repr(data["description"]) + "," + repr(data["keywords"]) + "," + repr(data["url"]) + ");\n")
                cont += 1
            
            #f.close()
            
    return 

# ------------------- SCRAPING ------------------- #
def getDataFromUrl(url, palabras):
    collected_data = {'url': url, 'title': None, 'description': None, 'keywords': None}
    try:
        r = requests.get(url, timeout=20)
    except Exception:
        return None

    if r.status_code == 200:
        
        # Se usa BeautifulSoap para parsear la metadata de los documentos HTML.
        source = requests.get(url).text
        soup = BeautifulSoup(source, features='html.parser')

        # Se otienes las etiquetas meta
        meta = soup.find("meta")
            
        # Obtenemos el título
        title = soup.find('title')
        
        # Obtenemos la descripción
        description = soup.find("meta", {'name': "description"})
        
        # Obtenemos la keywords y las limpiamos
        keywords = soup.find("meta", {'name': "keywords"})
        
        try:
            if (keywords is None) or (keywords['content'] == '') or (keywords['content'] == ' ') or (keywords['content'] == NULL):
                keywords = palabras
            else:
                keywords = keywords['content']
            
            if description is None:
                d = soup.find('p').text
                if (d is None) or (d == "") or (d == " ") or (d == 0):
                    description = "No hay descripcion disponible"
                else:
                    description = d
            else:
                description = description['content'] if description else None
                
            keywords = keywords.replace(" ", "")
            keywords = keywords.replace(".", "")
                             
        except Exception:
            return None
            
        if title is None:
            title = "Titulo no disponible"
        else:
            t = title.get_text()

            if (t == "") or (t == NULL) or (t is None):
                title = "Titulo no disponible"
            elif isinstance(t, str) == True:
                title = title.get_text().replace("\n","") if title else None
                title = title.replace("\r","") if title else None
                title = title.replace("\t","") if title else None
            else:
                return None
        
        collected_data['title'] = title
        collected_data['description'] = description
        collected_data['keywords'] = keywords 

        if collected_data['keywords'] is None:
            palabras = palabras.replace(" ", "") if palabras else None
            palabras = palabras.replace(".", "") if palabras else None

        return collected_data
          
    return None

# ------------------- MAIN ------------------- #
if __name__ == '__main__':
    path = 'user-ct-test-collection-06.txt'
    read_csv(path, 1000)
    

