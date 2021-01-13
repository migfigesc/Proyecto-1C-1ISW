# -*- coding: utf-8 -*-

'''
Created on 22 nov. 2020

@author: Miguel Figueroa
'''

from trafico_aereo import *

################################################################
#  Funciones auxiliares
################################################################
def mostrar_numerado(coleccion):
    for p, dato in enumerate(coleccion):
        print(p, dato)
        
        
################################################################
#  Funciones de test
################################################################

def test_lee_datos_trafico():
    print("Leidos" , len (DATOS), "datos del tráfico aéreo de India")
    mostrar_numerado(DATOS)
    #print(DATOS)  
    
def test_calcula_aerolinea():
    aerolineas = calcula_aerolinea(DATOS)
    print("Aerolineas")
    print("Leidas" , len (aerolineas), "aerolíneas distintas")
    mostrar_numerado(aerolineas)   
    
def test_filtra_por_aerolinea():         # Test de la filtra_por_pais
    aerolinea_es = filtra_por_aerolinea(DATOS, "SINGAPORE AIRLINES")
    print("Vuelos de Singapore Airlines")
    print("Leídas" , len (aerolinea_es), "datos de vuelos de Singapore Airlines")
    mostrar_numerado(aerolinea_es)
    
def test_total_pasajeros_destino_por_aerolinea():
    aerolinea_to = total_pasajeros_destino_por_aerolinea(DATOS, "SINGAPORE AIRLINES")
    print("Se han llevado", aerolinea_to, "pasajeros a su destino con SINGAPORE AIRLINES")

def test_top_pasajeros_segun_modalidad_trayecto():
    n = 2
    trayecto = "FOREIGN" #puede ser FOREIGN o DOMESTIC
    top_pasajeros = top_pasajeros_segun_modalidad_trayecto(DATOS, trayecto, n)
    mostrar_numerado(top_pasajeros[:n])
    
def test_aerolinea_mas_pasajeros_destino():
    top_aerolinea = aerolinea_mas_pasajeros_destino(DATOS)
    mostrar_numerado(top_aerolinea)
    
def test_agrupar_por_aerolinea():
    filtro = "DOMESTIC" #puede ser FOREIGN o DOMESTIC
    agrup_aerolinea = agrupar_por_aerolinea(DATOS, filtro)
    print("Mostrando listado de aerolineas que operan en vuelos de tipo", filtro)
    mostrar_numerado(agrup_aerolinea)
    
def test_contar_vuelos_por_aerolinea():
    d = contar_vuelos_por_aerolinea(DATOS)
    for clave, valor in d.items():
        print(clave, "-->", valor)
        
def test_carrier_type_más_carga_destino():
    d = carrier_type_más_carga_destino(DATOS)
    print(f" La modalidad de vuelo que más carga ha llevado a su destino es {d}")    
    
def test_aerolineas_hasta_india():
    d = aerolineas_hasta_india(DATOS)
    print("Aerolineas que más pasajeros han llevado hasta India:")
    mostrar_numerado(d)
    
def test_grafica_aerolineas_viajeros():
    grafica_aerolineas_viajeros(DATOS)
    print()
################################################################
#  Programa principal
################################################################
if __name__ == '__main__':
        DATOS = lee_datos_trafico ('../data/airTrafficIndia.csv')
        
        #test_lee_datos_trafico()
        #test_calcula_aerolinea()
        #test_filtra_por_aerolinea()
        #test_total_pasajeros_destino_por_aerolinea()
        #test_top_pasajeros_segun_modalidad_trayecto()
        #test_aerolinea_mas_pasajeros_destino()
        #test_agrupar_por_aerolinea()
        #test_contar_vuelos_por_aerolinea()
        #test_carrier_type_más_carga_destino()
        #test_aerolineas_hasta_india()
        test_grafica_aerolineas_viajeros()
        
#FECHA ÚLTIMA REVISIÓN: 10/01/2020