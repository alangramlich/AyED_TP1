# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 13:44:25 2023

@author: alang
"""

from modules.OrdenamientoExterno import *
import  math

escribir_numeros_aleatorios("datos.txt", 0.1)
lista1 = []
with open("datos.txt", 'r') as f:
    for linea in f:
        lista1.append(linea)
lista1.sort()
num_lineas=contar_lineas_archivo("datos.txt")
print(f"Lineas iniciales: {num_lineas}")

ordenar("datos.txt")

num_lineas=contar_lineas_archivo("datos.txt")
print(f"Lineas finales: {num_lineas}")

lista2 = []
with open("datos.txt", 'r') as f:
    for linea in f:
        lista2.append(linea)



lista_1 = [random.randint(1, 100) for _ in range(1000)]
        
with open('datos_test_1.txt', 'w') as archivo:
    for elemento in lista_1:
        archivo.write(str(elemento) + '\n')
    lista_1=[]
    with open("datos_test_1.txt", 'r') as f:
        for linea in f:
            linea.strip()
            lista_1.append(int(linea))
    lista_1.sort()
    ordenar('datos_test_1.txt')
    lista_2=[]
    with open('datos_test_1.txt', 'r') as f:
        for linea in f:
            linea.strip()
            lista_2.append(int(linea))