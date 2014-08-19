'''
Created on 18/08/2014

@author: macbookpro
'''



import numpy as np
from StringIO import StringIO
import random


def contarUnosMatriz(fila,columna,matriz):
    contador=1
    for i in range(fila):
        for j in range(columna):
            if(matriz[i][j]==1):
                contador+=1
    return contador
                

def llenarMatrizProbabilidad(fila,columna,matriz,probabilidad):
    cantPuntos=fila*columna
    prob=probabilidad/100.0
    print "probabilidad"+str(prob)
    cantLlenarPuntos=int(prob*cantPuntos)
    print "cantLLenas :"+str(cantLlenarPuntos)
    print str(cantLlenarPuntos)
    i=1
    while(i<cantLlenarPuntos):
        aleatorioX=random.randrange(fila)
        aleatorioY=random.randrange(columna)
        if(matriz[aleatorioX][aleatorioY]==0):
            matriz[aleatorioX][aleatorioY]=1
            i+=1
    return matriz
              
#----------MAIN-----------------              
filaMatriz=10
columnaMatriz=10
print "Matriz : ["+str(filaMatriz)+"]["+str(columnaMatriz)+"]"
matrizCeros=np.zeros((filaMatriz,columnaMatriz))
print matrizCeros
matrix=llenarMatrizProbabilidad(filaMatriz,columnaMatriz,matrizCeros,80)
print "cantidad de unos :"+str(contarUnosMatriz(filaMatriz,columnaMatriz,matrix))
print matrix
#print matrix






print "hola mundo"