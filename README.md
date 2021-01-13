# Proyecto Primer Cuatrimestre de migfigesc

El proyecto trata sobre los vuelos con destino / origen India, donde aparte de aparecer la información del día, aerolinea y pasajeros, aparece también la carga de material que lleva la aeronave

Para que el archivo .csv se ajuste a las necesidades se ha añadido una columna con fechas aleatorias, que indica cuando se produjo el vuelo
de esa entrada de datos

 - Columna 1 (str) - airline: aerolinea que efectua el trayecto
 - Columna 2 (str) - carrier_type: modalidad del trayecto (domestico o hacia el extranjero)
 - Columna 3 (int) - passengers_to: pasajeros que lleva desde el origen hasta India
 - Columna 4 (int) - pasengers_from: pasajeros que lleva hasta el destino desde India
 - Columna 5 (int) - freight_to: material de carga que lleva desde el origen hasta India
 - Columna 6 (int) - freight_from: material de carga que lleva hasta el destino desde India
 - Columna 7 (fecha) - date: fecha donde se efectuan los viajes
 
NOTA: intuyendo los datos, suponemos que cada linea de datos será el recuento del número
total de viajes de ese día de ese trayecto (Origen1 - Destino1)

URL del dataset original: https://www.kaggle.com/rajanand/international-air-traffic-from-and-to-india

## Descripción de funciones implementadas

 - lee_datos_trafico: lee los datos del archivo csv
 - calcula_aerolinea: devuelve una conjunto con el listado de aerolineas que aparecen en el .csv
 - filtra_por_aerolinea: devuelve un listado donde aparecen todas las fechas de los vueltos y su tipo (domestico o extranjero) de una aerolinea concreta
 - total_pasajeros_destino_por_aerolinea: calcula el número total de pasajeros llevados a sus correspondientes destinos por una aerolinea concreta
 - top_pasajeros_segun_modalidad_trayecto: ordena de mayor a menor los registros de vuelo con más pasajeros llevados a su destino, según la modalidad del trayecto (carrier_type)
 - agrupar_por_aerolinea: muestra por pantalla el listado de aerolineas que operan, dependiendo si son en territorio nacional (DOMESTIC) o al extranjero (FOREIGN)
 - contar_vuelos_por_aerolinea: muestra un listado en pantalla del número de vuelos que ha realizado cada aerolinea durante el periodo de tiempo en el que se han recogido los datos del fichero csv
 - carrier_type_mas_carga_destino: muestra la modalidad de vuelo que más carga ha llevado a destino
 - aerolineas_hasta_india: muestra de forma ordenada por aerolinea las que más pasajeros han trasladado hasta India
 - grafica_aerolineas_viajeros: genera una gráfica de barras con el número de vuelos que ha hecho cada aerolinea

## Log de versiones
 - v1.0 Totalidad de funciones implementadas
 - v1.1 Actualización de archivo README.md
 - v1.2 Actualización del archivo README.md
