# -*- coding: utf-8 -*-

import csv
from collections import namedtuple
from datetime import *
#from matplotlib import pyplot as plt



DatoTrafico = namedtuple('DatoTrafico', 'airline, carrier_type, passengers_to, passengers_from, freight_to, freight_from, date')


def lee_datos_trafico(fichero):
    lista_de_datos = []
    with open (fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for airline, carrier_type, passengers_to, passengers_from, freight_to, freight_from, date in lector:
            passengers_to=int(passengers_to)
            passengers_from=int(passengers_from)
            freight_to=int(freight_to)
            freight_from=int(freight_from)
            date=datetime.strptime(date,"%d/%m/%Y").date()
            tupla=DatoTrafico(airline, carrier_type, passengers_to, passengers_from, freight_to, freight_from, date)
            lista_de_datos.append(tupla)
    return lista_de_datos

def calcula_aerolinea(datos):
    '''
    Calcula las diferentes aerolíneas que existen
    ENTRADA:
        - datos: lista de tuplas de tipo DatoTrafico
    SALIDA:
        - Listado de aerolíneas que prestan servicio
    '''
    todas_aerolineas = {DatoTrafico.airline for DatoTrafico in datos}
    return todas_aerolineas

def filtra_por_aerolinea(datos, aerolinea):
    ''' 
    Calcula el tipo de vuelo y su fecha de una determinada aerolinea
    ENTRADA: 
       - datos: lista de tuplas de tipo DatoTrafico
       - aerolinea: de la que se seleccionarán los registros
    SALIDA: 
       - lista de tuplas (carrier_type, date) seleccionadas

    '''
    lista_aerolinea = [(DatoTrafico.carrier_type, DatoTrafico.date) for DatoTrafico
                       in datos if DatoTrafico.airline==aerolinea]
    return lista_aerolinea

def total_pasajeros_destino_por_aerolinea(datos, aerolinea):
    '''
    Calcula el número total de pasajeros llevados a su destino por una determinada aerolinea
    ENTRADA:
        - datos: lista de tuplas de tipo DatoTrafico
        - aerolinea: de la que se seleccionarán los registros
    SALIDA:
        - Número total de pasajeros llevados a su destino por la aerolinea

    '''
    #pasajeros_aerolinea = [DatoTrafico.passengers_to for DatoTrafico in datos
                           #if DatoTrafico.airline==aerolinea]
    return sum(DatoTrafico.passengers_to for DatoTrafico in datos
                           if DatoTrafico.airline==aerolinea)
    
def top_pasajeros_segun_modalidad_trayecto(datos, trayecto, n):
    '''
    Ordena de mayor a menor los registros de vuelo con más pasajeros llevados a su destino, según la modalidad del trayecto
    ENTRADA:
        - datos: lista de tuplas de tipo DatoTrafico
        - trayecto: modalidad (domestic / foreign) del que se seleccionarán los registros
        - n: número de registros que se mostrarán
    SALIDA:
        - Lista de tuplas (airline, passengers_to, date) ordenadas de mayor a menor número de viajeros
    '''
    top_pasajeros = [(DatoTrafico.airline, DatoTrafico.passengers_to, DatoTrafico.date) for DatoTrafico in datos if trayecto==DatoTrafico.carrier_type]
    return sorted(top_pasajeros, key=lambda x: x[1], reverse=True)

def agrupar_por_aerolinea(datos, filtro=None):
    '''
    Muestra por pantalla el listado de aerolineas que operan, dependiendo si son en territorio nacional (DOMESTIC) o al extranjero (FOREIGN)
    ENTRADA:
        - datos: lista de tuplas de tipo DatoTrafico
        - filtro: variable, según si queremos escoger vuelos nacionales o extranjero. None los muestra todos
    SALIDA:
        - Lista (airline) con los resultados según el filtro
    '''
    dicc_aerol = {}
    for dato in datos:
        if filtro==None or dato.carrier_type==filtro:
            clave = dato.airline
            if clave in dicc_aerol:
                dicc_aerol[clave].append(dato)
            else:
                dicc_aerol[clave] = [dato]
    return dicc_aerol

def contar_vuelos_por_aerolinea(datos):
    '''
    Muestra un listado en pantalla del número de vuelos que ha realizado cada aerolinea durante el periodo
    de tiempo en el que se han recogido los datos del fichero csv
    ENTRADA:
        - datos: lista de tuplas de tipo DatoTrafico
    SALIDA:
        - Diccionario con los resultados por aerolinea
    '''
    dicc_cont = {}
    for dato in datos:
        clave = dato.airline
        if clave in dicc_cont:
            dicc_cont[clave]+=1
        else:
            dicc_cont[clave]=1
    return dicc_cont

def carrier_type_más_carga_destino(datos):
    '''
    Muestra la modalidad de vuelo que más carga ha llevado a destino
    ENTRADA:
        - datos: lista de tuplas de tipo DatoTrafico
    SALIDA:
        - Max valor del diccionario que indica la modalidad de vuelo y la cantidad de vuelos
    '''
    dicc_carr = {}
    for dato in datos:
        if dato.airline in dicc_carr:
            dicc_carr[dato.carrier_type] += dato.freight_to
        else:
            dicc_carr[dato.carrier_type] = dato.freight_to
    return max(dicc_carr.items(), key=lambda x: x[1])

def aerolineas_hasta_india(datos):
    '''
    Muestra de forma ordenada por aerolinea las que más pasajeros han trasladado hasta India
    ENTRADA:
        - datos: lista de tuplas de tipo DatoTrafico
    SALIDA:
        - Diccionario ordenado según número de pasajeros de mayor a menor según cada aerolinea
    '''
    dicc_aerol = {}
    for dato in datos:
        if dato.airline in dicc_aerol:
            dicc_aerol[dato.airline] += dato.passengers_to
        else:
            dicc_aerol[dato.airline] = dato.passengers_to
    return sorted(dicc_aerol.items(), key=lambda x: x[1], reverse=True)

#La función del tipo 14 se corresponde a la ya implementada anteriormente: top_pasajeros_segun_modalidad_trayecto

def grafica_aerolineas_viajeros(datos):
    '''
    Genera una gráfica de barras con el número de vuelos que ha hecho cada aerolinea
    ENTRADA:
        - datos: lista de tuplas de tipo DatoTrafico
    SALIDA:
        - Gráfico de barras con nombre de cada compañía y cantidad de vuelo
    '''
    data = contar_vuelos_por_aerolinea(datos)
    nombre_aerolinea = list(data.keys())
    dato_aerolinea = list(data.values())
    plt.title("Número de vuelos de cada aerolinea")
    plt.plot(nombre_aerolinea, dato_aerolinea)
    plt.show()