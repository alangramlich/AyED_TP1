# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 18:49:28 2023

@author: alang
"""


from modules.Pila import Pila
import random
from ListaDobleEnlazada import ListaDobleEnlazada
import os

def limpiar_consola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        

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
        linea="["
        linea=linea+str(self.valor)+str(self.palo)
        linea=linea+"]"
        return linea
    
    def __bool__(self):
        return self.valor is not None
        
# class JuegoGuerra:
#     def __init__(self, random_seed = 0):
#      	self.semilla = random_seed

    
    
#     def inicializar_mazo(self):
#         self.turnos_jugados=0
#         mazo = [(valor, palo) for valor in valores for palo in palos]
#         random.seed(self.semilla)
#         random.shuffle(mazo)
#         mazo.reverse()
#         par = False
#         self.mazo1=ListaDobleEnlazada()
#         self.mazo2=ListaDobleEnlazada()
#         for carta in mazo:
#             aux=Carta(carta[0],carta[1])
#             if par is False:
#                 #self.mazo1.apilar(aux)
#                 self.mazo1.agregar_al_inicio(aux)
#                 par = not par
#             else:
#                 #self.mazo2.apilar(aux)
#                 self.mazo2.agregar_al_inicio(aux)
#                 par = not par
#         self.botin_de_guerra=ListaDobleEnlazada()
#         self.ganador=None
        
        
#     def iniciar_juego(self):
#         self.inicializar_mazo()
#         while (self.ganador is None):
#             self.jugar_1_carta()
        
        
#     def sacar_cartas(self):
#         if self.mazo1.tamanio == 0:
#             self.ganador="jugador 2"
#             print("HAY GANADOR: JUGADOR 2")
#             print(f"Turnos: {self.turnos_jugados}")
#             print(f"Mazo1: {self.mazo1}")
#             print(f"Mazo2: {self.mazo2}")

#         elif self.mazo2.tamanio == 0:
#             self.ganador="jugador 1"
#             print("HAY GANADOR: JUGADOR 1")
#             print(f"Turnos: {self.turnos_jugados}")
#             print(f"Mazo1: {self.mazo1}")
#             print(f"Mazo2: {self.mazo2}")
            
#         if self.ganador is None:
#             return [self.mazo1.extraer(0), self.mazo2.extraer(0)]
#         else:
#             return [Carta(0, 'A'),Carta(0, 'A')]
        
        
        
        
#     def guerra(self,carta_inicial_1, carta_inicial_2):
#         print("Hay guerra")
#         self.botin_de_guerra.agregar_al_final(carta_inicial_1)
#         self.botin_de_guerra.agregar_al_final(carta_inicial_2)
#         for i in range(3):
#             [carta_jug_1, carta_jug_2]=self.sacar_cartas()
#             self.botin_de_guerra.agregar_al_final(carta_jug_1)
#             self.botin_de_guerra.agregar_al_final(carta_jug_2)
#         [carta_jug_1, carta_jug_2]=self.sacar_cartas()
#         if (carta_jug_1 > carta_jug_2):
#             self.botin_de_guerra.agregar_al_final(carta_jug_1)
#             self.botin_de_guerra.agregar_al_final(carta_jug_2)
#             self.mazo1.concatenar(self.botin_de_guerra)
#             self.botin_de_guerra=ListaDobleEnlazada()
#         if (carta_jug_2 > carta_jug_1):
#             self.botin_de_guerra.agregar_al_final(carta_jug_1)
#             self.botin_de_guerra.agregar_al_final(carta_jug_2)
#             self.mazo2.concatenar(self.botin_de_guerra)
#             self.botin_de_guerra=ListaDobleEnlazada()
#         if (carta_jug_1 == carta_jug_2 and carta_jug_1.valor != 0):
#             self.guerra(carta_jug_1, carta_jug_2)
        
        
        
        
#     def jugar_1_carta(self):
#         self.turnos_jugados += 1
#         print("SE JUEGA UN TURNO")
#         print(f"Jug1: {self.mazo1}")

#         print(f"Jug2: {self.mazo2}")

#         [carta_jug_1, carta_jug_2]=self.sacar_cartas()

#         if (carta_jug_1 > carta_jug_2):
#             self.mazo1.agregar_al_final(carta_jug_1)
#             self.mazo1.agregar_al_final(carta_jug_2)
#         elif (carta_jug_2 > carta_jug_1):
#             self.mazo2.agregar_al_final(carta_jug_1)
#             self.mazo2.agregar_al_final(carta_jug_2)
#         elif (carta_jug_2 == carta_jug_1 and carta_jug_2 != Carta(0, 'A')):
#             self.guerra(carta_jug_1, carta_jug_2)
            
            
#     def mostrar_por_consola(self):
#         limpiar_consola()
#         print(f"Turno: {self.turnos_jugados}")
#         print("Jugador 1: ")
#         for i in range(self.mazo1.tamanio()+self.botin1.tamanio()):
#             print(f"X-")
#         print(f"\n\n")
        
#         print(f"\n\n")
#         for i in range(self.mazo2.tamanio+self.botin2.tamanio()):
#             print(f"X-")
#         #if (self.botin_de_guerra.esta_vacia() is False):
            
            
            
            
            
            
            
            
class JuegoGuerra:
    def __init__(self, random_seed = 0):
     	self.semilla = random_seed

    
    
    def inicializar_mazo(self):
        self.turnos_jugados=0
        mazo = [(valor, palo) for valor in valores for palo in palos]
        random.seed(self.semilla)
        random.shuffle(mazo)
        par = True
        self.aux1=Pila()
        self.aux2=Pila()
        self.mazo1=Pila()
        self.mazo2=Pila()
        for carta in mazo:
            aux=Carta(carta[0],carta[1])
            if par is False:
                self.aux1.apilar(aux)
                par = not par
            else:
                self.aux2.apilar(aux)
                par = not par
        while self.aux1.esta_vacia() is not True:
            self.mazo1.apilar(self.aux1.desapilar())
        while self.aux2.esta_vacia() is not True:
            self.mazo2.apilar(self.aux2.desapilar())
        self.botin1=Pila()
        self.botin2=Pila()
        self.botin_de_guerra=Pila()
        self.botin_aux=Pila()
        self.ganador=None
        self.memoria_jug_1_guerra = []
        self.memoria_jug_2_guerra = []
        self.memoria_x = ""
        
        
    def iniciar_juego(self):
        self.inicializar_mazo()
        while (self.ganador is None):
            self.jugar_1_carta()
        
        
    def sacar_cartas(self):
        
        if self.mazo1.esta_vacia() and self.botin1.esta_vacia():
            self.ganador="jugador 2"
            # print("HAY GANADOR: JUGADOR 2")
            # print(f"Mazo1: {self.mazo1}")
            # print(f"Botin1: {self.botin1}")
            # print(f"Mazo2: {self.mazo2}")
            # print(f"Botin2: {self.botin2}")
        elif self.mazo2.esta_vacia() and self.botin2.esta_vacia():
            self.ganador="jugador 1"
            # print(f"TAMANIO: {self.mazo2.tamanio()}")
            # print("HAY GANADOR: JUGADOR 1")
            # print(f"Turnos: {self.turnos_jugados}")
            # print(f"Mazo1: {self.mazo1}")
            # print(f"Botin1: {self.botin1}")
            # print(f"Mazo2: {self.mazo2}")
            # print(f"Botin2: {self.botin2}")
            # print(f"Tamanio mazo2: {self.mazo2.tamanio()}")
            # print(f"Tamanio mazo1: {self.mazo1.tamanio()}")
            # print(f"{self.mazo2.esta_vacia()}")
        if self.mazo1.esta_vacia() and not self.botin1.esta_vacia():
            for i in range(self.botin1.tamanio()):
                self.mazo1.apilar(self.botin1.desapilar())
            self.botin1=Pila()
        if self.mazo2.esta_vacia() and not self.botin2.esta_vacia():
            for i in range(self.botin2.tamanio()):
                self.mazo2.apilar(self.botin2.desapilar())
            self.botin2=Pila()
        if self.ganador is None:
            return [self.mazo1.desapilar(), self.mazo2.desapilar()]
        else:
            return [Carta(0, 'A'),Carta(0, 'A')]
        
        
        
        
    def guerra(self,carta_inicial_1, carta_inicial_2):
        # print("Hay guerra")
        self.mostrar_guerra(carta_inicial_1, carta_inicial_2)
        self.botin_de_guerra.apilar(carta_inicial_1)
        self.botin_de_guerra.apilar(carta_inicial_2)
        for i in range(3):
            [carta_jug_1, carta_jug_2]=self.sacar_cartas()
            self.botin_de_guerra.apilar(carta_jug_1)
            self.botin_de_guerra.apilar(carta_jug_2)
        [carta_jug_1, carta_jug_2]=self.sacar_cartas()
        if (carta_jug_1 > carta_jug_2):
            self.limpiar_memoria_guerra()
            self.botin_de_guerra.apilar(carta_jug_1)
            self.botin_de_guerra.apilar(carta_jug_2)
            while self.botin_de_guerra.esta_vacia() is not True:
                self.botin_aux.apilar(self.botin_de_guerra.desapilar())
            while self.botin_aux.esta_vacia() is not True:
                self.botin1.apilar(self.botin_aux.desapilar())
        if (carta_jug_2 > carta_jug_1):
            self.limpiar_memoria_guerra()
            self.botin_de_guerra.apilar(carta_jug_1)
            self.botin_de_guerra.apilar(carta_jug_2)
            while self.botin_de_guerra.esta_vacia() is not True:
                self.botin_aux.apilar(self.botin_de_guerra.desapilar())
            while self.botin_aux.esta_vacia() is not True:
                self.botin2.apilar(self.botin_aux.desapilar())
        if (carta_jug_1 == carta_jug_2 and carta_jug_1.valor != 0):
            self.guerra(carta_jug_1, carta_jug_2)
        
        
    def limpiar_memoria_guerra(self):
        self.memoria_jug_1_guerra.clear()
        self.memoria_jug_2_guerra.clear()
        self.memoria_x=""
        
    def jugar_1_carta(self):
        
        # print("SE JUEGA UN TURNO")
        # print(f"Jug1: {self.mazo1}")
        # print(f"{self.botin1}")
        # print(f"Jug2: {self.mazo2}")
        # print(f"{self.botin2}")
        
        [carta_jug_1, carta_jug_2]=self.sacar_cartas()
        self.mostrar_por_consola(carta_jug_1, carta_jug_2)
        if self.ganador is None:
            self.turnos_jugados += 1
        if (carta_jug_1 > carta_jug_2):
            self.botin1.apilar(carta_jug_1)
            self.botin1.apilar(carta_jug_2)
        elif (carta_jug_2 > carta_jug_1):
            self.botin2.apilar(carta_jug_1)
            self.botin2.apilar(carta_jug_2)
        elif (carta_jug_2 == carta_jug_1 and carta_jug_2 != Carta(0, 'A')):
            self.guerra(carta_jug_1, carta_jug_2)
        if self.turnos_jugados > 10000:
            self.ganador="Empate"
            self.empate=True
        
    def mostrar_guerra(self, carta_jug_1, carta_jug_2):
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
        for i in range(int((self.mazo1.tamanio()+self.botin1.tamanio())/10)):
            print(f"-X-X-X-X-X-X-X-X-X-X")
        linea=""
        for i in range ((self.mazo1.tamanio()+self.botin1.tamanio())%10):
            linea+="-X"
        print(linea)
        print(f"\n\n")
        print(linea_jug_1, self.memoria_x, linea_jug_2)
        print(f"\n\n")
        print("Jugador 2: ")
        for i in range(int((self.mazo2.tamanio()+self.botin2.tamanio())/10)):
            print(f"-X-X-X-X-X-X-X-X-X-X")
        linea=""
        for i in range ((self.mazo2.tamanio()+self.botin2.tamanio())%10):
            linea+="-X"
        print(linea)
        
    def mostrar_por_consola(self, carta_jug_1, carta_jug_2):
        #limpiar_consola()
        print(f"Turno: {self.turnos_jugados}")
        print("Jugador 1: ")
        for i in range(int((self.mazo1.tamanio()+self.botin1.tamanio())/10)):
            print(f"-X-X-X-X-X-X-X-X-X-X")
        linea=""
        for i in range ((self.mazo1.tamanio()+self.botin1.tamanio())%10):
            linea+="-X"
        print(linea)
        print(f"\n\n")
        print(f"{carta_jug_1} {carta_jug_2}")
        print(f"\n\n")
        print("Jugador 2: ")
        for i in range(int((self.mazo2.tamanio()+self.botin2.tamanio())/10)):
            print(f"-X-X-X-X-X-X-X-X-X-X")
        linea=""
        for i in range ((self.mazo2.tamanio()+self.botin2.tamanio())%10):
            linea+="-X"
        print(linea)

        #if (self.botin_de_guerra.esta_vacia() is False):