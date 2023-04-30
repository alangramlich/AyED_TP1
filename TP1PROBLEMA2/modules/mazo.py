# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:16:05 2023

@author: Priscila
"""
import sys
import os
ruta_actual = os.getcwd()
ruta_actual = ruta_actual[:-9]
ruta_actual +="1\modulos"
sys.path.append(ruta_actual)
from modulos.ListaDobleEnlazada import ListaDobleEnlazada

class Mazo:
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
        Retorna True si la lista está vacía y False si contiene algún elemento.

        Returns
        -------
        retornar : variable de tipo booleana que indica si una lista está vacía
        o no.

        """
        retornar = True
        if self.lista.tamanio != 0:
            retornar = False
        return retornar
    
    def agregar(self,dato):
        """
        Agrega un dato al final del mazo.

        Parameters
        ----------
        dato : dato a agregar en el mazo.

        Returns
        -------
        None.

        """
        self.lista.agregar_al_final(dato)
        
    def avanzar(self):
        """
        Extrae y devuelve el primer elemento del mazo.
        
        Returns
        -------
        Si el mazo está vacío la función devuelve None.

        """
        return self.lista.extraer(0)
    
    def tamanio(self):
        """
        Retorna el tamaño del mazo.

        Returns
        -------
        tamanio: la cantidad de datos que tiene el mazo.

        """
        return self.lista.tamanio
    
    def __str__(self):
        """
        Devuelve una cadena de caracteres que representa el estado actual del
        mazo.
        La cadena comienza con la palabra "Piso" y luego se agregan los elementos 
        de la pila desde el fondo hasta el tope. Finalmente, se agrega la palabra 
        "Tope" al final de la cadena.
        Returns
        -------
        linea : cadena resultante.

        """
        linea = "Piso"
        for i in self.lista:
            linea = linea + str(i) + ","
        linea = linea[:-1]
        linea = linea + "Tope"
        return linea
    
    def __iter__(self):
        """
        Define un iterador que permite recorrer la pila y extraer sus elementos
        en orden de último en entrar.
        Utiliza un generador que itera sobre la pila y extrae los elementos 
        mediante la función desapilar hasta que la pila esté vacía. Cada vez 
        que se extrae un elemento se usa la sentencia yield para devolverlo al 
        iterador, de modo que el ciclo que recorre el mazo pueda continuar su 
        ejecución.

        Returns
        ------

        """
        while self.esta_vacia() is not True:
            yield self.desapilar()
        
        
      
   
    