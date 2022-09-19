### Redis

El sistema de caché implementado en Redis, consta de 3 nodos, donde se distribuye aleatoriamente la información. Las configuraciones de cada nodo son las siguientes:

1. Políticas de remoción: algoritmo utilizado para remover un elemento del caché, cuando esté lleno
2. Límite de máxima memoria: límite de la máxima memoria disponible en un nodo

En este caso se usaron las siguientes configuraciones:

1. Política de remoción LRU y límite de máxima memoria de 900 Kb
2. Política de remoción LRU y límite de máxima memoria de 2000 Kb
3. Política de remoción LFU y límite de máxima memoria de 900 Kb
4. Política de remoción LFU y límite de máxima memoria de 2000 Kb

A traves del archivo "analisis.py", se analisan las métricas de latencia y aciertos de caché (los resultados se encuentran en "resultadosMetricas"), de las 4 configuraciones antes mencionadas. Las consultas que se realizan, se extraen del archivo "keywords.txt", el cual es generado por el archivo "obtieneKeywords.py", el archivo "keywords.txt", contiene un numero de 1416 keywords, extraidas aleatoriamente de las keywords del archivo "DatosDB.txt".
