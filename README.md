# Sistema Cache

### Descripción del sistema

Sistema cache desarrollado en Python, el cual nos permite reducir considerablemente, las consultas que se realizan al backend de una aplicación.

Este sistema permite simular un buscador web, al cual se le ingresan consultas a través de un cliente(API) y este revisa si existe la consulta en el caché de Redis, si no existe, se dirige al backend y le consulta a la base de datos Postgres y retorna el valor de la consulta correspondiente, guardando así el valor de la consulta en el caché de Redis. Si se encuentra la consulta en el caché de Redis, este la retorna automáticamente, sin necesidad de consultarle al backend de la aplicación. Además, cabe mencionar, que la forma de comunicación entre el backend y el cliente, es a través de GRPC, el cual es un moderno sistema de llamada a procedimiento.

### Enlace del vídeo del funcioamiento del Sistema

[video](https://player.vimeo.com/video/751082572?h=0881c993b2&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479)

### Obtención de los datos guardados en Postgres

Los datos inicialmente almacenados en Postgres, se obtienen a través de una "query log", en la cual se muestran distintas búsquedas hechas por usuarios, en un buscador web. La información de las url se extrae de este "query log" y el resto de información guardado en la base de datos, se extrae de un crawler, el cual extrae la metada más relevante de cada url (para este caso).

### Métricas utilizadas

Las métricas utilizadas, son con respecto a las distintas configuraciones que tiene el sistema caché de Redis, principalmente el uso de políticas de remoción y el límite máximo de memoria. Al variar estas configuraciones, se analiza principalmente 2 métricas, la latencia y los aciertos de caché.

