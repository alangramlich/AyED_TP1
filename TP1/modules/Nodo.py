# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:24:42 2023

@author: alang
"""

class Nodo:
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente