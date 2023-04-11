# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 18:49:28 2023

@author: alang
"""

import sys
sys.path.append("C:/REPOSITORIOS/Algoritmos-y-estructuras-de-datos/TP1PROBLEMA1")
from modules.Pila import Pila
import random


valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'] 
palos = ['♠', '♥', '♦', '♣']

def transformacion_comparable(valor):
    
    if valor == 'A':
        valor = 14
    if valor == 'K':
        valor = 13
    if valor == 'Q':
        valor = 12
    if valor == 'J':
        valor = 11
    valor=int(valor)
    #print(valor)
    return valor

class Carta:
    def __init__(self,valor,palo):
        [self.valor, self.palo] = [valor,palo]
    
    def __eq__(self,other):
        return self.valor == other.valor 
    
    def __lt__(self, other):
        valor_comparable1=transformacion_comparable(self.valor)
        valor_comparable2=transformacion_comparable(other.valor)
        
        return valor_comparable1 < valor_comparable2
    
    def __str__(self):
        linea="{"
        linea=linea+str(self.valor)+str(self.palo)
        linea=linea+"}"
        return linea
    
    def __bool__(self):
        return self.valor is not None
        
class JuegoGuerra:
    def __init__(self, random_seed = 0):
    	self.semilla = random_seed

    
    
    def inicializar_mazo(self):
        mazo = [(valor, palo) for valor in valores for palo in palos]
        random.seed(self.semilla)
        random.shuffle(mazo)
        par = False
        self.mazo1=Pila()
        self.mazo2=Pila()
        for carta in mazo:
            aux=Carta(carta[0],carta[1])
            if par is False:
                self.mazo1.apilar(aux)
                par = not par
            else:
                self.mazo2.apilar(aux)
                par = not par
        self.botin1=Pila()
        self.botin2=Pila()
        self.botin_de_guerra=Pila()
        self.ganador=None
        
    def sacar_cartas(self):
        if self.mazo1.esta_vacia() and self.botin1.esta_vacia():
            self.ganador="Jugador 2"
            print("HAY GANADOR: JUGADOR 2")
            exit()
        elif self.mazo2.esta_vacia() and self.botin2.esta_vacia():
            self.ganador="Jugador 1"
            print(f"TAMANIO: {self.mazo2.tamanio()}")
            print("HAY GANADOR: JUGADOR 1")
            print(f"Mazo1: {self.mazo1}")
            print(f"Botin1: {self.botin1}")
            print(f"Mazo2: {self.mazo2}")
            print(f"Botin2: {self.botin2}")
            print(f"Tamanio mazo2: {self.mazo2.tamanio()}")
            print(f"Tamanio mazo1: {self.mazo1.tamanio()}")
            print(f"{self.mazo2.esta_vacia()}")
            exit()
        if self.mazo1.esta_vacia() and not self.botin1.esta_vacia():
            self.mazo1=self.botin1
            self.botin1=Pila()
        if self.mazo2.esta_vacia() and not self.botin2.esta_vacia():
            self.mazo2=self.botin2
            self.botin2=Pila()
        if self.ganador is None:
            return [self.mazo1.desapilar(), self.mazo2.desapilar()]
        else:
            return [0,0]
    def guerra(self,carta_inicial_1, carta_inicial_2):
        print("Hay guerra")
        self.botin_de_guerra.apilar(carta_inicial_1)
        self.botin_de_guerra.apilar(carta_inicial_2)
        for i in range(2):
            [carta_jug_1, carta_jug_2]=self.sacar_cartas()
            self.botin_de_guerra.apilar(carta_jug_1)
            self.botin_de_guerra.apilar(carta_jug_2)
        [carta_jug_1, carta_jug_2]=self.sacar_cartas()
        #carta_jug_1=self.mazo1.desapilar()
        #carta_jug_2=self.mazo2.desapilar()
        #print(f"Se comparan: jug 1: {carta_jug_1} jug 2: {carta_jug_2}")
        if (carta_jug_1 > carta_jug_2):
            self.botin1.apilar(carta_jug_1)
            self.botin1.apilar(carta_jug_2)
            while self.botin_de_guerra.esta_vacia() is not True:
                self.botin1.apilar(self.botin_de_guerra.desapilar())
        if (carta_jug_2 > carta_jug_1):
            self.botin2.apilar(carta_jug_1)
            self.botin2.apilar(carta_jug_2)
            while self.botin_de_guerra.esta_vacia() is not True:
                self.botin2.apilar(self.botin_de_guerra.desapilar())
        if (carta_jug_1 == carta_jug_2):
            self.guerra(carta_jug_1, carta_jug_2)
        
    def jugar_1_carta(self):
        print("SE JUEGA UN TURNO")
        print(f"Jug1: {self.mazo1}")
        print(f"{self.botin1}")
        print(f"Jug2: {self.mazo2}")
        print(f"{self.botin2}")
        [carta_jug_1, carta_jug_2]=self.sacar_cartas()
        #carta_jug_1 = self.mazo1.desapilar()
        #carta_jug_2 = self.mazo2.desapilar()
        #print(f"Se comparan: jug 1: {carta_jug_1} jug 2: {carta_jug_2}")
        if (carta_jug_1 > carta_jug_2):
            self.botin1.apilar(carta_jug_1)
            self.botin1.apilar(carta_jug_2)
        elif (carta_jug_2 > carta_jug_1):
            self.botin2.apilar(carta_jug_1)
            self.botin2.apilar(carta_jug_2)
        elif (carta_jug_2 == carta_jug_1):
            self.guerra(carta_jug_1, carta_jug_2)
            