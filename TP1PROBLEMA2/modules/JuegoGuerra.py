# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 18:49:28 2023

@author: alang
"""

import sys
sys.path.append("C:/REPOSITORIOS/Algoritmos-y-estructuras-de-datos/TP1PROBLEMA1")
from ListaDobleEnlazada import *
import random


valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'] 
palos = ['♠', '♥', '♦', '♣']




class JuegoGuerra:
    def __init__(self, p_semilla = 0):
    	self.semilla = p_semilla


    def inicializar_mazo():
    	cartas_en_orden = [(valor, palo) for valor in valores for palo in palos]
    	random.seed(self.semilla)
    	# aquí se inicializa el mazo de cartas
    	random.shuffle(cartas)
    