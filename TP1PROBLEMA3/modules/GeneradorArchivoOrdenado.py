# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 12:20:17 2023

@author: Priscila
"""
# -*- coding: utf-8 -*-

from random import randint
import random

def crear_archivo_de_datos(nombre):
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
    f = 10**6
    N = 5*f
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
        bloque = [str(randint(10**(cif-1), 10**cif-1))+'\n'
                  for i in range(t)]        
        with open(nombre, 'a+') as archivo:
            archivo.writelines(bloque)
 
def dividir_archivo(archivoDeEntrada, archivoDeSalida1, archivoDeSalida2, cantidadDatos):
    """
    Divide un archivo de entrada en dos archivos de salida, escribiendo los 
    primeros cantidadDatos en archivoDeSalida1 y alternando la escritura entre 
    archivoDeSalida1 y archivoDeSalida2 para el resto de las lineas.

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
    with open(archivoDeEntrada, 'r') as entrada,\
         open(archivoDeSalida1, 'w') as salida1,\
         open(archivoDeSalida2, 'w') as salida2:
        #escribir las primeras cantidadDatos en salida1
        for i in range(cantidadDatos):
            linea = entrada.readline()
            if not linea:
                break
            if(linea.strip()):
                salida1.write(linea)
        #alternar entre salida1 y salida2, despues escribir tantas lineas como cantidadDatos haya
        destino = salida2
        contadorLineas = 0
        for linea in entrada:
            if(linea.strip()):
                destino.write(linea)
            contadorLineas += 1
            if contadorLineas == cantidadDatos:
                destino = salida1 if destino == salida2 else salida2
                contadorLineas = 0
            
def unir_archivos(archivoDeEntrada1, archivoDeEntrada2, archivoDeSalida, cantidadDatos):
    """
    Une dos archivos de entrada ordenados de menor a mayor y escribe el resultado en un 
    archivo de salida.
    
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
    with open(archivoDeEntrada1, 'r') as archivoDeEntrada1,\
         open(archivoDeEntrada2, 'r') as archivoDeEntrada2,\
         open(archivoDeSalida, 'w') as archivoDeSalida:
             datosRestantesDeEntrada1 = cantidadDatos - 1
             datosRestantesDeEntrada2 = cantidadDatos - 1
             entrada1 = archivoDeEntrada1.readline()
             entrada2 = archivoDeEntrada2.readline()
             if(entrada1 != ''):
                 entrada1 = int(entrada1)
             if(entrada2 != ''):
                 entrada2 = int(entrada2)
             while(entrada1 != '' or entrada2 != ''):
                 if((entrada1 == '\n' or entrada1 == '' or entrada1 == '\r\n') and (entrada2 == '\n' or entrada2 == '' or entrada2 == '\r\n')):
                     break
                 elif(entrada1 != '' and entrada2 != '' and entrada1 != '\n' and entrada2 != '\n'):
                     if(entrada1 <= entrada2 and datosRestantesDeEntrada1 >= 0 and datosRestantesDeEntrada2 >= 0):
                         archivoDeSalida.write(str(entrada1) + '\n')
                         datosRestantesDeEntrada1 -= 1
                         if(datosRestantesDeEntrada1 >= 0):
                             entrada1 = archivoDeEntrada1.readline()
                             if(entrada1.split()):
                                 entrada1 = int(entrada1)
                         elif(datosRestantesDeEntrada1 == -1):
                             entrada1 = ''
                     elif(entrada2 < entrada1 and datosRestantesDeEntrada1 >= 0 and datosRestantesDeEntrada2 >= 0):
                         archivoDeSalida.write(str(entrada2) + '\n')
                         datosRestantesDeEntrada2 -= 1
                         if(datosRestantesDeEntrada2 >= 0):
                             entrada2 = archivoDeEntrada2.readline()
                             if(entrada1.split()):
                                entrada2 = int(entrada2)
                         elif(datosRestantesDeEntrada2 == -1):
                             entrada2 = ''
                 elif(datosRestantesDeEntrada1 == -1 and datosRestantesDeEntrada2 >= 0 and entrada2 != '' and entrada2 != '\n' and entrada2 != '\r\n'):
                     while datosRestantesDeEntrada2 >= 0:
                         if(entrada2 != ''):
                             archivoDeSalida.write(str(entrada2) + '\n')
                         datosRestantesDeEntrada2 -= 1
                         if(datosRestantesDeEntrada2 >= 0):
                             entrada2 = archivoDeEntrada2.readline()
                             if(entrada2.split()):
                                 entrada2 = int(entrada2)
                 elif(datosRestantesDeEntrada2 == -1 and datosRestantesDeEntrada1 >= 0 and entrada1 != '' and entrada1 != '\n' and entrada1 != '\r\n'):
                     while datosRestantesDeEntrada1 >= 0:
                         if(entrada1 != ''):
                             archivoDeSalida.write(str(entrada1) + '\n')
                         datosRestantesDeEntrada1 -= 1
                         if(datosRestantesDeEntrada1 >= 0):
                             entrada1 = archivoDeEntrada1.readline()
                             if(entrada1.split()):
                                 entrada1 = int(entrada1)
                 elif(datosRestantesDeEntrada1 == -1 and datosRestantesDeEntrada2 == -1):
                     datosRestantesDeEntrada1 = cantidadDatos - 1
                     datosRestantesDeEntrada2 = cantidadDatos - 1
                     entrada1 = archivoDeEntrada1.readline()
                     if(entrada1.split()):
                         entrada2 = int(entrada2)
                 elif((entrada1 == '' or entrada1 == '\n') and (entrada2 != '' and entrada2 !='\n')):
                     archivoDeSalida.write(str(entrada2) + '\n')
                     entrada2 = archivoDeEntrada2.readline()
                     if(entrada2.split()):
                        entrada2 = int(entrada2)
                 elif((entrada2 == '' or entrada2 == '\n') and (entrada1 != '' and entrada1 != '\n')):
                     archivoDeSalida.write(str(entrada1) + '\n')
                     entrada1 = archivoDeEntrada1.readline()
                     if(entrada1.split()):
                         entrada1 = int(entrada1)
                         
random.seed(1)
lista = [numero for numero in range(1,800)]
with open('datos,txt', 'w') as archivo:
    for elemento in lista:
        archivo.write(str(elemento) + '\n')

dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 1)
unir_archivos("salida1.txt","salida2.txt","datos.txt", 1)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 2)
unir_archivos("salida1.txt","salida2.txt","datos.txt", 2)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 4)
unir_archivos("salida1.txt","salida2.txt","datos.txt", 4)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 8)
unir_archivos("salida1.txt","salida2.txt","datos.txt", 8)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 16)
unir_archivos("salida1.txt","salida2.txt","datos.txt", 16)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 32)
unir_archivos("salida1.txt","salida2.txt","datos.txt", 32)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 64)
unir_archivos("salida1.txt","salida2.txt","datos.txt", 64)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 128)
unir_archivos("salida1.txt","salida2.txt","datos.txt", 128)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 256)
unir_archivos("salida1.txt","salida2.txt","datos.txt", 256)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 512)
unir_archivos("salida1.txt","salida2.txt","datos.txt", 512)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 1024)
unir_archivos("salida1.txt","salida2.txt","datos.txt", 1024)                     
                     
                         
                 
                 
                             
                         
                         
                         
                 
                 
             
             
             
