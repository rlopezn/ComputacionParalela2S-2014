# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 14:31:26 2014

@author: paralela
"""
import numpy as np
from StringIO import StringIO
from random import randint
import random

def llenarMatriz(fila,columna):
    matriz=np.random.randint(99, size=(fila,columna))
    return matriz
    
    
    
#----------MAIN--------------------------
 
#----datos iniciales---------------------  

filaMatriz=20
columnaMatriz=20
print "Matriz : ["+str(filaMatriz)+"]["+str(columnaMatriz)+"]"
matriz=llenarMatriz(filaMatriz,columnaMatriz)
print matriz
