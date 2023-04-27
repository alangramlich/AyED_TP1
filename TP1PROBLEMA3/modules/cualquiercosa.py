# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from random import randint
from typing import List


#ESTA FUNCION ME LEE UN BLOQUE DE B DATOS
def leer_bloque(archivo, B):
    bloq = []
    for i in range(B):
        linea = archivo.readline()
        if not linea:
            break
        bloq.append(int(linea.strip()))
    return bloq


def escribir_datos_ordenados(datos_ordenados, nombre, ronda=0):
    with open(str(nombre) + str(ronda) + ".txt", "w") as archivo:
        for dato in datos_ordenados:
            archivo.write(str(dato) + "\n")



def fusionar_archivos(archivo1, archivo2, archivo_salida):
    with open(archivo1) as f1, open(archivo2) as f2, open(archivo_salida, 'w') as fs:
        linea1 = f1.readline().rstrip('\n')
        linea2 = f2.readline().rstrip('\n')
        
        while linea1 and linea2:
            if int(linea1) < int(linea2):
                fs.write(linea1 + '\n')
                linea1 = f1.readline().rstrip('\n')
            else:
                fs.write(linea2 + '\n')
                linea2 = f2.readline().rstrip('\n')
        
        # copiar restante del archivo 1
        while linea1:
            fs.write(linea1 + '\n')
            linea1 = f1.readline().rstrip('\n')
        
        # copiar restante del archivo 2
        while linea2:
            fs.write(linea2 + '\n')
            linea2 = f2.readline().rstrip('\n')

   
def crear_archivo_de_datos(nombre):
    f = 10**6
    N = 1*f
    cifras = 20
    tam_bloque = f # 1 M de valores por bloque a escribir
    
    print('Cantidad de valores a escribir:', N)
    
    # truncar archivo si existe
    with open(nombre, 'w') as archivo:
        pass
    
    # escribir datos
    N_restantes = N
    while N_restantes > 0:
        cif = cifras
        r = N_restantes % tam_bloque
        c = N_restantes // tam_bloque
        if c > 0:
            t = tam_bloque
        elif c == 0:
            t = r
        N_restantes -= t
        print('t =', t, ', N_restantes =', N_restantes)
        bloque = [str(randint(10*(cif-1), 10*cif-1))+'\n'
                  for i in range(t)]        
        with open(nombre, 'a+') as archivo:
            archivo.writelines(bloque)
 
def contar_lineas(archivo):
    with open(archivo, 'r') as f:
        contador = 0
        for linea in f:
            contador += 1
    return contador




#ESTA ES LA PARTE DE DIVIDIR 

datos_por_bloque = 90000
crear_archivo_de_datos('datos.txt')
cantidad_de_datos = contar_lineas('datos.txt')
cantidad_de_bloques = cantidad_de_datos // datos_por_bloque
if cantidad_de_datos%datos_por_bloque != 0:
    cantidad_de_bloques+=1
nombre=0
archivo=open('datos.txt', 'r')
for numero in range(cantidad_de_bloques):
    bloque = leer_bloque(archivo, datos_por_bloque)
    bloque.sort()
    escribir_datos_ordenados(bloque, numero)
archivo.close()


#ESTA ES LA PARTE DE FUSIONAR
numero_de_archivo=0
numero_de_ronda=0
if cantidad_de_bloques%2 == 0:
    cantidad_de_archivos=cantidad_de_bloques
    while(cantidad_de_archivos != 1):
        for par_de_archivos in range(int(cantidad_de_archivos/2)):
            if cantidad_de_archivos != 2:
                fusionar_archivos(str(par_de_archivos*2)+str(numero_de_ronda)+".txt" , str(par_de_archivos*2+1)+str(numero_de_ronda)+".txt" , str(par_de_archivos)+str(numero_de_ronda+1)+".txt")
            else:
                fusionar_archivos(str(par_de_archivos*2)+str(numero_de_ronda)+".txt" , str(par_de_archivos*2+1)+str(numero_de_ronda)+".txt" , "archivo_ordenado.txt")
        cantidad_de_archivos=int(cantidad_de_archivos/2)
        numero_de_ronda+=1
    
else:
    cantidad_de_archivos=cantidad_de_bloques-1
    while(cantidad_de_archivos != 1):
        for par_de_archivos in range(int(cantidad_de_archivos/2)):
            fusionar_archivos(str(par_de_archivos*2)+str(numero_de_ronda)+".txt" , str(par_de_archivos*2+1)+str(numero_de_ronda)+".txt" , str(par_de_archivos)+str(numero_de_ronda+1)+".txt")
        cantidad_de_archivos=int(cantidad_de_archivos/2)
        numero_de_ronda+=1
    fusionar_archivos(str(cantidad_de_bloques-1)+"0.txt", str(0)+str(numero_de_ronda)+".txt", "archivo_ordenado.txt")
archivo.close()