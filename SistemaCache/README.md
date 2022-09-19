### Sistema

Gran parte del codigo explicado a continuacion, fue extraido del siguiente Repositorio [repositorio](https://github.com/Joacker/Ayu-SD-2022-2/tree/main/Ayu2/python), realizando ciertas modificaciones para adaptarlo a la problemtaica planteada.

El sistema, está construido a partir de los siguientes elementos:

1. GRPC: es un sistema de llamada a procedimiento remoto. Utiliza como transporte HTTP/2 y Protocol Buffers como lenguaje de descripción de interfaz. Es utilizado para enviar la información desde el cliente (API) al backend y viceversa. Usando una estructura definida en el archivo "proto_message.proto", el cual se encuentra tanto en el backend, como en el cliente. Esta estructura contiene los mismos campos de la tabla creada en la base de datos Postgres. 

2. Backend: la principal función que tiene es, recibir una palabra de búsqueda desde el cliente, luego se conecta a Postgres y obtiene todos los elementos de la tabla creada en la base de datos, luego los filtra, almacenando en una variable sólo los elementos que en el campo de las "keywords", contengan la palabra consultada, por ultimo envia el resultado al cliente a traves de GRPC.

3. Cache: en la carpeta cache, se encuentra un archivo de configuración de Redis, donde se configura las políticas de remoción y el límite máximo de memoria. También se hace la conexión de Redis en el Cliente, donde también se configura. En el cliente es donde se crean los 3 nodos de Redis, para distribuir la carga de almacenamiento, donde cada vez que hay que almacenar algo en caché, se guarda aleatoriamente en uno de estos 3 nodos. 

4. Cliente: es una API, la cual recibe una palabra o frase como consulta y revisa si los resultados asociados a esta palabra o frase se encuentra en alguno de los nodos de Redis, si esta en alguno de los nodos, se devuelve el resultado. Si no está el resultado, en ningún nodo de Redis, se manda la palabra al backend a través de GRPC y el resultado que retorna, lo almacena en uno de los nodos de Redis, de forma aleatoria.

5. Base de datos: se usa para almacenar las URL con su respectiva metadata. En el archivo "init.sql", se crea una tabla y se insertan los datos obtenidos a través del Crawler.

### Funcionamiento

Todos los servicios fueron configurados en el docker-compose que se encuentra en este repositorio, donde se encuentran los siguientes servicios:

1. Servidor
2. Cliente
3. Nodos de Redis
4. Postgres

El comandos más relevantes son los siguientes:

Para levantar los servicios
```sh
docker-compose up --build
```
Para bajar los servicios
```sh
docker-compose down
```

Para realizar una petición a la API
```sh
http://localhost:8000/search?search=
```

Para borrar el cache en los contenedores
```sh
docker system prune -a
```

Para borrar el cache en los volúmenes
```sh
docker volume rm $(docker volume ls -q)
```
