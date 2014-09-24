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
                
            

# Se buscará de forma horizontal hacia la derecha hasta el casillero 17,
# esto es para no estarsize repitiendo operaciones y limitar el recorrido por fila
# hasta j=17
# el valor de "c" ayudará a calcular sin tener que moverse en la posición del indice
# en donde se empieza a calcular, para posteriormente, retornar el valor mayor y una lista
# que esta compuesta consecutivamente por lso indices y valor del primer valor
# hasta el 4to valor, que contribuyen a los cuatros valores que la productoria
# será la mayor, en este caso solo horizontal.
def buscarHorizontal(ini,fin):
    i=0
    j=0
    c=0
    multi=1
    valor_mayor=-1
    lista= []
    lista_mayor=[]
#    print "ini: " + str(ini)
#    print "fin: " + str(fin)
    if ini[1]>=17:
#        print "--pos: "+str(i)+","+str(j)
        if ini[0] != 19:
            ini[0]=ini[0]+1
        else:
            i=fin[0]
            j=fin[1]
        ini[1]=0
    for i in range (ini[0],fin[0]+1):
#        if ini[1]>=17:
#            print "--pos: "+str(i)+","+str(j)
#            if ini[0] != 19:
#                ini[0]=ini[0]+1
#            else:
#                i=fin[0]
#                j=fin[1]
#            ini[1]=0
        for j in range (ini[1],fin[1]+1):
#            print ""
#            print "j: " + str(j)
#            print "j- ini: " + str(ini)
#            print "j- fin: " + str(fin)
#            print "pos: "+str(i)+","+str(j)
            if j<17:
                for c in range (4):
                    if c==0:
                        lista=[]
                    lista=lista+ [i,j+c,data[i][j+c]]
#                    print "["+str(i)+"]["+str(c+j)+"]="+str(data[i][c+j])
                    multi=multi*data[i][j+c]
                result=multi
#                print "multi: "+ str(result)
                multi=1
                if (result>valor_mayor):
                    valor_mayor=result
                    lista_mayor=[]
                    lista_mayor=lista
#                    print "---indice mayor horizontal: ["+str(i)+"]["+str(j)+"]= "+str(data[i][j])+" y el valor es "+str(valor_mayor)
#                    print str(valor_mayor)+" -  "+str(lista_mayor)
                else:
                    lista=[]
#            else:
#                j=19
#                print "break"
#                break
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
if rank==0:
    ini=[0,0]
    i=1
    if size>0:
        comm.send(fin,dest=1)

# Hasta los p procesadores
if rank !=0:
    ini=comm.recv(source=rank-1)
    if (rank+1)<size: 
        comm.send(fin,dest=rank+1)

print ""
#print str(rank)+" empieza : "+ str(ini)
#print str(rank)+" finaliza: "+ str(fin)


horizontal=buscarHorizontal(ini,fin)
print "Rank "+str(rank)+ ": " + str(horizontal)
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