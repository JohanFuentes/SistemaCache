### Obtención del "query log"

El "query log", fue obtenido a través del siguiente enlace [Query Log](http://www.cim.mcgill.ca/~dudek/206/Logs/AOL-user-ct-collection/). El "query log" que fue utilizado, fue el "user-ct-test-collection-06.txt.gz". El archivo del "query log", consta de los siguientes campos:

1. AnonID: número de usuario anónimo
2. Query: consulta realizada por el usuario
3. QueryTime: fecha y hora de la consulta
4. ItemRank: si hizo click en una URL, muestra el número de la fila de la URL
5. ClickURL: si hizo click en una URL, muestra la URL

Los elementos que no tienen URL, no se tomaron en consideración.

### Crawler

Con el crawler se obtuvo información importante de cada URL, para luego agregarla a la base de datos Postgres. La información relevante fueron los siguientes campos de la metadata:

1. title: título de la página
2. description: descripción de la página
3. keywords: palabras claves de la página (antiguamente servían para posicionar las páginas)

Al ser una gran cantidad de datos en el archivo "query log", solamente se recopilaron 700 elementos con el Crawler, los datos obtenidos se encuentran en el archivo “DatosDB.txt”. El contenido de este archivo, es el que se copia en el archivo "init.sql", el cual permite insertar los datos en la base de datos, una vez iniciados los servicios.

La estructura de la tabla en la base de datos queda de la siguiente forma:

```CREATE TABLE Items(Id INT, Title VARCHAR(800), Description VARCHAR(2000), Keywords VARCHAR(2000), URL VARCHAR(500));```

Donde el campo Id es serial. Por último, cabe mencionar que se descartaron todos los elementos del archivo "query log", que no tuvieran completos todos los campos.
