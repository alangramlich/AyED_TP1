# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 09:38:14 2023

@author: Priscila
"""
import sys
sys.path.append("C:/algoritmosYEstructuraDeDatos/practica/TPN1/problema1")
import random
import os
from modulos.carta import Carta
from modulos.mazo import Mazo
from modulos.ListaDobleEnlazada import ListaDobleEnlazada

def limpiar_consola():
    """
    Borra la pantalla de la consola en función del sistema operativo. 
    Si el sistema operativo es Windows (nt), utiliza el comando "cls" 
    para limpiar la pantalla. De lo contrario, utiliza el comando "clear".

    Returns
    -------
    None.

    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'] 
palos = ['♠', '♥', '♦', '♣']

def comparar_letra_valor(valor):
    """
    Toma un valor de carta representado como una cadena de caracteres y 
    devuelve su equivalente numérico. Si el valor de la carta es una letra 
    (J, Q, K o A), se le asigna un valor numérico correspondiente y se 
    convierte en entero. El valor numérico de las demás cartas se convierte 
    directamente a entero y se devuelve.

    Parameters
    ----------
    valor : una cadena de caracteres que representa el valor de una carta.

    Returns
    -------
    valor : un entero que representa el valor de la carta

    """
    if valor == 'J':
        valor = 11
    if valor == 'Q':
        valor = 12
    if valor == 'K':
        valor = 13
    if valor == 'A':
        valor = 14    
    valor = int(valor)
    return valor

class Carta:
    def __init__(self ,valor, palo):
        """
        Es el constructor de la clase.

        Parameters
        ----------
        valor : valor entero de la carta.
        palo : palo de la carta.

        Returns
        -------
        None.

        """
        [self.valor, self.palo] = [valor, palo]

    def __eq__(self, otro):
        """
        Compara si el valor del objeto actual es igual al valor del objeto 'otro'.

        Parameters
        ----------
        otro : objeto de la misma clase.

        Returns
        -------
        bool: True si los valores son iguales, False si son diferentes

        """
        return self.valor == otro.valor
    
    def __lt__(self, otro):
        """
        Compara dos cartas del mazo por su valor.

        Parameters
        ----------
        otro : valor de la carta con el que se compara de la carta actual .

        Returns
        -------
        bool: True si la carta actual tiene un valor menor que la carta a comparar,
        False en caso contrario.

        """
        valorComparable1 = comparar_letra_valor(self.valor)
        valorComparable2 = comparar_letra_valor(otro.valor)
        return valorComparable1 < valorComparable2
    
    def __str__(self):
        """
        Retorna un string que representa una carta.

        Returns
        -------
        linea 

        """
        linea = "["
        linea = linea + str(self.valor) + str(self.palo)
        linea = linea + "]"
        return linea
    
    def __bool__(self):
        """
        Devuelve True si el atributo 'valor' del objeto es distinto de None, 
        False en caso contrario.

        """
        return self.valor is not None

class JuegoGuerra:
    def __init__(self, p_semilla = 0):
        """
        Es el constructor de la clase. 
        Se define el comportamiento inicial de un objeto de la clase Random.

        Parameters
        ----------
        p_semilla : se utiliza para inicializar el generador de números 
        aleatorios.Si no se especifica, su valor predeterminado es 0.

        Returns
        -------
        None.

        """
        self.semilla = p_semilla

    def inicializar_mazo(self):
        """
        Inicializa todas las variables del juego de cartas y mezcla las cartas
        en el mazo.
        Crea una lista de tuplas que contienen el valor y el palo de cada carta
        del mazo.
        Se crean dos variables booleanas par y impar para controlar la asignación
        de cartas a los dos mazos.
        Se crea un objeto Carta para cada carta en la lista mazo y se agrega al
        mazo correspondiente según corresponda.

        Returns
        -------
        None.

        """
        self.turnosJugados = 0
        mazo = [(valor, palo) for valor in valores for palo in palos]
        random.seed(self.semilla)
        random.shuffle(mazo)
        par = True
        self.auxiliar1 = Mazo()
        self.auxiliar2 = Mazo()
        self.mazo1 = Mazo()
        self.mazo2 = Mazo()
        for carta in mazo:
            auxiliar = Carta(carta[0], carta[1])
            if par is False:
                self.mazo1.agregar_al_inicio(auxiliar)
                par = not par
            else:
                self.mazo2.agregar_al_inicio(auxiliar)
                par = not par

        self.mazoGuerraJugador1 = []
        self.mazoGuerraJugador2 = []
        self.mazoEnMesa = Mazo()
        self.mazoEnGuerra = Mazo()
        self.jugadorGanador = None
        self.memoria_x = ""
       
    def agregar_al_inicio(self,valorCarta):
        """
        Crea una nueva Carta con valorCarta, la cual se convierte en la nueva 
        cabeza del mazo. Si ya había una cabeza, se establece la nueva carta 
        como su carta anterior. Si no había cabeza, la nueva carta también es 
        la cola.
        Se incrementa en uno el tamaño del mazo.

        Parameters
        ----------
        valorCarta :valor de la carta a agregar al inicio

        Returns
        -------
        None.

        """
        nuevaCarta = Carta(valorCarta, self.cabeza,None)
        if self.cabeza != None:
             self.cabeza.anterior = nuevaCarta
        else:
            self.cola = nuevaCarta
        self.cabeza = nuevaCarta
        self.tamanioMazo += 1
    
    def iniciar_juego(self):
        """
        Inicia el juego mezclando las cartas del mazo, y luego inicia el ciclo 
        del juego en el que los jugadores juegan sus cartas hasta que uno de 
        ellos gane.

        Returns
        -------
        None.

        """
        self.inicializar_mazo()
        while (self.jugadorGanador is None):
            self.jugar_carta()
            
    def sacar_cartas(self):
        """
        Toma dos cartas del principio de cada mazo y las devuelve en una lista. 
        Si uno de los mazos se queda sin cartas, se asigna un ganador. 
        
        Returns
        -------
        list: Una lista de dos cartas tomadas del principio de cada mazo.

        """
        if self.mazo1.esta_vacia():
           self.jugadorGanador = "Jugador 2 es el ganador"
           
        elif self.mazo2.esta_vacia():
           self.jugadorGanador = "Jugador 1 es el ganador"
       
        if self.jugadorGanador is None:
           return [self.mazo1.avanzar(), self.mazo2.avanzar()]
        else:
           return[Carta(0,'A'), Carta(0,'A')]
       
    def repartir_cartas(mazo):
        """
        Reparte el mazo entre dos jugadores generando dos mazos distintos de 
        igual tamaño.

        Parameters
        ----------
        mazo : Mazo de cartas que será repartido entre los jugadores.

        Returns
        -------
        mazoJugador1 : mazo que corresponderá al jugador1.
        mazoJugador2 : mazo que corresponderá al jugador2.

        """
        random.shuffle(mazo)    
        tamanioMazo = len(mazo)
        divisionMazo = tamanioMazo // 2
        for i in range(tamanioMazo):
            if i < divisionMazo:
                mazoJugador1.append(mazo[i])
            else:
                mazoJugador2.append(mazo[i])
        return mazoJugador1,mazoJugador2
    
    def mostrar_cartas(p_mazoJugador1,p_mazoJugador2):
        """
        Imprime en pantalla las cartas de los jugadores, mostrando solo la 
        última carta visible.

        Parameters
        ----------
        p_mazoJugador1 : mazo correspondiente al jugador1.
        p_mazoJugador2 : mazo correspondiente al jugador2.
            
        Returns
        -------
        None.

        """
        print("------------------------------------")
        print ("Turno:", "1")
        print ("jugador 1:")
        contador = 0
        for carta in mazoJugador1[:min(len(mazoJugador1), 52)]:
            print("-X", end='')
            contador += 1
            if contador == 10:
                print()
                contador = 0
        if contador != 0:
            print()     
        print()
        print("          ",mazoJugador1[-1][0],mazoJugador1[-1][1],"",mazoJugador2[-1][0],mazoJugador2[-1][1])
        print()
        print ("jugador 2:")
        contador = 0
        for carta in mazoJugador2[:min(len(mazoJugador2), 52)]:
            print("-X", end='')
            contador += 1
            if contador == 10:
                print()
                contador = 0
        if contador != 0:
            print()      
        print("------------------------------------")
        
    def guerra(self, p_cartaJugador1, p_cartaJugador2):
        """
        Ejecuta una ronda de "guerra" en el juego de cartas. Se compara una 
        carta de cada jugador y, si son iguales, se ejecuta otra ronda de guerra. 
        Las cartas se agregan a un mazo temporal y se vacía cuando se completa 
        la guerra.

        Parameters
        ----------
        p_cartaJugador1 : carta correspondiente al jugador1.
        p_cartaJugador2 : carta correspondiente al jugador2.

        Returns
        -------
        None.

        """
        self.mostrar_guerra(p_cartaJugador1, p_cartaJugador2)
        self.mazoGuerra.agregar_al_inicio(p_cartaJugador1)
        self.mazoGuerra.agregar_al_inicio(p_cartaJugador2)
        for i in range(3):
            [cartaJugador1, cartaJugador2] = self.sacar_cartas()
            self.mazoEnGuerra.agregar_al_inicio(cartaJugador1)
            self.mazoEnGuerra.agregar_al_inicio(cartaJugador2)
        [cartaJugador1, cartaJugador2] = self.sacar_cartas()
        
        if cartaJugador1 > cartaJugador2 :
            self.vaciar_mazo_guerra()
            self.mazoEnGuerra.agregar_al_inicio(cartaJugador1)
            self.mazoEnGuerra.agregar_al_inicio(cartaJugador2)
            while self.mazoEnGuerra.esta_vacia() is not true:
                self.mazo1.agregar_al_inicio(self.mazoEnGuerra.avanzar())
        
        if cartaJugador2 > cartaJugador1 :
            self.vaciar_mazo_guerra()
            self.mazoEnGuerra.agregar_al_inicio(cartaJugador1)
            self.mazoEnGuerra.agregar_al_inicio(cartaJugador2)
            while self.mazoEnGuerra.esta_vacia() is not True:
                self.mazo2.agregar_al_inicio(self.mazoEnGuerra.avanzar())
        
        if cartaJugador1 == cartaJugador2 and cartaJugador1.valor != 0:
            self.guerra(cartaJugador1, cartaJugador2)
   
    def vaciar_mazo_guerra(self):
        """
        Vacía los mazos de guerra de ambos jugadores y borra cualquier memoria
        de la última guerra en el juego.

        Returns
        -------
        None.

        """
        self.mazoGuerraJugador1.clear()
        self.mazoGuerraJugador2.clear()
        self.memoria_x = ""
        
        
    def jugar_carta(self):
        """
        Juega una ronda del juego de la Guerra.

        Returns
        -------
        None.

        """
        [cartaJugador1, cartaJugador2] = self.sacar_cartas()
        
        if self.jugadorGanador is None:
            self.turnosJugados += 1
        
        if cartaJugador1 > cartaJugador2:
            self.mazo1.agregar_al_inicio(cartaJugador1)
            self.mazo2.agregar_al_inicio(cartaJugador2)
        
        elif cartaJugador2 > cartaJugador1:
            self.mazo2.agregar_al_inicio(cartaJugador1)
            self.mazo2.agregar_al_inicio(cartaJugador2)
           
        elif cartaJugador2 == cartaJugador1 and cartaJugador2 != Carta(0,'A'):
            self.guerra(cartaJugador1, cartaJugador2)
        
        if self.turnosJugados > 10000:
            self.jugadorGanador = "EMPATE"
            self.empate = True
    
    def mostrar_guerra(self, cartaJugador1, cartaJugador2):
        """
        Muestra la información de la partida durante una guerra de cartas.
        
        Parameters
        ----------
        cartaJugador1 : carta correspondiente al jugador1.
        cartaJugador2 : carta correspondiente al jugador2.

        Returns
        -------
        None.

        """
        self.mazoGuerraJugador1.append(cartaJugador1)
        self.mazoGuerraJugador2.append(cartaJugador2)
        self.memoria_x += "-X-X-X-X-X-X"
        lineaJugador1 = ""
        lineaJugador2 = ""
        for carta in self.mazoGuerraJugador1:
             lineaJugador1 += "["
             lineaJugador1 += str(carta.valor)
             lineaJugador1 += carta.palo
             lineaJugador1 += "]"
        for carta in self.mazoGuerraJugador2:
             lineaJugador2 += "["
             lineaJugador2 += str(carta.valor)
             lineaJugador2 += carta.palo
             lineaJugador2 += "]"
        print("GUERRA")
        print(f"Turno: {self.turnosJugados}")
        print("Jugador 1: ")
        for i in range (int((self.mazo1.tamanio())/10)):
            print(f"-X-X-X-X-X-X-X-X-X-X")
        linea = ""
        for i in range((self.mazo1.tamanio())%10):
            linea += "-X"
        print(linea)
        print(f"\n\n")
        print(lineaJugador1, self.memoria_x, lineaJugador2)
        print(f"\n\n")
        print("Jugador 2: ")
        for i in range(int((self.mazo2.tamanio())/10)):
            print(f"-X-X-X-X-X-X-X-X-X-X")
        linea = ""
        for i in range ((self.mazo2.tamanio())%10):
            linea += "-X"
        print(linea)
        
    def mostrar_por_pantalla(self, cartaJugador1, cartaJugador2):
        """
        Muestra por pantalla el estado actual de la partida, incluyendo los mazos
        de cada jugador y las últimas cartas jugadas en el turno actual.

        Parameters
        ----------
        cartaJugador1 : la última carta jugada por el jugador 1 en el turno actual.
        cartaJugador2 : la última carta jugada por el jugador 2 en el turno actual.

        Returns
        -------
        None.

        """
        print(f"Turno: {self.turnosJugados}")
        print("Jugador 1: ")
        for i in range(int((self.mazo1.tamanio())/10)):
            print(f"-X-X-X-X-X-X-X-X-X-X")
        linea = ""
        for i in range ((self.mazo1.tamanio())%10):
            linea += "-X"
        print(linea)
        print(f"\n\n")
        print(f"{cartaJugador1} {cartaJugador2}")
        print(f"\n\n")
        print("Jugador 2: ")
        for i in range(int((self.mazo2.tamanio())/10)):
            print(f"-X-X-X-X-X-X-X-X-X-X")
        linea = ""
        for i in range((self.mazo2.tamanio())%10):
            linea += "-X"
        print(linea)
         
         posicion = p_posicion 
         cartaJugador1 = p_cartaJugador1
         cartaJugador2 = p_cartaJugador2
         mazoJugador1 = p_mazoJugador1 
         mazoJugador2 = p_mazoJugador2 
         if(len(mazoJugador1) <= 52 and len(mazoJugador2) <= 52 and len(mazoJugador1) > 0 and len(mazoJugador2) > 0 ):
            mazoEnMesa[posicion + 2] = cartaJugador1
            mazoEnMesa[posicion + 3] = cartaJugador2
            mazoEnMesa[posicion + 4] = cartaJugador1
            mazoEnMesa[posicion + 5] = cartaJugador2
            mazoEnMesa[posicion + 6] = cartaJugador1
            mazoEnMesa[posicion + 7] = cartaJugador2
            mazoEnMesa[posicion + 8] = cartaJugador1
            mazoEnMesa[posicion + 9] = cartaJugador2
            
            if mazoEnMesa[posicion + 8] > mazoEnMesa[posicion + 9]:
               mazoJugador1.agregar_al_inicio(mazoEnMesa[-1])
               mazoJugador1.agregar_al_inicio(mazoEnMesa[-2])
               mazoEnMesa.clear()
                 
            elif mazoEnMesa[posicion + 8] < mazoEnMesa[posicion + 9]:                  
                 mazoJugador2.agregar_al_inicio(mazoEnMesa[-1])
                 mazoJugador2.agregar_al_inicio(mazoEnMesa[-2])
                 mazoEnMesa.clear()
                    
            elif mazoEnMesa[posicion + 8] == mazoEnMesa[posicion + 9]:
                 mazoEnMesa[posicion + 10] = cartaJugador1
                 mazoEnMesa[posicion + 11] = cartaJugador2
                 mazoEnMesa[posicion + 12] = cartaJugador1
                 mazoEnMesa[posicion + 13] = cartaJugador2
                 mazoEnMesa[posicion + 14] = cartaJugador1
                 mazoEnMesa[posicion + 15] = cartaJugador2
            
    def jugar():
        """
        Juega una partida del juego de la guerra con dos jugadores.

        Returns
        -------
        None.

        """
        mazoEnMesa = Mazo()
        mazoJugador1 = Mazo()
        mazoJugador2 = Mazo()
        turno = 0
        posicion = 0
        
        while len(mazoJugador1) <= 52 and len(mazoJugador2) <= 52:  
           turno = turno + 1
           
           cartaJugador1 = mazoJugador1[-1]
           cartaJugador2 =  mazoJugador2[-1]
           
           mazoEnMesa.mostrar_cartas(mazoJugador1,mazoJugador2)
           
           mazoEnMesa[posicion] = cartaJugador1 
           mazoEnMesa[posicion + 1] = cartaJugador2 
           
           posicion = posicion + 1
           
           if cartaJugador1 > cartaJugador2:
               mazoJugador1.agregar_al_inicio(mazoEnMesa[-1])
               mazoJugador1.agregar_al_inicio(mazoEnMesa[-2])
               mazoEnMesa.clear()
               
           elif cartaJugador1 < cartaJugador2:
                mazoJugador2.agregar_al_inicio(mazoEnMesa[-1])
                mazoJugador2.agregar_al_inicio(mazoEnMesa[-2])
                mazoEnMesa.clear()
              
           elif cartaJugador1 == cartaJugador2:
               mazoEnMesa.guerra(mazoEnMesa,mazoJugador1,mazoJugador2, posicion, cartaJugador1, cartaJugador2)
                    
           elif (len(mazoJugador1) == 0):
               break
               "El jugador 1 pierde el juego"
                    
           elif (len(mazoJugador2) == 0):
               break
               "El jugador 2 pierde el juego"
                            
                        
                    























