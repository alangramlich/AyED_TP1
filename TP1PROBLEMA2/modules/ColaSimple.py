# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 15:46:35 2023

@author: alang
"""
import sys
import os
ruta_actual = os.getcwd()
ruta_actual=ruta_actual[:-9]
ruta_actual+="1\modules"
sys.path.append(ruta_actual)
from ListaDobleEnlazada import *

class ColaSimple:
    def __init__(self):
        """
        Constructor de la clase que inicializa el atributo 'lista' como una 
        instancia de la clase 'ListaDobleEnlazada'
        Returns
        -------
        None.
        """
        self.lista = ListaDobleEnlazada()
        
    def esta_vacia(self):
        """
        Retorna True si la cola está vacía y False si contiene algún elemento.
        Returns
        -------
        retornar : variable de tipo bool que indica si la cola está vacía
        o no.
        """
        retornar = True
        if self.lista.tamanio is not 0:
            retornar = False
        return retornar
        
    def agregar(self, dato):
        """
       Agrega un dato al final de la lista.
       Parameters
       ----------
       dato : dato a agregar en la lista.
       Returns
       -------
       None.
       """
        self.lista.agregar_al_final(dato)
        
    def avanzar(self):
        """
       Extrae y devuelve el primer elemento de la cola.
       
       Returns
       -------
       Si el mazo está vacío la función devuelve None.
       """
        return self.lista.extraer(0)
        
    
    def tamanio(self):
        """
        Retorna el tamaño de la cola.
        Returns
        -------
        tamanio: la cantidad de datos que tiene la cola.
        """
        return self.lista.tamanio
    
