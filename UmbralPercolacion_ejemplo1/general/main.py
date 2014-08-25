'''
Created on 18/08/2014

@author: macbookpro
'''



import numpy as np
from StringIO import StringIO
import random
import matplotlib.pyplot as plt



def contarUnosMatriz(fila,columna,matriz):
    contador=1
    for i in range(fila):
        for j in range(columna):
            if(matriz[i][j]==1):
                contador+=1
    return contador
                

def llenarMatrizProbabilidad(fila,columna,probabilidad):
    matriz=np.zeros((filaMatriz,columnaMatriz))
    cantPuntos=fila*columna
    prob=probabilidad/100.0
    print "probabilidad de llenado : "+str(prob)
    cantLlenarPuntos=int(prob*cantPuntos)
    print "cantidad puntos por LLenar :"+str(cantLlenarPuntos)
    i=1
    while(i<cantLlenarPuntos):
        aleatorioX=random.randrange(fila)
        aleatorioY=random.randrange(columna)
        if(matriz[aleatorioX][aleatorioY]==0):
            matriz[aleatorioX][aleatorioY]=1
            i+=1
    return matriz

def graficoPercolacion(matriz,ax):
    ax.imshow(matriz,cmap=plt.cm.gray,interpolation='nearest') #nearest
    ax.set_title('Umbral Percolacion')
    # Move left and bottom spines outward by 10 points
    ax.spines['left'].set_position(('outward', 10))
    ax.spines['bottom'].set_position(('outward', 10))
    # Hide the right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')#bottom
    plt.show()

#----------MAIN-----------------    
  #--datos iniciales-----        
filaMatriz=10
columnaMatriz=10
probLlenado=80
print "Matriz : ["+str(filaMatriz)+"]["+str(columnaMatriz)+"]"
matrix=llenarMatrizProbabilidad(filaMatriz,columnaMatriz,probLlenado)
print "cantidad de unos(contar) :"+str(contarUnosMatriz(filaMatriz,columnaMatriz,matrix))
print matrix

#print matrix

#---------Graficas------------------------
# 1 es blanco - 0 es negro
fig, ax = plt.subplots()
graficoPercolacion(matrix,ax)
#-------------------------------------------