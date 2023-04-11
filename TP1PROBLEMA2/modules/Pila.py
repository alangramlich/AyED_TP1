# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:09:18 2023

@author: alang
"""

import sys
sys.path.append("C:/REPOSITORIOS/Algoritmos-y-estructuras-de-datos/TP1PROBLEMA1")
from modules.ListaDobleEnlazada import *

class Pila:
    def __init__(self):
        self.lista = ListaDobleEnlazada()
        
    def esta_vacia(self):
        retornar = True
        if self.lista.tamanio is not 0:
            retornar = False
        return retornar
        
    def apilar(self, dato):
        self.lista.agregar_al_final(dato)
        
    def desapilar(self):
        return self.lista.extraer()
        
    def ver_tope(self):
        if self.esta_vacia():
            raise ValueError("La pila está vacía")
        return self.lista.cola.dato
    
    def tamanio(self):
        return self.lista.tamanio
    
    def __str__(self):
        linea="PISO"
        for i in self.lista:
            #linea=linea+print(dato) ESTO NO ANDA PORQUE PRINT NO ME DEVUELVE UN STRING
            #PRINT SOLO MUESTRA POR PANTALLA Y DEVUELVE NONETYPE
            linea=linea+str(i)+","
        linea=linea[:-1]
        linea=linea+"TOPE"
        return linea
    
    def __iter__(self):
        while self.esta_vacia() is not True: 
            yield self.desapilar()
            