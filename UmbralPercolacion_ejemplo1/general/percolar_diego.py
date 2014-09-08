# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 14:07:55 2014

@author: paralela
"""

import numpy as np
from StringIO import StringIO
import random
import matplotlib.pyplot as plt

import networkx as nx

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
    
def buscarCamino(matrix):
    cantCaminos=0
    return cantCaminos
            

                
            
    
#----------MAIN--------------------------
 
#----datos iniciales---------------------  
filaMatriz=10
columnaMatriz=10
probLlenado=70
print "Matriz : ["+str(filaMatriz)+"]["+str(columnaMatriz)+"]"
matrix=llenarMatrizProbabilidad(filaMatriz,columnaMatriz,probLlenado)
#print "cantidad de unos(contar) :"+str(contarUnosMatriz(filaMatriz,columnaMatriz,matrix))
print matrix


#---------Graficas------------------------
# 1 es blanco - 0 es negro
fig, ax = plt.subplots()
graficoPercolacion(matrix,ax)
#-----------------------------------------

G = nx.from_numpy_matrix(mlow, high=None, size=Noneatrix, create_using=nx.DiGraph())
print(nx.dijkstra_path(G, 0, 1))





