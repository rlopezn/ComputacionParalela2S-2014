# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 14:31:26 2014

@author: paralela
"""
import numpy as np
from StringIO import StringIO 
import time
from mpi4py import MPI

starting_point=time.time()

#Explicacion serial
#Para cada procesador ingresado por el terminal, ya sea "np"=4 o "np"=12 va a funcionar de la misma forma,
#la distribución para que los "np" procesadores, será dividir la cantidad total de datos 
#por la cantidad de procesado, dejandolos de forma pareja. En el caso que sobren será asignado para
#el ultimo procesador. A continuación se describiran brevemente que realizarán cada función


comm = MPI.COMM_WORLD  # comunicador entre dos procesadores
rank =  comm.rank     # id procesador actual 
size =  comm.size     # cantidad de procesadores a usar

# En esta funcion se mandara a cada procesador la cantidad de datos con la que trabajaran
# Si sobran datos para que sean parejos, se le asignara al ultimo procesador
def distribuirEnP(size):
    print ""
    print ""
    print " Funcion distribuirenP("+str(size)+")"
    if (rank==0):
        cuoc= (20*20)/size #c : cuociente
        rest= (20*20)%size #r : resto
        conta=0
        for p in range (size):
            if (p+1)!=size:
                conta=conta+cuoc
                print "Enviar a "+str(p)+" el valor: "+str(conta)
                comm.send (conta, dest = p)
            else:
                conta=conta+cuoc+rest
                print "Enviar a "+str(p)+" el valor: "+str(conta)
                comm.send (conta, dest = p)
                
# El procesador 0 recibirá las cantidad de datos con la que trabajará 
# cada procesador para devolver los indice i y j hasta donde operará
def buscarRangoFinal(size):
    print ""
    print ""
    print " Funcion buscarRangoFinal("+str(size)+")"
    if rank==0:
        p=0
        conta=0
        rangos_end=[]
        valor=0
        for i in range(20):
            for j in range (20):
                if(valor==0):
                    valor=comm.recv(source=p)
                    #print valor
#                print "i,j = "+str(i)+","+str(j)
#                print "recv: "+ str(valor)
#                print "p = "+str(p)
#                print "conta: "+str(conta)
                if conta==valor:
                    rangos_end = rangos_end + [i,j]
                    print "Enviar a "+str(p)+" el rango: "+ str(rangos_end)
                    comm.send(rangos_end,dest=p)
                    p = p + 1
                    conta = conta + 1
                    valor=0
                else:
                    conta = conta + 1
                
            

# Se buscará de forma horizontal hacia la derecha hasta el casillero 17,
# esto es para no estarsize repitiendo operaciones y limitar el recorrido por fila
# hasta j=17
# el valor de "c" ayudará a calcular sin tener que moverse en la posición del indice
# en donde se empieza a calcular, para posteriormente, retornar el valor mayor y una lista
# que esta compuesta consecutivamente por lso indices y valor del primer valor
# hasta el 4to valor, que contribuyen a los cuatros valores que la productoria
# será la mayor, en este caso solo horizontal.
def buscarHorizontal(fin):
    i=0
    j=0
    c=0
    multi=1
    valor_mayor=-1
    lista= []
    lista_mayor=[]
    for i in range (20):
        for j in range (17):
            if i<=fin[0] and j<=fin[1]:
                for c in range (4):
                    lista=lista+ [i,j+c,data[i][j+c]]
                    multi=multi*data[i][j+c]
                result=multi
                multi=1
                if (result>valor_mayor):
                    valor_mayor=result
                    lista_mayor=lista
                else:
                    lista=[]
    return (valor_mayor,lista_mayor)   

# Al igual que la funcion anterior, la funcion buscarVertical, hará la búsqueda
# de forma vertical hacia abajo, para no repetir operaciónes y hasta i=17         
            
#def buscarVertical(info):
#    i=0
#    j=0
#    c=0
#    multi=1
#    valor_mayor=-1
#    lista= []
#    lista_mayor=[]
#    for i in range (17):
#        for j in range (20):
#            for c in range (4):
#                lista=lista+ [i+c,j,data[i+c][j]]
#                multi=multi*data[i+c][j]
#            result=multi
#            multi=1
#            if (result>valor_mayor):
#                valor_mayor=result
#                lista_mayor=lista
#            else:
#                lista=[] 
#    return (valor_mayor,lista_mayor)             
            
# Esta función cumple el mismo principio de busqueda que las dos funciones
# anteriores variando solo la variable "c" y limitando filas y columnas hasta 
# los casilleros 17
            
#def buscarDiagonal(info):
#    i=0
#    j=0
#    c=0
#    multi=1
#    valor_mayor=-1
#    lista= []
#    lista_mayor=[]
#    for i in range (17):
#        for j in range (17):
#            for c in range (4):
#                lista=lista+ [i+c,j+c,data[i+c][j+c]]
#                multi=multi*data[i+c][j+c]
#            result=multi
#            multi=1
#            if (result>valor_mayor):
#                valor_mayor=result
#                lista_mayor=lista
#            else:
#                lista=[]
#    return (valor_mayor,lista_mayor) 
    
# Recibe los resultados de cada busqueda y devuelve el de mayor resultado
#def comparar (horizontal,vertical,diagonal):
#    if(horizontal[0]>vertical[0] and horizontal[0]>diagonal[0]):
#        return horizontal
#    else:
#        if(vertical[0]>diagonal[0] and vertical[0]>horizontal[0]):
#            return vertical
#        else:
#            if(diagonal[0]>vertical[0] and diagonal[0]>horizontal[0]):
#                return diagonal
        

    
   

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
    
rango=comm.recv(source=0)
rango=rango-1
comm.send(rango,dest=0)

if rank==0:
    buscarRangoFinal(size)
    init=[0,0]
    fin = comm.recv(source=0)
    comm.send(fin,dest=rank+1)
horizontal=buscarHorizontal(fin)
print horizontal
#vertical=buscarVertical(info)
#diagonal=buscarDiagonal(info)

if rank==0:
#    mejor=comparar(horizontal,vertical,diagonal)
#    print "--Result--"
#    print ""
#    print "Matriz["+str(mejor[1][0])+"]["+str(mejor[1][1])+"]="+str(mejor[1][2])
#    print "Matriz["+str(mejor[1][3])+"]["+str(mejor[1][4])+"]="+str(mejor[1][5])
#    print "Matriz["+str(mejor[1][6])+"]["+str(mejor[1][7])+"]="+str(mejor[1][8])
#    print "Matriz["+str(mejor[1][9])+"]["+str(mejor[1][10])+"]="+str(mejor[1][11])
#    print ""
#    print str(mejor[1][2])+" x "+str(mejor[1][5])+" x "+str(mejor[1][8])+" x "+str(mejor[1][11])+" = "+str(mejor[0])
            
    
#    Calculo de tiempo
    elapsed_time=time.time()-starting_point
    elapsed_time_int = int(elapsed_time)
    print ""
    print "Time [seconds]: " + str(elapsed_time)
    elapsed_time_minutes = elapsed_time_int/60
    elapsed_time_seconds = elapsed_time_int%60
    print "Time [min:sec]: "+ str(elapsed_time_minutes) + ":" + str(elapsed_time_seconds)
    print ""
    print ""