# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 14:31:26 2014

@author: paralela
"""
import numpy as np
from StringIO import StringIO
import time
from mpi4py import MPI
from pylab import *
import matplotlib.pyplot as plt

starting_point=time.time()

#Explicacion paralelo
#Para cada procesador ingresado por el terminal, ya sea "np"=4 o "np"=12 va a funcionar de la misma forma,
#la distribución para que los "np" procesadores, será dividir la cantidad total de datos 
#por la cantidad de procesado, dejandolos de forma pareja. En el caso que sobren será asignado para
#el ultimo procesador. A continuación se describiran brevemente que realizarán cada función


comm = MPI.COMM_WORLD  # comunicador entre dos procesadores
rank = comm.rank     # id procesador actual
size = comm.size     # cantidad de procesadores a usar

# En esta funcion se mandara a cada procesador la cantidad de datos con la que trabajaran
# Si sobran datos para que sean parejos, se le asignara al ultimo procesador
def distribuirEnP(size):
    if (rank==0):
        cuoc= (20*20)/size #c : cuociente
        rest= (20*20)%size #r : resto
        conta=0
        for p in range (size):
            if (p+1)!=size:
                conta=conta+cuoc
                comm.send (conta, dest = p)
            else:
                conta=conta+cuoc+rest
                comm.send (conta, dest = p)

# El procesador 0 recibirá las cantidad de datos con la que trabajará 
# cada procesador para devolver los indice i y j hasta donde operará
def buscarRangoFinal(size):
    if rank==0:
        p=0
        conta=0
        rangos_end=[]
        valor=0
        for i in range(20):
            for j in range (20):
                if(valor==0):
                    valor=comm.recv(source=p)
                if conta==valor:
                    rangos_end = rangos_end + [i,j]
                    comm.send(rangos_end,dest=p)
                    rangos_end=[]
                    p = p + 1
                    conta = conta + 1
                    valor=0
                else:
                    conta = conta + 1



# Se buscará de forma horizontal hacia la derecha completar el rango dado por los argumentos
# el valor de "c" ayudará a calcular sin tener que moverse en la posición del indice
# en donde se empieza a calcular, para posteriormente, retornar el valor mayor y una lista
# que esta compuesta consecutivamente por lso indices y valor del primer valor
# hasta el 4to valor, que contribuyen a los cuatros valores que la productoria
# será la mayor, en este caso solo horizontal. Hay diversos condicionales "if" dado
# a las excepciones que se han encontrado para movernos en los rangos 
def buscarHorizontal(ini,fin):
    i=0
    j=0
    c=0
    multi=1
    valor_mayor=-1
    lista= []
    lista_mayor=[]
    aux=-1
    if size==1:
        ini=[0,0]
        fin=[19,19]
    if ini[1]>=17:
        if ini[0] != 19:
            ini[0]=ini[0]+1
        ini[1]=0
    #fin[1] se extiende a 19 para poder recorrer la matriz
    if fin[1]!=19:
            aux_fin1=fin[1]
            fin[1]=19
    for i in range (ini[0],fin[0]+1):
        # arreglar limites ini: [x, 12] fin: [x, 5]
        # dado que no ingresara al segundo ciclo
        if ini[1]>=fin[1]:
            aux=fin[1]
            fin[1]=19
        if i== fin[0] and aux!=-1:
            fin[1]=aux
        #Restaurar fin[1] cuando este era distinto a 19 y se haya echo el cambio anteriormente
        if i==fin[0] and 'aux_fin1' in locals():
            fin[1]=aux_fin1
        for j in range (ini[1],fin[1]+1):
            if j<17:
                for c in range (4):
                    if c==0:
                        lista=[]
                    lista=lista+ [i,j+c,data[i][j+c]]
                    multi=multi*data[i][j+c]
                result=multi
                multi=1
                if (result>valor_mayor):
                    valor_mayor=result
                    lista_mayor=[]
                    lista_mayor=lista
                else:
                    lista=[]
        ini[1]=0
        #Modificación para el arreglo
        if aux != -1:
            ini[1]=0
    return (valor_mayor,lista_mayor)

# Al igual que la funcion anterior, la funcion buscarVertical, hará la búsqueda
# de forma vertical hacia abajo, para no repetir operaciónes y hasta i=17         
def buscarVertical(ini,fin):
    i=0
    j=0
    c=0
    multi=1
    valor_mayor=-1
    lista= []
    lista_mayor=[]
    aux=-1
    if size==1:
        ini=[0,0]
        fin=[19,19]
#    print "ini: " + str(ini)
#    print "fin: " + str(fin)
#    print "ini: " + str(ini)+ " - fin: " + str(fin)
    # Modificación si hay llegamos al limite para trabajar 
    if ini[0]>=17:
        lista_mayor=np.zeros(1)
        return lista_mayor
    # Modificación si hay llegamos al limite para trabajar 
    if ini[1]>=17:
        if ini[0] != 19:
            ini[0]=ini[0]+1
        ini[1]=0
    #fin[0] se extiende de 0 para poder recorrer la matriz
    if fin[0]!=0:
        aux_fin0=ini[1]
    #fin[1] se extiende a 19 para poder recorrer la matriz
    if fin[1]!=19:
        aux_fin1=fin[1]
        fin[1]=19
    for i in range (ini[0],fin[0]+1):
        # arreglar limites ini: [x, 12] fin: [x, 5]
        if ini[1]>=fin[1]:
            aux=fin[1]
            fin[1]=19
        if i== fin[0] and aux!=-1:
            fin[1]=aux
        # Fin arreglo
        #Modificar fin[0] bajarlo a 0 para recurrer fila
        if j==19 and 'aux_fin0' in locals():
            ini[1]=0
        #Restaurar fin[0] para terminar
        if i==fin[0] and 'aux_fin0' in locals():
            ini[1]=0
        #Restaurar fin[1] cuando este era distinto a 19 y se haya echo el cambio anteriormente
        if i==fin[1] and 'aux_fin1' in locals():
            fin[1]=aux_fin1

        for j in range (ini[1],fin[1]+1):
            if i<17:
                for c in range (4):
                    if c==0:
                        lista=[]
                    lista=lista+ [i+c,j,data[i+c][j]]
                    multi=multi*data[i+c][j]
                result=multi
                multi=1
                if (result>valor_mayor):
                    valor_mayor=result
                    lista_mayor=[]
                    lista_mayor=lista
                else:
                    lista=[]
        #Modificación para el arreglo
        if aux != -1:
            ini[1]=0
    return (valor_mayor,lista_mayor)

# Esta función cumple el mismo principio de busqueda que las dos funciones
# anteriores variando solo la variable "c" y limitando filas y columnas hasta 
# los casilleros 17

def buscarDiagonalDer(ini,fin):
    i=0
    j=0
    c=0
    multi=1
    valor_mayor=-1
    lista= []
    lista_mayor=[]
    aux=-1
    if size==1:
        ini=[0,0]
        fin=[19,19]
    # Modificación si hay llegamos al limite para trabajar 
    if ini[0]>=17:
        lista_mayor=np.zeros(1)
        return lista_mayor
    # Modificación si hay llegamos al limite para trabajar 
    if ini[1]>=17:
        lista_mayor=np.zeros(1)
        return lista_mayor
    #fin[1] se extiende a 19 para poder recorrer la matriz
    if fin[1]!=19:
        aux_fin1=fin[1]
        fin[1]=19
    for i in range (ini[0],fin[0]+1):
        # arreglar limites ini: [x, 12] fin: [x, 5]
        if ini[1]>=fin[1]:
            aux=fin[1]
            fin[1]=19
        if i==fin[0] and aux!=-1:
            fin[1]=aux
        # Fin arreglo
        #Restaurar fin[1] cuando este era distinto a 19 y se haya echo el cambio anteriormente
        if i==fin[1] and 'aux_fin1' in locals():
            fin[1]=aux_fin1

        for j in range (ini[1],fin[1]+1):
            if i<17 and j<17:
                for c in range (4):
                    if c==0:
                        lista=[]
                    lista=lista+ [i+c,j+c,data[i+c][j+c]]
                    multi=multi*data[i+c][j+c]
                result=multi
                multi=1
                if (result>valor_mayor):
                    valor_mayor=result
                    lista_mayor=[]
                    lista_mayor=lista
                else:
                    lista=[]
        # arreglar limites ini: [x, 5] en el ciclo "j"
        if ini[1]>=0:
            ini[1]=0
        # Fin arreglo
        #Modificación para el arreglo
        if aux != -1:
            ini[1]=0
    return (valor_mayor,lista_mayor)

# Esta función cumple el mismo principio de busqueda que las dos funciones
# anteriores variando solo la variable "c" y limitando filas y columnas hasta 
# los casilleros 17
def buscarDiagonalIzq(ini,fin):
    i=0
    j=0
    c=0
    multi=1
    valor_mayor=-1
    lista= []
    lista_mayor=[]
    aux=-1
    if size==1:
        ini=[0,0]
        fin=[19,19]
    # No permite empezar con los primeros datos
    if ini[0]<=2:
        ini[0]=3
        if ini[0]>fin[0] or (ini[0]==fin[0] and ini[1]>=fin[1]):
            lista_mayor=np.zeros(1)
            return lista_mayor
    if ini[0]>=17:
        lista_mayor=np.zeros(1)
        return lista_mayor
    if ini[1] == 19:
        ini[0]=ini[0]+1
        ini[1]=0
    #fin[1] se extiende a 19 para poder recorrer la matriz
    if fin[1]!=19:
        aux_fin1=fin[1]
        fin[1]=19
    for i in range (ini[0],fin[0]+1):
        # arreglar limites ini: [x, 12] fin: [x, 5]
        if ini[1]>=fin[1]:
            aux=fin[1]
            fin[1]=19
        if i==fin[0] and aux!=-1:
            fin[1]=aux
        # Fin arreglo
        #Restaurar fin[1] cuando este era distinto a 19 y se haya echo el cambio anteriormente
        if i==fin[1] and 'aux_fin1' in locals():
            fin[1]=aux_fin1

        for j in range (ini[1],fin[1]+1):
            if i>2 and j>2 and i<17:
                for c in range (4):
                    lista=lista+[i+c,j-c,data[i+c][j-c]]
                    multi=multi*data[i+c][j-c]
                result=multi
                multi=1
                if (result>valor_mayor):
                    valor_mayor=result
                    lista_mayor=[]
                    lista_mayor=lista
                    lista=[]
                else:
                    lista=[]
        # arreglar limites ini: [x, 5] en el ciclo "j"
        if ini[1]>=0:
            ini[1]=0
        # Fin arreglo
        #Modificación para el arreglo
        if aux != -1:
            ini[1]=0
    if valor_mayor==-1:
        return (0,lista_mayor)
    return (valor_mayor,lista_mayor)

# Recibe los resultados de cada busqueda y devuelve el de mayor resultado
def comparar (horizontal,vertical,diagonalDer,diagonalIzq):
    if(horizontal[0]>vertical[0] and horizontal[0]>diagonalDer[0] and horizontal[0]>diagonalIzq[0]):
        return horizontal
    else:
        if(vertical[0]>diagonalDer[0] and vertical[0]>horizontal[0] and vertical[0]>diagonalIzq[0]):
            return vertical
        else:
            if(diagonalDer[0]>vertical[0] and diagonalDer[0]>horizontal[0] and diagonalDer[0]>diagonalIzq[0]):
                return diagonalDer
            else:
                if(diagonalIzq[0]>vertical[0] and diagonalIzq[0]>horizontal[0] and diagonalIzq[0]>diagonalDer[0]):
                    return diagonalIzq

def leerTiempoSerial():
    archi=open('SerialTime.txt','r')
    linea=archi.readline()
    archi.close()
    return linea



#-------------MAIN--------------------- 

# Se comenzará por generar la una matriz a partir de lso datos entregados
# en un archivo txt

pfile=open('Tarea3.txt','r')
data=pfile.read()
pfile.close()

# Se sobre entiende que los delimitadores son espacios
data=np.genfromtxt(StringIO(data))

# El procesador 0 estará a cargo de mandar la cantidad de datos 
# para cada procesador
if rank==0:
    distribuirEnP(size)

# Recibe la cantidad de datos en cada procesador
rango=comm.recv(source=0)
rango=rango-1
comm.send(rango,dest=0)

# Con la cantidad de datos se buscara el rango donde terminara de procesar en la matriz
if rank==0:
    buscarRangoFinal(size)

# Con la posición de termino se mandarán como punto de inicio para los procesadores siguientes
# Primero se inicia el procesador 1
fin = comm.recv(source=0)
if size != 1:
    if rank==0:
        ini=[0,0]
        i=1
        if size>0:
            comm.send(fin,dest=1)
else:
    ini=[0,0]
    comm.send(fin,dest=0)

# Hasta los p procesadores
if size != 1:
    if rank !=0:
        ini=comm.recv(source=rank-1)
        if (rank+1)<size:
            comm.send(fin,dest=rank+1)
else:
    ini=comm.recv(source=0)

horizontal=buscarHorizontal(ini,fin)
#print "Horiz "+str(rank)+ ": " + str(horizontal)
vertical=buscarVertical(ini,fin)
#print "Verti "+str(rank)+ ": " + str(vertical)
diagonalDer=buscarDiagonalDer(ini,fin)
#print "DiDer "+str(rank)+ ": " + str(diagonalDer)
diagonalIzq=buscarDiagonalIzq(ini,fin)
#print "DiIzq "+str(rank)+ ": " + str(diagonalIzq)


##Cada procesador obtiene su "mejor"
mejor=comparar(horizontal,vertical,diagonalDer,diagonalIzq)
#print "Rank "+str(rank)+" : "+str(mejor)
#Se enviará los mejores al rank=0 para determinar cual es el mejor
comm.send(mejor,dest=0)
if rank==0:
    optimo=0
    list_optimo=[]
    for rank in range (size):
        mejor=comm.recv(source=rank)
        if mejor[0]>optimo:
            optimo=mejor[0]
            list_optimo=mejor
    print ""
    print "--Result-For n="+str(size)
    print ""
    print "Matriz["+str(list_optimo[1][0])+"]["+str(list_optimo[1][1])+"]="+str(list_optimo[1][2])
    print "Matriz["+str(list_optimo[1][3])+"]["+str(list_optimo[1][4])+"]="+str(list_optimo[1][5])
    print "Matriz["+str(list_optimo[1][6])+"]["+str(list_optimo[1][7])+"]="+str(list_optimo[1][8])
    print "Matriz["+str(list_optimo[1][9])+"]["+str(list_optimo[1][10])+"]="+str(list_optimo[1][11])

    print str(list_optimo[1][2])+" x "+str(list_optimo[1][5])+" x "+str(list_optimo[1][8])+" x "+str(list_optimo[1][11])+" = "+str(list_optimo[0])


#    Calculo de tiempo
    elapsed_time=time.time()-starting_point
    elapsed_time_int = int(elapsed_time)
    print ""
    print "Parallel Time [seconds]: " + str(elapsed_time)
#    elapsed_time_minutes = elapsed_time_int/60
#    elapsed_time_seconds = elapsed_time_int%60
#    print "Time [min:sec]: "+ str(elapsed_time_minutes) + ":" + str(elapsed_time_seconds)

    SerialTime=leerTiempoSerial()
    print "Serial   Time [seconds]: " + str(SerialTime)
    VectorTiempo=[SerialTime,elapsed_time]
    VectorN=[1,size]

    #Generador de grafico
    fig = plt.figure()
    fig.suptitle(u'Tarea 3 de Computación Paralela - UTEM', fontsize=14, fontweight='bold')
    
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    
    if float(VectorTiempo[0])>float(VectorTiempo[1]):
        valor=float(VectorTiempo[1])/float(VectorTiempo[0])*100
        ax.set_title(u'Entre 1 y '+str(size)+' procesadores hubo una mejora de ' + str(valor)+'%')
    else:
        if float(VectorTiempo[0])<float(VectorTiempo[1]):
            valor=float(VectorTiempo[1])/float(VectorTiempo[0])*100
            ax.set_title(u'Entre 1 y '+str(size)+'procesadores hubo un deterioro de ' + str(valor)+'%')
        else:
            ax.set_title(u'Entre 1 y '+str(size)+' procesadores no hubo mejora')
        
    
    ax.set_xlabel(u'Número de procesadores')
    ax.set_ylabel('Tiempo [Segundos]')
        
    x =     VectorN
    y =     VectorTiempo
    ax.plot(x, y, 'o')
    ax.plot(0.5,float(SerialTime), '-')
    ax.plot(size+0.5,float(elapsed_time), '-')
    
    plt.show()
