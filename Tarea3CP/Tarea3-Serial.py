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
    c=0
    multi=1
    valor_mayor=-1
    i_mayor=0
    j_mayor=0
    for i in range (20):
        for j in range (17):
            for c in range (4):
                #print "data["+str(i)+"]["+str(j)+"]="+str(data[i][j])
                #print "["+str(i)+"]["+str(c+j)+"]="+str(data[i][c+j])
                multi=multi*data[i][j+c]
            result=multi
            #print "multi: "+ str(result)
            multi=1
            if (result>valor_mayor):
                valor_mayor=result
                i_mayor=i
                j_mayor=j
    #print "---indice mayor horizontal: ["+str(i_mayor)+"]["+str(j_mayor)+"]= "+str(data[i_mayor][j_mayor])+" y el valor es "+str(valor_mayor)
    return (i_mayor,j_mayor,data[i_mayor][j_mayor],valor_mayor)            
            
def buscarVertical():
    i=0
    j=0
    c=0
    multi=1
    valor_mayor=-1
    i_mayor=0
    j_mayor=0
    for i in range (17):
        for j in range (20):
            for c in range (4):
                #print "data["+str(i)+"]["+str(j)+"]="+str(data[i][j])
                #print "["+str(i+c)+"]["+str(j)+"]="+str(data[i+c][j])
                multi=multi*data[i+c][j]
            result=multi
            #print "multi: "+ str(result)
            multi=1
            if (result>valor_mayor):
                valor_mayor=result
                i_mayor=i
                j_mayor=j
    #print "---indice mayor horizontal: ["+str(i_mayor)+"]["+str(j_mayor)+"]= "+str(data[i_mayor][j_mayor])+" y el valor es "+str(valor_mayor)
    return (i_mayor,j_mayor,data[i_mayor][j_mayor],valor_mayor)             
            
    
    
#----------MAIN--------------------------
 
#----datos iniciales---------------------  

pfile=open('Tarea3.txt','r')
data=pfile.read()
pfile.close()
print""
#se sobre entiende que los delimitadores son espacios
data=np.genfromtxt(StringIO(data)) 

indice_horizontal=buscarHorizontal()
print "Horizontal : (i,j,valor,total) = "+ str(indice_horizontal)

indice_vertical=buscarVertical()
print "Vertical   : (i,j,valor,total) = "+ str(indice_vertical)
#print data
