


from random import randint
import random

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
            
            

def dividir_archivo(archivo_entrada, archivo_salida1, archivo_salida2, cant_datos):
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
                print(entrada1)
                print(entrada2)
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
                             if (entrada1.split()):
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





random.seed(1)
lista= [numero for numero in range(1, 800)]
#random.shuffle(lista)
with open('datos.txt', 'w') as f:
    for elemento in lista:
        f.write(str(elemento) + '\n')

dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 1)
unir_archivo("salida1.txt", "salida2.txt", "datos.txt", 1)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 2)
unir_archivo("salida1.txt", "salida2.txt", "datos.txt", 2)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 4)
unir_archivo("salida1.txt", "salida2.txt", "datos.txt", 4)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 8)
unir_archivo("salida1.txt", "salida2.txt", "datos.txt", 8)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 16)
unir_archivo("salida1.txt", "salida2.txt", "datos.txt", 16)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 32)
unir_archivo("salida1.txt", "salida2.txt", "datos.txt", 32)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 64)
unir_archivo("salida1.txt", "salida2.txt", "datos.txt", 64)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 128)
unir_archivo("salida1.txt", "salida2.txt", "datos.txt", 128)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 256)
unir_archivo("salida1.txt", "salida2.txt", "datos.txt", 256)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 512)
unir_archivo("salida1.txt", "salida2.txt", "datos.txt", 512)
dividir_archivo("datos.txt", "salida1.txt", "salida2.txt", 1024)
unir_archivo("salida1.txt", "salida2.txt", "datos.txt", 1024)