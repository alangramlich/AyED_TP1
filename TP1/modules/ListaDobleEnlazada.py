# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 20:23:51 2023

@author: alang
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:18:01 2023

@author: alang
"""
from modules.Nodo import Nodo

class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0
    def esta_vacia(self):
        return self.tamanio == 0
    def tamanio(self):
        return self.tamanio
    
    
    
    
    
        #PASOS : creo el nodo 
        #desp enlazo el ahora segundo al nuevo primero 
        #enlazo el nuevo al inicio 
    def agregar_al_inicio(self, dato):
        nuevo = Nodo(dato, self.primero, None)
        if self.primero != None:
            self.primero.anterior = nuevo
        else:
            self.ultimo = nuevo
        self.primero = nuevo
        self.tamanio += 1
        


        
    def agregar_al_final(self, dato):
        nuevo = Nodo(dato, None, self.ultimo)
        if self.ultimo != None:
            self.ultimo.siguiente = nuevo
        else:
            self.primero = nuevo
            
        self.ultimo = nuevo
        self.tamanio += 1
        
        

        
    #PASOS:
        #1: me fijo que vaya al inicio o al final.
        #2: me fijo q este en el rango
        #3: tengo que ir desde el primero a la posicion 
        #4: YA TENGO LA POSICION. Ahora creo el nuevo nodo y lo enlazo
        #COMO LO ENLAZO: 
        
    def insertar(self,dato, posicion=None):
        if posicion == None:
            self.agregar_al_final(dato)
        elif posicion == 0:
            self.agregar_al_inicio(dato)
        elif 0<posicion<self.tamanio:
            actual = self.primero
            for i in range(posicion):
                actual = actual.siguiente
            nuevo = Nodo(dato, actual, actual.anterior)
            actual.anterior.siguiente = nuevo
            actual.anterior = nuevo
            self.tamanio += 1
        else:
            self.agregar_al_final(dato)
            
        
    #Esto es parecido a lo anterior, solo que no tengo un nuevo para enlazar.
    #tengo que posicionarme en el que quiero borrar y desde ahi cambiar los enlaces
    #hacia adelante y hacia atras
    def extraer(self, posicion=None):
        if posicion == None:
            retornar=self.ultimo
            self.ultimo.anterior.siguiente=None;
            self.ultimo=self.ultimo.anterior;
            self.tamanio=self.tamanio-1
        elif posicion == 0:
            aux=self.primero
            aux.siguiente.anterior=None
            retornar=aux
        elif 0<posicion<self.tamanio:
            actual = self.primero
            for i in range(posicion):
                actual = actual.siguiente
            
            actual.anterior.siguiente=actual.siguiente
            actual.siguiente.anterior=actual.anterior
            retornar=actual
            self.tamanio=self.tamanio-1
        return retornar
                
        
    def copiar(self):
        copia=ListaDobleEnlazada()
        actual=self.primero
        while actual.siguiente != None:
            copia.agregar_al_final(actual.dato)
            actual=actual.siguiente
        copia.agregar_al_final(actual.dato)
        return copia
            
    
        
        
        
    def invertir(self):
        aux0=self.primero
        aux1=self.primero.siguiente
        aux2=self.primero.siguiente.siguiente
        aux0.siguiente=None
        aux0.anterior=aux1
        aux1.siguiente=aux0
        aux1.anterior=aux2
        aux0=aux1
        aux1=aux2
        aux2=aux2.siguiente
        
        for i in range(self.tamanio-3):
            aux1.siguiente=aux0
            aux1.anterior=aux2
            aux0=aux1
            aux1=aux2
            aux2=aux2.siguiente
            
        aux1.anterior=None
        aux1.siguiente=aux0
        aux=self.ultimo
        self.ultimo=self.primero
        self.primero=aux
        
    def ordenar(self):
        if self.tamanio<2:
            return
        actual = self.primero
        while actual is not None:
            aux = actual.siguiente
            while aux is not None:
                if aux.dato < actual.dato:
                    aux1=actual.dato
                    actual.dato = aux.dato
                    aux.dato=aux1
                    aux = aux.siguiente
                else:
                    aux=aux.siguiente
                
            actual=actual.siguiente
        
        
    def concatenar(self,Lista):
        #PREGUNTA: ESTO FUNCIONA??
        #Lista.primero.anterior=self.ultimo
        #self.ultimo.siguiente=Lista.primero
        #OPCION 2
        concatenada=ListaDobleEnlazada()
        aux=self.primero
        while aux != None:
            concatenada.agregar_al_final(aux.dato)
            aux=aux.siguiente
        aux=Lista.primero
        while aux != None:
            concatenada.agregar_al_final(aux.dato)
            aux=aux.siguiente
        return concatenada




  #ListaSuma = MiLista1 + MiLista2

    def __add__(self, otro):
        return self.concatenar(otro)


