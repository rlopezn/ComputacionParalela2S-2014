# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 14:31:26 2014

@author: paralela
"""
import numpy as np
from random import randint
import random
from StringIO import StringIO 

#def llenarMatriz(fila,columna):
#    matriz=np.random.randint(99, size=(fila,columna))
#    return matriz
#    
def buscarHorizontal():
    i=0
    j=0
    menor=-1
    for i in range (20):
        for j in range (16):
            print "data["+str(i)+"]["+str(j)+"]="+str(data[i][j])
            
            
    
    
#----------MAIN--------------------------
 
#----datos iniciales---------------------  

pfile=open('Tarea3.txt','r')
data=pfile.read()
pfile.close()
data=np.genfromtxt(StringIO(data)) #Se sobre entiende que los 
                                   #delimitadores son espacios

#filaMatriz=20
#columnaMatriz=20
#print "Matriz : ["+str(filaMatriz)+"]["+str(columnaMatriz)+"]"
#matriz=llenarMatriz(filaMatriz,columnaMatriz)
##print matriz
#
buscarHorizontal()
