
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 13:44:25 2023

@author: alang
"""


import random
import os
import math


def ordenamiento_inicial(archivo_entrada, archivo_salida1, archivo_salida2, cant_datos):
    """
    Ordena el primer bloque de claves, esta funcion carga en memoria cant_datos
    y los ordena utilizando una lista de python. Luego, escribe alternadamente
    los datos ordenados en los archivos de salida.

    Parameters
    ----------
    nombre : es el nombre que se le dará al archivo que va a generarse.

    Returns
    -------
    None.

    """
    with open(archivo_entrada, 'r') as entrada, \
         open(archivo_salida1, 'w') as salida1, \
         open(archivo_salida2, 'w') as salida2:
             linea_salida1 = []
             linea_salida2 = []
             for i in range(cant_datos):
                 linea = entrada.readline()
                 if not linea:
                     break  # fin del archivo
                 if (linea.strip()):
                     linea_salida1.append(linea)
             # alternar entre salida1 y salida2 y escribir cant_datos líneas en cada uno
             linea_salida1.sort()
             for k in range(len(linea_salida1)):
                 salida1.write(linea_salida1[k])
             linea_salida1=[]
             destino = linea_salida2
             contador_lineas = 0
             for linea in entrada:
                 if (linea.strip()):
                     destino.append(linea)
                 contador_lineas += 1
                 if contador_lineas == cant_datos:
                     destino.sort()
                     for k in range(len(destino)):
                         if destino == linea_salida1:
                             salida1.write(destino[k])
                         elif destino == linea_salida2:
                             salida2.write(destino[k])
                     if destino == linea_salida1:
                         linea_salida1 = []
                         destino = linea_salida2
                     elif destino == linea_salida2:
                         linea_salida2 = []
                         destino = linea_salida1
                     contador_lineas = 0
             for dato in linea_salida1:
                 salida1.write(dato)
             for dato in linea_salida2:
                 salida2.write(dato)
            

def escribir_numeros_aleatorios(nombre_archivo, cant_megas):
    """
    Genera un archivo de datos con números aleatorios de una determinada 
    cantidad de cifras.

    Parameters
    ----------
    nombre : es el nombre que se le dará al archivo que va a generarse.

    Returns
    -------
    None.

    """
    tamano_deseado = cant_megas * 1024 * 1024  # 101 MB en bytes
    tamano_actual = 0
    with open(nombre_archivo, 'w') as f:
        while tamano_actual < tamano_deseado:
            numero = random.randint(10**3, 10**4 - 1)  # Número aleatorio de 20 cifras
            f.write(str(numero) + '\n')  # Escribir el número en el archivo
            tamano_actual = os.stat(nombre_archivo).st_size  # Obtener el tamaño actual del archivo




def dividir_archivo(archivo_entrada, archivo_salida1, archivo_salida2, cant_datos):
    """
    Divide un archivo de entrada en dos archivos de salida, haciendo la 
    mezcla binaria.

    Parameters
    ----------
    archivoDeEntrada : nombre del archivo de entrada.
    archivoDeSalida1 : nombre del archivo de salida 1.
    archivoDeSalida2 : nombre del archivo de salida 2.
    cantidadDatos : Cantidad de datos que se deben escribir en el primer 
    archivo de salida.

    Returns
    -------
    None.

    """
    with open(archivo_entrada, 'r') as entrada, \
         open(archivo_salida1, 'w') as salida1, \
         open(archivo_salida2, 'w') as salida2:
        # escribir las primeras cant_datos líneas en salida1
        for i in range(cant_datos):
            linea = entrada.readline()
            if not linea:
                break  # fin del archivo
            if (linea.strip()):
                salida1.write(linea)
        # alternar entre salida1 y salida2 y escribir cant_datos líneas en cada uno
        destino = salida2
        contador_lineas = 0
        for linea in entrada:
            if (linea.strip()):
                destino.write(linea)
            contador_lineas += 1
            if contador_lineas == cant_datos:
                destino = salida1 if destino == salida2 else salida2
                contador_lineas = 0





def unir_archivo(archivo_entrada_1, archivo_entrada_2, archivo_salida, cant_datos):
    """
    Une dos archivos haciendo la mezcla binaria.
    
    Parameters
    ----------
    archivoDeEntrada1 : Ruta de archivo de entrada1.
    archivoDeEntrada2 : Ruta de archivo de entrada2.
    archivoDeSalida : Ruta de archivo de salida.
    cantidadDatos : Cantidad de datos a escribir en el archivo de salida.

    Returns
    -------
    None.

    """
    with open(archivo_entrada_1, 'r') as archivo_entrada1, \
        open(archivo_entrada_2, 'r') as archivo_entrada2, \
        open(archivo_salida, 'w') as archivo_salida:
            datos_restantes_entrada1=cant_datos-1
            datos_restantes_entrada2=cant_datos-1
            entrada1=archivo_entrada1.readline()
            entrada2=archivo_entrada2.readline()
            if(entrada1 != ''):
                entrada1=int(entrada1)
            if (entrada2 != ''):
                entrada2=int(entrada2)
            while(entrada1 != '' or entrada2 != ''):
                #print(entrada1)
                #print(entrada2)
                if((entrada1 == '\n' or entrada1 == '' or entrada1 == '\r\n') and (entrada2 == '\n' or entrada2 == '' or entrada2 == '\r\n')):
                    break
                elif (entrada1!='' and entrada2!='' and entrada1 != '\n' and entrada2 != '\n'):
                    if (entrada1<=entrada2 and datos_restantes_entrada1 >= 0 and datos_restantes_entrada2 >= 0):
                         archivo_salida.write(str(entrada1)+'\n')
                         datos_restantes_entrada1-=1
                         if (datos_restantes_entrada1>=0):
                             entrada1=archivo_entrada1.readline()
                             if(entrada1.split()):
                                 entrada1=int(entrada1)
                         elif (datos_restantes_entrada1 == -1):
                             entrada1 = ''
                    elif (entrada2<entrada1 and datos_restantes_entrada1 >= 0 and datos_restantes_entrada2 >= 0):
                         archivo_salida.write(str(entrada2)+'\n')
                         datos_restantes_entrada2-=1
                         if (datos_restantes_entrada2>=0):
                             entrada2=archivo_entrada2.readline()
                             if (entrada2.split()):
                                 entrada2=int(entrada2)
                         elif (datos_restantes_entrada2 == -1):
                             entrada2 = ''
                elif (datos_restantes_entrada1 == -1 and datos_restantes_entrada2 >= 0 and entrada2!='' and entrada2!='\n' and entrada2 != '\r\n'):
                    while datos_restantes_entrada2 >= 0:
                        if (entrada2 != ''):
                            archivo_salida.write(str(entrada2)+'\n')
                        datos_restantes_entrada2-=1
                        if (datos_restantes_entrada2>=0):
                            entrada2=archivo_entrada2.readline()
                            if(entrada2.split()):
                                entrada2=int(entrada2)
                elif (datos_restantes_entrada2 == -1 and datos_restantes_entrada1 >= 0 and entrada1!='' and entrada1!='\n' and entrada1 != '\r\n'):
                    while datos_restantes_entrada1 >= 0:
                        if (entrada1 != ''):
                            archivo_salida.write(str(entrada1)+'\n')
                        datos_restantes_entrada1-=1
                        if (datos_restantes_entrada1>=0):
                            entrada1=archivo_entrada1.readline()
                            if (entrada1.split()):
                                entrada1=int(entrada1)
                elif (datos_restantes_entrada1 == -1 and datos_restantes_entrada2 == -1):
                    datos_restantes_entrada1=cant_datos-1
                    datos_restantes_entrada2=cant_datos-1
                    entrada1=archivo_entrada1.readline()
                    if (entrada1.split()):
                        entrada1=int(entrada1)
                    entrada2=archivo_entrada2.readline()
                    if (entrada2.split()):
                        entrada2=int(entrada2)
                elif ((entrada1=='' or entrada1 == '\n') and (entrada2!='' and entrada2!='\n')):
                    archivo_salida.write(str(entrada2)+'\n')
                    entrada2=archivo_entrada2.readline()
                    if(entrada2.split()):
                        entrada2=int(entrada2)
                elif ((entrada2=='' or entrada2 == '\n') and (entrada1!='' and entrada1!='\n')):
                    archivo_salida.write(str(entrada1)+'\n')
                    entrada1=archivo_entrada1.readline()
                    if(entrada1.split()):
                        entrada1=int(entrada1)


def contar_lineas_archivo(archivo):
    """
    Cuenta las lineas del archivo, sin abrirlo en memoria.
    
    Parameters
    ----------
    archivo: Nombre del archivo

    Returns
    -------
    contador: La cantidad de lineas.

    """
    contador = 0
    with open(archivo, 'r') as f:
        for linea in f:
            contador += 1
    return contador

def ordenar(archivo):
    """
    Esta funcion tiene dentro ordenadas las llamadas a las demas funciones.
    Con solo llamar a esta funcion y pasarle el nombre del archivo, se ordena.
    
    Parameters
    ----------
    archivo: Nombre del archivo

    Returns
    -------

    """
    cantidad_datos=contar_lineas_archivo(archivo)
    # for ronda in range(int(math.log2(cantidad_datos)+1)):
    #     dividir_archivo(archivo, "salida1.txt", "salida2.txt", int(math.pow(2, ronda)))
    #     unir_archivo("salida1.txt", "salida2.txt", archivo, int(math.pow(2, ronda)))
        
    ordenamiento_inicial(archivo, "salida1.txt", "salida2.txt", 10)
    unir_archivo("salida1.txt", "salida2.txt", archivo, 10)
    for ronda in range(int(math.log2(cantidad_datos/10)+1)):
        dividir_archivo(archivo, "salida1.txt", "salida2.txt", int(math.pow(2, ronda)*10))
        #print(f"Divido en long: {int(math.pow(2, ronda)*10)}")
        unir_archivo("salida1.txt", "salida2.txt", archivo, int(math.pow(2, ronda)*10))


