# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 18:49:28 2023

@author: alang
"""
import os
import sys
#sys.path.append(os.path.abspath('..'))

ruta_actual = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
print("La ruta actual es:", ruta_actual)
ruta_actual+="..\TP2\modules"
sys.path.append(ruta_actual)
from modules.ColaSimple import ColaSimple
import random

        

valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'] 
palos = ['♠', '♥', '♦', '♣']

def transformacion_comparable(valor):
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
    if valor == 'A':
        valor = 14
    if valor == 'K':
        valor = 13
    if valor == 'Q':
        valor = 12
    if valor == 'J':
        valor = 11
    valor=int(valor)
    return valor

class Carta:
    def __init__(self,valor,palo):
        """
        Es el constructor de la clase. Esta clase se utiliza para facilitar
        la resolucion del juego. Tiene el fin de poder comparar elementos de 
        tipo carta.
        Parameters
        ----------
        valor : valor entero de la carta.
        palo : palo de la carta.
        Returns
        -------
        None.
        """
        [self.valor, self.palo] = [valor,palo]
    
    def __eq__(self,other):
        """
        Compara si el valor del objeto actual es igual al valor del 
        objeto 'otro'.
        Parameters
        ----------
        otro : objeto de la misma clase.
        Returns
        -------
        bool: True si los valores son iguales, False si son diferentes
        """
        return self.valor == other.valor 
    
    def __lt__(self, other):
        """
        Compara dos cartas del mazo por su valor, incluyendo la posibilidad
        de compara letras.
        Parameters
        ----------
        otro : valor de la carta con el que se compara de la carta actual .
        Returns
        -------
        bool: True si la carta actual tiene un valor menor que la carta a comparar,
        False en caso contrario.
        """
        valor_comparable1=transformacion_comparable(self.valor)
        valor_comparable2=transformacion_comparable(other.valor)
        
        return valor_comparable1 < valor_comparable2
    
    def __str__(self):
        """
        Retorna un string que representa una carta.
        Returns
        -------
        linea 
        """
        linea="["
        linea=linea+str(self.valor)+str(self.palo)
        linea=linea+"]"
        return linea
    
    def __bool__(self):
        """
        Devuelve True si el atributo 'valor' del objeto es distinto de None, 
        False en caso contrario.
        """
        return self.valor is not None
        
            
class JuegoGuerra:
    def __init__(self, random_seed = 0):
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
        self.semilla = random_seed

    
    
    def inicializar_mazo(self):
        """
        Inicializa todas las variables del juego de cartas y mezcla las cartas
        en los mazos.
        Returns
        -------
        None.
        """
        self.turnos_jugados=0
        mazo = [(valor, palo) for valor in valores for palo in palos]
        random.seed(self.semilla)
        random.shuffle(mazo)
        par = True
        self.mazo1=ColaSimple()
        self.mazo2=ColaSimple()
        for carta in mazo:
            aux=Carta(carta[0],carta[1])
            if par is False:
                self.mazo1.agregar(aux)
                par = not par
            else:
                self.mazo2.agregar(aux)
                par = not par

        self.botin_de_guerra=ColaSimple()
        self.ganador=None
        self.memoria_jug_1_guerra = []
        self.memoria_jug_2_guerra = []
        self.memoria_x = ""
        
        
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
        while (self.ganador is None):
            self.jugar_1_carta()
        
        
    def sacar_cartas(self):
        """
        Toma dos cartas del principio de cada mazo y las devuelve en una lista. 
        Si uno de los mazos se queda sin cartas, se asigna un ganador. 
        
        Returns
        -------
        list: Una lista de dos cartas tomadas del principio de cada mazo.
        """
        if self.mazo1.esta_vacia():
            self.ganador="jugador 2"
        elif self.mazo2.esta_vacia():
            self.ganador="jugador 1"
        if self.ganador is None:
            return [self.mazo1.avanzar(), self.mazo2.avanzar()]
        else:
            return [Carta(0, 'A'),Carta(0, 'A')]
        
        
        
        
    def guerra(self,carta_inicial_1, carta_inicial_2):
        """
        Ejecuta una ronda de "guerra" en el juego de cartas. Se compara una 
        carta de cada jugador y, si son iguales, se ejecuta otra ronda de 
        guerra. 
        Parameters
        ----------
        p_cartaJugador1 : carta correspondiente al jugador1.
        p_cartaJugador2 : carta correspondiente al jugador2.
        Returns
        -------
        None.
        """
        self.mostrar_guerra(carta_inicial_1, carta_inicial_2)
        self.botin_de_guerra.agregar(carta_inicial_1)
        self.botin_de_guerra.agregar(carta_inicial_2)
        for i in range(3):
            [carta_jug_1, carta_jug_2]=self.sacar_cartas()
            self.botin_de_guerra.agregar(carta_jug_1)
            self.botin_de_guerra.agregar(carta_jug_2)
        [carta_jug_1, carta_jug_2]=self.sacar_cartas()
        if (carta_jug_1 > carta_jug_2):
            self.limpiar_memoria_guerra()
            self.botin_de_guerra.agregar(carta_jug_1)
            self.botin_de_guerra.agregar(carta_jug_2)
            while self.botin_de_guerra.esta_vacia() is not True:
                self.mazo1.agregar(self.botin_de_guerra.avanzar())
        if (carta_jug_2 > carta_jug_1):
            self.limpiar_memoria_guerra()
            self.botin_de_guerra.agregar(carta_jug_1)
            self.botin_de_guerra.agregar(carta_jug_2)
            while self.botin_de_guerra.esta_vacia() is not True:
                self.mazo2.agregar(self.botin_de_guerra.avanzar())
        if (carta_jug_1 == carta_jug_2 and carta_jug_1.valor != 0):
            self.guerra(carta_jug_1, carta_jug_2)
        
        
    def limpiar_memoria_guerra(self):
        """
        Limpia la memoria de guerra. Es utilizada para mostrar por consola.
        Returns
        -------
        None.
        """
        self.memoria_jug_1_guerra.clear()
        self.memoria_jug_2_guerra.clear()
        self.memoria_x=""
        
    def jugar_1_carta(self):
        """
        Juega una ronda del juego de la Guerra.
        Returns
        -------
        None.
        """
        [carta_jug_1, carta_jug_2]=self.sacar_cartas()
        if self.ganador is None:
            self.turnos_jugados += 1
        if (carta_jug_1 > carta_jug_2):
            self.mazo1.agregar(carta_jug_1)
            self.mazo1.agregar(carta_jug_2)
        elif (carta_jug_2 > carta_jug_1):
            self.mazo2.agregar(carta_jug_1)
            self.mazo2.agregar(carta_jug_2)
        elif (carta_jug_2 == carta_jug_1 and carta_jug_2 != Carta(0, 'A')):
            self.guerra(carta_jug_1, carta_jug_2)
        if self.turnos_jugados > 10000:
            self.ganador="Empate"
            self.empate=True
        
    def mostrar_guerra(self, carta_jug_1, carta_jug_2):
        """
        Muestra la información de la partida durante una guerra.
        
        Parameters
        ----------
        cartaJugador1 : carta correspondiente al jugador1.
        cartaJugador2 : carta correspondiente al jugador2.
        Returns
        -------
        None.
        """
        self.memoria_jug_1_guerra.append(carta_jug_1)
        self.memoria_jug_2_guerra.append(carta_jug_2)
        self.memoria_x+="-X-X-X-X-X-X"
        linea_jug_1=""
        linea_jug_2=""
        for carta in self.memoria_jug_1_guerra:
            linea_jug_1+="["
            linea_jug_1+=str(carta.valor)
            linea_jug_1+=carta.palo
            linea_jug_1+="]"
        for carta in self.memoria_jug_2_guerra:
            linea_jug_2+="["
            linea_jug_2+=str(carta.valor)
            linea_jug_2+=carta.palo
            linea_jug_2+="]"
        print("***Guerra!!!***")
        print(f"Turno: {self.turnos_jugados}")
        print("Jugador 1: ")
        for i in range(int((self.mazo1.tamanio())/10)):
            print(f"-X-X-X-X-X-X-X-X-X-X")
        linea=""
        for i in range ((self.mazo1.tamanio())%10):
            linea+="-X"
        print(linea)
        print(f"\n\n")
        print(linea_jug_1, self.memoria_x, linea_jug_2)
        print(f"\n\n")
        print("Jugador 2: ")
        for i in range(int((self.mazo2.tamanio())/10)):
            print(f"-X-X-X-X-X-X-X-X-X-X")
        linea=""
        for i in range ((self.mazo2.tamanio())%10):
            linea+="-X"
        print(linea)
        
    def mostrar_por_consola(self, carta_jug_1, carta_jug_2):
        """
        Muestra por pantalla el estado actual de la partida.
        Parameters
        ----------
        cartaJugador1 : la última carta jugada por el jugador 1 en el 
        turno actual.
        cartaJugador2 : la última carta jugada por el jugador 2 en el 
        turno actual.
        Returns
        -------
        None.
        """
        print(f"Turno: {self.turnos_jugados}")
        print("Jugador 1: ")
        for i in range(int((self.mazo1.tamanio())/10)):
            print(f"-X-X-X-X-X-X-X-X-X-X")
        linea=""
        for i in range ((self.mazo1.tamanio())%10):
            linea+="-X"
        print(linea)
        print(f"\n\n")
        print(f"{carta_jug_1} {carta_jug_2}")
        print(f"\n\n")
        print("Jugador 2: ")
        for i in range(int((self.mazo2.tamanio())/10)):
            print(f"-X-X-X-X-X-X-X-X-X-X")
        linea=""
        for i in range ((self.mazo2.tamanio())%10):
            linea+="-X"
        print(linea)
