# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:41:37 2023

@author: alang
"""
from modules.ListaDobleEnlazada import ListaDobleEnlazada
from modules.Nodo import Nodo

# lista=ListaDobleEnlazada()
# lista.agregar_al_final(1)
# lista.agregar_al_final(2)
# lista.agregar_al_final(3)
# lista.agregar_al_final(4)
# lista.agregar_al_final(5)
# lista.agregar_al_final(6)
# print(lista)

# print(f"Longitud: {len(lista)}")

#----------------------PRUEBA DE CONCATENAR
# print("PRUEBA DE CONCATENAR: ")
# lista2=ListaDobleEnlazada()
# lista2.agregar_al_final(7)
# lista2.agregar_al_final(8)
# lista2.agregar_al_final(9)
# lista3=lista+lista2
# print(lista3)
# lista4=ListaDobleEnlazada()
# lista4=lista3+lista4
# print(lista4)

# print("PRUEBA DE COPIAR: ")
# lista4=lista3.copiar()
# print(lista4)

# print("PRUEBA DE INSERTAR: ")
# lista.insertar(10,3)
# print(lista)

# print("PRUEBA DE EXTRAER: ")
# print(lista)
# lista.extraer(-1)
# print(lista)

# print("PRUEBA DE INVERTIR: ")
# lista.invertir()
# print(lista)


print("PRUEBA DE ORDENAR: ")
lista = [8, 6, 5, 1, 2, 0, 4, 7, 3, 9]
lista_ord=ListaDobleEnlazada()
for i in range(len(lista)):
    lista_ord.agregar_al_final(lista[i])
print("Lista original: ")
print(lista_ord)
lista_ord.ordenar()
print(lista_ord)