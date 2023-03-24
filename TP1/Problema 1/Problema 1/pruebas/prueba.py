# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:41:37 2023

@author: alang
"""
from modules.ListaDobleEnlazada import ListaDobleEnlazada
from modules.Nodo import Nodo

lista=ListaDobleEnlazada()
lista.agregar_al_final(1)
lista.agregar_al_final(4)
lista.agregar_al_final(3)
lista.agregar_al_final(4)
lista.agregar_al_final(5)
lista.agregar_al_final(2)
#lista.insertar(10,0)
#print(lista.extraer(3).dato)
#lista.invertir()

print("None")
actual=lista.primero
for i in range(lista.tamanio):
    print(actual.dato)
    actual=actual.siguiente
print("None")

lista.ordenar()

print("None")
actual=lista.primero
for i in range(lista.tamanio):
    print(actual.dato)
    actual=actual.siguiente
print("None")


# print("None")
# lista2=lista.copiar()

# actual2=lista2.primero
# print("None")
# print(lista2.tamanio)
# for i in range(lista2.tamanio):
#     print(actual2.dato)
#     actual2=actual2.siguiente
# print("None")