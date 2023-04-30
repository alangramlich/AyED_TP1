# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 18:27:00 2023

@author: alang
"""
from modules.ListaDobleEnlazada import ListaDobleEnlazada
import time
import random
import matplotlib.pyplot as plt


#%%    ESTE BLOQUE CREA LOS TIEMPOS Y LOS GUARDA EN UN TXT

lista_doble_enlazada = ListaDobleEnlazada()
lista = []
lista_de_tiempos=[]
for l in range(1000): 
    lista = random.sample(range(10000), l)
    lista_doble_enlazada = ListaDobleEnlazada()
    for k in range(len(lista)):
        lista_doble_enlazada.agregar_al_final(lista[k])
    tiempo_inicial=time.time()
    lista_doble_enlazada.ordenar()
    tiempo_final=time.time()
    lista_de_tiempos.append(tiempo_final-tiempo_inicial)
    del lista_doble_enlazada
with open("tiempos_para_alg_insercion_de_0_a_1000_muestras.txt", "w") as archivo:
    for elemento in lista_de_tiempos:
        archivo.write(str(elemento) + "\n")
        
        
#%%      ESTE BLOQUE LEVANTA LOS DATOS DEL TXT Y LOS GRAFICA  
def leer_archivo(nombre_archivo):
    lista_datos=[]
    with open(nombre_archivo, 'r') as archivo:
        for i in range(1000):
            lista_datos.append(float(archivo.readline()))
    return lista_datos


x = list(range(1000))
y = leer_archivo("tiempos_para_alg_insercion_de_0_a_1000_muestras.txt")
z = [i**2/5000000 for i in range(1000)]
# Plot 1
plt.plot(x, y, label='Alg. insercion')
plt.xlabel('Muestras')
plt.ylabel('Tiempos')
plt.title('Tiempos para algoritmo de insercion')
plt.legend()
plt.show()

# Plot 2

plt.plot(x, y, color = 'blue', label='Alg. insercion')
plt.plot(x, z, color = 'red', label='x**2')
plt.xlabel('N muestras')
plt.ylabel('Tiempos')
plt.title('Tiempos y x**2')
plt.legend()
plt.show()

