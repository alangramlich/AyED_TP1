# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 19:46:59 2023

@author: Priscila
"""
class Nodo:
    """
    Clase que representa un nodo de una lista doblemente enlazada.

    Atributos:
    ----------
    dato :  El dato almacenado en el nodo.
    siguiente : El siguiente nodo en la lista enlazada.
    anterior : El nodo anterior en la lista enlazada.
    
    """
    def __init__(self, dato=None, siguiente=None, anterior=None):
        """
        Inicializa un nuevo objeto Nodo.

        Parameters:
        ----------
        dato : El valor del dato que se almacenará en el nodo, por defecto None.
        siguiente : El siguiente nodo en la lista enlazada, por defecto None.
        anterior : El nodo anterior en la lista enlazada, por defecto None.
        
        """
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

    def obtenerDato(self):
        """
        Devuelve el dato almacenado en el nodo.

        Returns:
        ----------
        dato: El dato almacenado en el nodo.
        """
        return self.dato

    def obtenerSiguiente(self):
        """
        Devuelve el siguiente nodo en la lista enlazada.

        Returns:
        ----------
        Nodo: El siguiente nodo en la lista enlazada.
        """
        return self.siguiente
    
    def asignarDato(self, nuevoDato):
        """
        Asigna un nuevo valor de dato al nodo.

        Parameters:
        ----------
        nuevoDato : Es el nuevo valor del dato a asignar.
        
        """
        self.dato = nuevoDato
    
    def asignarSiguiente(self, nuevoSiguiente):
        """
        Asigna un nuevo nodo siguiente al nodo actual.

        Parameters:
        ----------
        nuevoSiguiente : El nuevo nodo siguiente a asignar.
        
        """
        self.siguiente = nuevoSiguiente
        
    def __str__(self):
        """
        Devuelve una cadena que representa el nodo.

        Returns:
        ----------
        linea: La cadena que representa el nodo.
        """
        linea = str(self.dato)
        return linea
