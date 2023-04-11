# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:55:39 2023

@author: alang
"""
from modules.JuegoGuerra import JuegoGuerra
from modules.JuegoGuerra import Carta
from modules.JuegoGuerra import Pila

# carta1=Carta('9','pica')
# carta2=Carta('A','corazon')
# print(carta1)
# print(carta2)

juego=JuegoGuerra()
juego.inicializar_mazo()
aux=Carta('A','♠')
juego.mazo1.apilar(aux)
juego.mazo2.apilar(aux)
print ("MAZOS INICIALES: ")
print(juego.mazo1)
print(juego.mazo2)


for i in range(3000):
    juego.jugar_1_carta()




# print("MAZOS FINALES:")
# print(juego.mazo1)
# print(juego.mazo2)
# print(juego.botin1)
# print(juego.botin2)