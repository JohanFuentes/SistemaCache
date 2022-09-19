import requests
import time

sumaTiempoRedis1 = 0
sumaTiempoRedis2 = 0
sumaTiempoRedis3 = 0
sumaTiempoPostgres = 0
cont1 = 0
cont2 = 0
cont3 = 0
contp = 0

fichero = open('keywords.txt')
lineas = fichero.readlines()

for search in lineas:

    a = time.time()*1000
    r = requests.get('http://localhost:8000/search?search='+search)
    b = time.time()*1000

    tipo = str(r.content)[251:252]

    tiempoMS = b-a


    if tipo == "1":
        cont1 = cont1 + 1
        sumaTiempoRedis1 = sumaTiempoRedis1 + tiempoMS
        print("sacado del nodo 1")
    elif tipo == "2":
        print("sacado del nodo 2")
        sumaTiempoRedis2 = sumaTiempoRedis2 + tiempoMS
        cont2 = cont2 + 1
    elif tipo == "3":
        print("sacado del nodo 3")
        cont3 = cont3 + 1
        sumaTiempoRedis3 = sumaTiempoRedis3 + tiempoMS
    else:
        print("sacado de Postgres")
        contp = contp + 1
        sumaTiempoPostgres = sumaTiempoPostgres + tiempoMS

print('Consultas respondidas por el backend: ',contp)
print('Tiempo promedio de respuesta del backend',sumaTiempoPostgres/contp)
print('Consultas respondidas por Redis: ',cont1+cont2+cont3)
print('Tiempo promedio de respuesta de redis',(sumaTiempoRedis3+sumaTiempoRedis2+sumaTiempoRedis1)/(cont1+cont2+cont3))
print('Consultas respondidas por el nodo 1 de Redis: ',cont1)
print('Tiempo promedio de respuesta del nodo 1 de Redis',sumaTiempoRedis1/cont1)
print('Consultas respondidas por el nodo 2 de Redis: ',cont2)
print('Tiempo promedio de respuesta del nodo 2 de Redis',sumaTiempoRedis2/cont2)
print('Consultas respondidas por el nodo 3 de Redis: ',cont3)
print('Tiempo promedio de respuesta del nodo 3 de Redis',sumaTiempoRedis3/cont3)
