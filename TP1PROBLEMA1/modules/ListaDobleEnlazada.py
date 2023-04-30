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
        
    def __str__(self):
        linea=str(self.dato)
        return linea

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
    def esta_vacia(self):
        return self.tamanio == 0
    def tamanio(self):
        return self.tamanio
    
    
    
    
        #PASOS : creo el nodo 
        #desp enlazo el ahora segundo al nuevo cabeza 
        #enlazo el nuevo al inicio 
    def agregar_al_inicio(self, dato):
        nuevo = Nodo(dato, self.cabeza, None)
        if self.cabeza != None:
            self.cabeza.anterior = nuevo
        else:
            self.cola = nuevo
        self.cabeza = nuevo
        self.tamanio += 1
        


        
    def agregar_al_final(self, dato):
        nuevo = Nodo(dato, None, self.cola)
        if self.cola != None:
            self.cola.siguiente = nuevo
        else:
            self.cabeza = nuevo
            
        self.cola = nuevo
        self.tamanio += 1
        
        

        
    #PASOS:
        #1: me fijo que vaya al inicio o al final.
        #2: me fijo q este en el rango
        #3: tengo que ir desde el cabeza a la posicion 
        #4: YA TENGO LA POSICION. Ahora creo el nuevo nodo y lo enlazo
        #COMO LO ENLAZO: 
        
    def insertar(self,dato, posicion=None):
        if posicion == None:
            self.agregar_al_final(dato)
        elif posicion == 0:
            self.agregar_al_inicio(dato)
        elif 0<posicion<self.tamanio:
            actual = self.cabeza
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
        retornar = None
        if posicion == None:
            if self.tamanio>1:
                retornar=self.cola.dato
                self.cola=self.cola.anterior;
                self.cola.siguiente=None;
            elif self.tamanio == 1:
                retornar=self.cola.dato
        elif posicion < 0 and self.tamanio > 1:
            if -posicion<self.tamanio-1 and posicion != -1:
                aux=self.cola
                for i in range(-posicion-1):
                    aux=aux.anterior
                retornar=aux.dato
                aux.anterior.siguiente=aux.siguiente
                aux.siguiente.anterior=aux.anterior
            elif -posicion==self.tamanio-1:
                retornar=self.cabeza.dato
                self.cabeza.siguiente.anterior=None
                self.cabeza=self.cabeza.siguiente
            elif -posicion == 1:
                retornar=self.cola.dato
                self.cola.anterior.siguiente=None
                self.cola=self.cola.anterior
        elif posicion < 0 and self.tamanio == 1 and -posicion == 1:
            retornar=self.cabeza.dato
        elif posicion == 0 and self.tamanio>1:
            aux=self.cabeza
            self.cabeza.siguiente.anterior=None
            self.cabeza=self.cabeza.siguiente
            retornar=aux.dato
        elif posicion == 0 and self.tamanio == 1:
            retornar=self.cabeza.dato
        elif 0<posicion<self.tamanio-1 and self.tamanio>1:
            actual = self.cabeza
            for i in range(posicion):
                actual = actual.siguiente
            actual.anterior.siguiente=actual.siguiente
            actual.siguiente.anterior=actual.anterior
            retornar=actual.dato
        elif (posicion == 1 or posicion == 0) and self.tamanio == 1:
            retornar=self.cabeza.dato
        elif posicion == self.tamanio-1:
            retornar=self.cola.dato
            self.cola=self.cola.anterior;
            self.cola.siguiente=None;
        if retornar is not None:
            self.tamanio=self.tamanio-1
            if self.tamanio == 0:
                self.cola=None
                self.cabeza=None
        return retornar
                
        
    def copiar(self):
        copia=ListaDobleEnlazada()
        actual=self.cabeza
        if actual == None:
            return copia
        while actual.siguiente != None:
            copia.agregar_al_final(actual.dato)
            actual=actual.siguiente
        copia.agregar_al_final(actual.dato)
        return copia
    #return self ESTO ME RETORNA LA MISMA LISTA Y SI MODIFICO LA NUEVA ASIGNACION SE MODIFICA ESTA TAMBIEN 
            
    
        
        
        
    def invertir(self):
        aux0=self.cabeza
        aux1=self.cabeza.siguiente
        aux2=self.cabeza.siguiente.siguiente
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
        aux=self.cola
        self.cola=self.cabeza
        self.cabeza=aux
        
    # def ordenar(self):
    #     if self.tamanio<2:
    #         return
    #     actual = self.cabeza
    #     while actual is not None:
    #         aux = actual.siguiente
    #         while aux is not None:
    #             if aux.dato < actual.dato:
    #                 aux1=actual.dato
    #                 actual.dato = aux.dato
    #                 aux.dato=aux1
    #                 aux = aux.siguiente
    #             else:
    #                 aux=aux.siguiente
                
    #         actual=actual.siguiente
    
    def ordenar(self):    #ACA CREO QUE LO HICE POR INSERCION
        for i in range(self.tamanio):
            aux=self.extraer(i)
            j=0
            nodo=self.cabeza
            while j<=i:
                if(aux<nodo.dato):
                    self.insertar(aux,j)
                    j=i+1
                elif j==i:
                    self.insertar(aux,j)
                    j+=1
                else:
                    nodo=nodo.siguiente
                    j+=1
                    
                        
                    
                        
                
        
    def add(self,Lista):
        #PREGUNTA: ESTO FUNCIONA??
        #Lista.cabeza.anterior=self.cola
        #self.cola.siguiente=Lista.cabeza
        #OPCION 2
        concatenada=ListaDobleEnlazada()
        aux=self.cabeza
        while aux != None:
            concatenada.agregar_al_final(aux.dato)
            aux=aux.siguiente
        aux=Lista.cabeza
        while aux != None:
            concatenada.agregar_al_final(aux.dato)
            aux=aux.siguiente
        return concatenada

    def concatenar(self,Lista):
        aux=Lista.cabeza
        while aux != None:
            self.agregar_al_final(aux.dato)
            aux=aux.siguiente

  #ListaSuma = MiLista1 + MiLista2

    def __add__(self, otro): #SOBRECARGA EL +
        return self.add(otro)

    def __str__(self):
       linea="None "
       for i in self:
           #linea=linea+print(dato) ESTO NO ANDA PORQUE PRINT NO ME DEVUELVE UN STRING
           #PRINT SOLO MUESTRA POR PANTALLA Y DEVUELVE NONETYPE
           linea=linea+str(i)+" "
       linea=linea+"None"
       return linea


    def __iter__(self):
        actual=self.cabeza
        while actual is not None: 
            yield actual.dato
            actual=actual.siguiente
        
        
    def __len__(self):
        return self.tamanio