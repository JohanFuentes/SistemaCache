#from asyncio.windows_events import NULL
from time import time
from unicodedata import decimal, name

# ------------------- READ_TXT ------------------- #
def read_csv(path):
    
    with open(path, 'r',encoding='utf8') as f:
        
        lines = f.readlines()[1:]
        f = open("keywords.txt", "w", encoding='utf8', errors='ignore')
        
        for line in lines:
            tab = line.split(",'",1)
            tab2 = tab[1].split("','")

            if(len(tab2) == 4):
                coma = ","

                if coma in tab2[2]:
                    tab3 = tab2[2].split(",",1)
                    palabra = tab3[0]
                else:
                    palabra = tab2[2]

                f.write(palabra + "\n")
            
    f.close()        
    return 

# ------------------- MAIN ------------------- #
if __name__ == '__main__':
    path = 'DatosDB.txt'
    read_csv(path)
    

