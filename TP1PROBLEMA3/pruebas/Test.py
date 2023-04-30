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
        lista1 = [random.randint(1, 100) for _ in range(1000)]
        
        with open('datos_test_1.txt', 'w') as archivo:
            for elemento in lista1:
                archivo.write(str(elemento) + '\n')
        lista1.sort()
        ordenar('datos_test_1.txt')
        lista2=[]
        with open('datos_test_1.txt', 'r') as f:
            for linea in f:
                linea.strip()
                lista2.append(int(linea))
        self.assertEqual(lista1, lista2)







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