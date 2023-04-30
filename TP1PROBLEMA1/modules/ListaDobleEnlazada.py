# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:18:01 2023

@author: alang
"""

class Nodo:
    """
    Clase que representa un nodo de una lista doblemente enlazada.

    Atributos:
    ----------
    dato :  El dato almacenado en el nodo.
    siguiente : El siguiente nodo.
    anterior : El nodo anterior.
    
    """
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
    
    
    def tamanio(self):
        return self.tamanio
    
    
    
    
        #PASOS : creo el nodo 
        #desp enlazo el ahora segundo al nuevo cabeza 
        #enlazo el nuevo al inicio 
    def agregar_al_inicio(self, dato):
        """
        Método que agrega un elemento al inicio de la lista.

        Args:
        - dato: Dato a agregar en la lista.

        """
        nuevo = Nodo(dato, self.cabeza, None)
        if self.cabeza != None:
            self.cabeza.anterior = nuevo
        else:
            self.cola = nuevo
        self.cabeza = nuevo
        self.tamanio += 1
        


        
    def agregar_al_final(self, dato):
        """
        Método que agrega un elemento al final de la lista.

        Args:
        - dato: Dato a agregar en la lista.

        """
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
        """
        Extrae el nodo eque se encuentre en la posición indicada.
        Si no se especifica la posición, se extrae el último nodo de la lista. 

        Args:
        posicion: Es la posición de la que se va a extraer el nodo.
        
        Returns:
            nodoAExtraer: nodo extraído    

        """
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
        """
        Retorna una copia de la lista enlazada actual, creando una nueva 
        instancia de ListaDobleEnlazada. 
        
        Returns
        -------
            listaCopia: una nueva instancia de ListaDobleEnlazada 
            que es una copia de la lista original.   

        """
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
        """
        Invierte la lista doblemente enlazada.
        Se trabaja con tres nodos auxiliares, invirtiendo los enlaces de cada 
        nodo. 

        Returns
        -------
        None.

        """
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

    
    def ordenar(self):   
        """
        Ordena los elementos de la lista en orden ascendente utilizando el 
        algoritmo de ordenamiento por inserción.

        Returns
        -------
        None.

        """    
        if (self.tamanio>3):
            for i in range(self.tamanio):
                aux=self.extraer(i)
                j=0
                nodo=self.cabeza
                while j<=i:
                    if j==i:
                        self.insertar(aux,j)
                        j+=1
                    elif(aux<nodo.dato):
                        self.insertar(aux,j)
                        j=i+1

                    else:
                        nodo=nodo.siguiente
                        j+=1
        elif(self.tamanio == 2):
            if (self.cabeza.dato>self.cola.dato):
                aux=self.cabeza.dato
                self.cabeza.dato=self.cola.dato
                self.cola.dato=aux
        elif(self.tamanio == 3):
            tercero=self.extraer(0)
            self.ordenar()
            if(tercero>=self.cabeza.dato and tercero<self.cola.dato):
                self.insertar(tercero, 1)
            elif (tercero>=self.cola.dato):
                self.agregar_al_final(tercero)
            elif (tercero<self.cabeza.dato):
                self.agregar_al_inicio(tercero)
                        
                    
                        
                
        
    def add(self,Lista):
        """
        Se crea esta funcion para concatenar dos listas doblemente enlazadas.
        Esta funcion es llamada dentro del operador __add__.

        Parameters
        ----------
        Lista : lista doblemente enlazada.

        Returns
        -------
        listaConcatenada 

        """
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
        aux=Lista.cabeza
        while aux != None:
            self.agregar_al_final(aux.dato)
            aux=aux.siguiente

  #ListaSuma = MiLista1 + MiLista2

    def __add__(self, otro): #SOBRECARGA EL +
        """
        Sobrecarga el operador + para que dos objetos de la clase 
        ListaDobleEnlazada puedan concatenarse usando el operador +.

        Parameters
        ----------
        otro : objeto de la clase ListaDobleEnlazada que se va a
        concatenar con el objeto actual.

        Returns
        -------
        ListaDobleEnlazada: nuevo objeto de la clase ListaDobleEnlazada 
        que es la concatenación del objeto actual y el objeto otro.
        """

        return self.add(otro)

    def __str__(self):
        """
        Devuelve una cadena de caracteres que representa la lista doblemente 
        enlazada.     

        Returns
        -------
        linea 

        """
        linea="None "
        for i in self:
            #linea=linea+print(dato) ESTO NO ANDA PORQUE PRINT NO ME DEVUELVE UN STRING
            #PRINT SOLO MUESTRA POR PANTALLA Y DEVUELVE NONETYPE
            linea=linea+str(i)+" "
        linea=linea+"None"
        return linea


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
        actual=self.cabeza
        while actual is not None: 
            yield actual.dato
            actual=actual.siguiente
        
        
    def __len__(self):
        """Devuelve el tamaño de la lista.

        Returns:
            int: Tamaño del objeto.
            
        """
        return self.tamanio