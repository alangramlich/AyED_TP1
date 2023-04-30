# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:55:39 2023

@author: alang
"""
from modules.JuegoGuerra import JuegoGuerra
from modules.JuegoGuerra import Carta


# carta1=Carta('9','pica')
# carta2=Carta('A','corazon')
# print(carta1)
# print(carta2)

juego=JuegoGuerra(random_seed=314)
juego.inicializar_mazo()


print ("MAZOS INICIALES: ")
print(juego.mazo1)
print(juego.mazo2)

juego.iniciar_juego()

print("Termino")
print(f"Turnos: {juego.turnos_jugados}")

# print("MAZOS FINALES:")
# print(juego.mazo1)
# print(juego.mazo2)
# print(juego.botin1)
# print(juego.botin2)