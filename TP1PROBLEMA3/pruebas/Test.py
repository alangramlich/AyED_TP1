# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 14:41:15 2023

@author: alang
"""
import unittest
import random
from modules.OrdenamientoExterno import *
class TestOrdenamientoExterno(unittest.TestCase):
    
    def test_ordenamiento_fino(self):
        """
        Compruebo con pocos datos que ordene correctamente
        """
        
        """ 
        Creo una lista de mil elementos, los guardo en un archivo
        los ordeno y luego compruebo que esten en orden
        """
        escribir_numeros_aleatorios("datos.txt", 0.1)
        lista1 = []
        with open("datos.txt", 'r') as f:
            for linea in f:
                lista1.append(linea)
        lista1.sort()
        ordenar("datos.txt")

        lista2 = []
        with open("datos.txt", 'r') as f:
            for linea in f:
                lista2.append(linea)
        self.assertEqual(lista1==lista2, True)







    def test_ordenamiento_grueso(self):
        """
        Compruebo que la cantidad de de datos sea la misma, y que los datos
        sean de valor creciente.
        """
        
        escribir_numeros_aleatorios("datos_test_2.txt", 5)
        numero_lineas_originales = 0
        with open("datos_test_2.txt", 'r') as f:
            for linea in f:
                numero_lineas_originales += 1
                
                
        ordenar('datos_test_2.txt')
        
        numero_lineas_luego_de_ordenar=0
        es_creciente = True
        num_anterior=0
        with open('datos_test_2.txt', 'r') as f:
            for linea in f:
                numero_lineas_luego_de_ordenar+=1
                linea.strip()
                num_actual=int(linea)
                if (num_actual>=num_anterior):
                    num_anterior=num_actual
                else:
                    es_creciente=False
        self.assertEqual(es_creciente, True)
        self.assertEqual(numero_lineas_originales, numero_lineas_luego_de_ordenar)
    
if __name__ == '__main__':
    unittest.main()