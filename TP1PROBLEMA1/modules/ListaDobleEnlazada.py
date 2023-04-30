# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:38:45 2023

@author: Priscila
"""

from modulos.Nodo import Nodo 
"""
Módulo que contiene la clase Nodo.

La clase Nodo representa un nodo.

"""
class ListaDobleEnlazada:
    """
    Clase que representa una lista doblemente enlazada.
    """

    def __init__(self):
        """
        Constructor de la clase ListaDobleEnlazada.

        Args:
        - No recibe argumentos.
        
        Returns:
        - No retorna valores
        
        Descripción:
        - Inicializa los atributos cabeza, cola y tamanio.
        """
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
        
    def __iter__(self):
        """
        Método que permite la iteración de los elementos de la lista.

        Args:
        - No recibe argumentos.

        Returns:
        - Yield: Retorna los valores de los nodos de la lista.

        Descripción:
        - Recorre la lista y retorna los valores de los nodos a medida que los encuentra.
        """
        nodoActual = self.cabeza
        while nodoActual is not None:
            yield nodoActual.dato
            nodoActual = nodoActual.siguiente
     
    def esta_vacia(self):
        """
        Método que determina si la lista está vacía.Comprueba si el tamanio es 
        igual a 0. Si es así, devuelve True, indicando que la lista está vacía
        y en caso contrario, devuelve False.
    
        Args:
        - No recibe argumentos.

        Returns:
        - bool: devuelve True si la lista está vacía, False en caso contrario.

        """
        return self.tamanio == 0
   
    def agregar_al_inicio(self,dato):
        """
        Método que agrega un elemento al inicio de la lista.

        Args:
        - dato: Dato a agregar en la lista.

        """
        nuevoNodo = Nodo(dato, self.cabeza, None)
        if self.cabeza != None:
             self.cabeza.anterior = nuevoNodo
        else:
            self.cola = nuevoNodo
        self.cabeza = nuevoNodo
        self.tamanio += 1
           
    def agregar_al_final(self, dato):
        """
        Método que agrega un elemento al final de la lista.

        Args:
        - dato: Dato a agregar en la lista.

        """
        nodoAAgregar = Nodo(dato, None, self.cola)
        if self.cola != None:
            self.cola.siguiente = nodoAAgregar
        else:
            self.cabeza = nodoAAgregar    
       
        self.cola = nodoAAgregar
        self.tamanio += 1
        
    def insertar(self,dato, posicion=None):
        """
        Inserta un nuevo nodo en la posición indicada.
        Si no se especifica la posición, se agrega al final de la lista. Si la
        posición es 0, se agrega al inicio de la lista. 

        Args:
        dato: Es el dato que se va a almacenar en el nuevo nodo.
        posicion: Es la posición en la que se va a insertar el nuevo nodo.

        """
        if posicion == None:
           self.agregar_al_final(dato)
     
        elif posicion == 0:
           self.agregar_al_inicio(dato)
      
        elif 0 < posicion < self.tamanio:
           nodoActual = self.cabeza
           for i in range(posicion):
               nodoActual = nodoActual.siguiente
           nuevoNodo = Nodo(dato, nodoActual, nodoActual.anterior)
           nodoActual.anterior.siguiente = nuevoNodo
           nodoActual.anterior = nuevoNodo
           self.tamanio += 1
        else:
           self.agregar_al_final(dato)
    
    def __len__(self):
        """Devuelve el tamaño de la lista.

        Returns:
            int: Tamaño del objeto.
            
        """
        return self.tamanio


    def extraer(self, posicion = None):
        """
        Extrae el nodo eque se encuentre en la posición indicada.
        Si no se especifica la posición, se extrae el último nodo de la lista. 

        Args:
        posicion: Es la posición de la que se va a extraer el nodo.
        
        Returns:
            nodoAExtraer: nodo extraído    

        """
        nodoAExtraer = None
        
        if posicion == None:
            if self.tamanio > 1:
                nodoAExtraer = self.cola.dato
                self.cola = self.cola.anterior
                self.cola.siguiente = None
            elif self.tamanio == 1:
                nodoAExtraer = self.cola.dato
                
        elif posicion < 0 and self.tamanio > 1:
            if -posicion < self.tamanio-1 and posicion != -1:
                nodoAux = self.cola
                for i in range (-posicion-1):
                    nodoAux = nodoAux.anterior
                nodoAExtraer = nodoAux.dato
                nodoAux.anterior.siguiente = nodoAux.siguiente
                nodoAux.siguiente.anterior = nodoAux.anterior   
            
            elif -posicion == self.tamanio -1:
                nodoAExtraer = self.cabeza.dato
                self.cabeza.siguiente.anterior = None
                self.cabeza = self.cabeza.siguiente
            
            elif -posicion == 1:
               nodoAExtraer = self.cola.dato
               self.cola.anterior.siguiente = None
               self.cola = self.cola.anterior
       
        elif posicion < 0 and self.tamanio == 1 and -posicion == 1:
            nodoAExtraer = self.cabeza.dato
        
        elif posicion == 0 and self.tamanio > 1:
            nodoAux = self.cabeza
            self.cabeza.siguiente.anterior = None
            self.cabeza = self.cabeza.siguiente
            nodoAExtraer = nodoAux.dato
       
        elif posicion == 0 and self.tamanio == 1:
           nodoAExtraer = self.cabeza.dato     
            
        elif 0 < posicion < self.tamanio-1 and self.tamanio > 1:
            nodoActual = self.cabeza
            for i in range(posicion):
                nodoActual = nodoActual.siguiente
            nodoActual.anterior.siguiente = nodoActual.siguiente
            nodoActual.siguiente.anterior = nodoActual.anterior
            nodoAExtraer = nodoActual.dato
            
        elif (posicion == 1 or posicion == 0) and self.tamanio == 1:
            nodoAExtraer = self.cabeza.dato
        
        elif posicion == self.tamanio - 1:
            nodoAExtraer = self.cola.dato
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        
        if nodoAExtraer is not None:
            self.tamanio = self.tamanio - 1
            if self.tamanio == 0:
                self.cola = None
                self.cabeza = None
        
        return nodoAExtraer
               
    def copiar(self):
        """
        Retorna una copia de la lista enlazada actual, creando una nueva 
        instancia de ListaDobleEnlazada. 
        
        Returns
        -------
            listaCopia: una nueva instancia de ListaDobleEnlazada 
            que es una copia de la lista original.   

        """
        listaCopia = ListaDobleEnlazada()
        listaActual = self.cabeza
        if listaActual == None:
            return listaCopia
        while listaActual.siguiente != None:
            listaCopia.agregar_al_final(listaActual.dato)
            listaActual = listaActual.siguiente
        listaCopia.agregar_al_final(listaActual.dato)
        return listaCopia
    
    def invertir(self):
        """
        Invierte la lista doblemente enlazada.
        Se intercambian los enlaces del primer nodo con el último, 
        los del segundo con el penúltimo, y así sucesivamente, 
        hasta invertir todos los nodos.

        Returns
        -------
        None.

        """
        nodoAux0 = self.cabeza
        nodoAux1 = self.cabeza.siguiente
        nodoAux2 = self.cabeza.siguiente.siguiente
        nodoAux0.siguiente = None
        nodoAux0.anterior = nodoAux1
        nodoAux1.siguiente = nodoAux0
        nodoAux1.anterior = nodoAux2
        nodoAux0 = nodoAux1
        nodoAux1 = nodoAux2
        nodoAux2 = nodoAux2.siguiente
       
        for i in range (self.tamanio -3):
           nodoAux1.siguiente = nodoAux0
           nodoAux1.anterior = nodoAux2
           nodoAux0 = nodoAux1
           nodoAux1 = nodoAux2
           nodoAux2 = nodoAux2.siguiente
           
        nodoAux1.anterior = None
        nodoAux1.siguiente = nodoAux0
        nodoAux = self.cola
        self.cola = self.cabeza
        self.cabeza = nodoAux

    def ordenar(self):
        """
        Ordena los elementos de la lista en orden ascendente utilizando el 
        algoritmo de ordenamiento por inserción.

        Returns
        -------
        None.

        """
        for i in range(self.tamanio):
            nodoAux = self.extraer(i)
            j = 0
            nodo = self.cabeza
            while j <= i:
                if nodoAux < nodo.dato:
                    self.insertar(nodoAux,j)
                    j = i + 1
                elif j == i:
                    self.insertar(nodoAux,j)
                    j += 1
                else:
                    nodo = nodo.siguiente
                    j += 1

    def concatenar(self, Lista):
        """
        Toma como parámetro otra lista doblemente enlazada llamada Lista y 
        agrega los nodos de esta lista al final de la lista actual.
        
        Parameters
        ----------
        Lista : lista doblemente enlazada que se desea concatenar a la 
        lista actual.

        Returns
        -------
        None.

        """
        nodoAux = Lista.cabeza
        while nodoAux != None:
            self.agregar_al_final(nodoAux.dato)
            nodoAux = nodoAux.siguiente
    
    def __add__(self, Lista):
        """
        Se sobrecarga para permitir la concatenación de dos objetos de tipo 
        ListaDobleEnlazada. En la primera implementación, se crea una nueva 
        lista concatenando los elementos de la lista actual y la lista pasada 
        como argumento. En la segunda implementación, se llama a la función 
        add para añadir un nuevo nodo a la lista. 

        Parameters
        ----------
        Lista : lista doblemente enlazada.

        Returns
        -------
        listaConcatenada 

        """
        listaConcatenada = ListaDobleEnlazada()
        nodoAux = self.cabeza
        while nodoAux != None:
            listaConcatenada.agregar_al_final(nodoAux.dato)
            nodoAux = nodoAux.siguiente
        return listaConcatenada

    def __add__(self, otroNodo):
        """
        Sobrecarga el operador + para que dos objetos de la clase 
        ListaDobleEnlazada puedan concatenarse usando el operador +.

        Parameters
        ----------
        otroNodo : objeto de la clase ListaDobleEnlazada que se va a
        concatenar con el objeto actual.

        Returns
        -------
        ListaDobleEnlazada: nuevo objeto de la clase ListaDobleEnlazada 
        que es la concatenación del objeto actual y el objeto otroNodo.

        """
        return self.add(otroNodo)
    
    def __str__(self):
        """
        Devuelve una cadena de caracteres que representa la lista doblemente 
        enlazada.     

        Returns
        -------
        linea 

        """
        linea = "None"
        for i in self:
            linea = linea + str(i) + " "
        linea = linea + "None"
        return linea
   