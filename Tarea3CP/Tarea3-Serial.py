# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 14:31:26 2014

@author: paralela
"""
import numpy as np
from StringIO import StringIO 


def buscarHorizontal():
    i=0
    j=0
    c=0
    multi=1
    valor_mayor=-1
    i_mayor=0
    j_mayor=0
    lista= []
    lista_mayor=[]
    for i in range (20):
        for j in range (17):
            for c in range (4):
                lista=lista+ [i,j+c,data[i][j+c]]
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
                lista_mayor=lista
                #print "---indice mayor horizontal: ["+str(i_mayor)+"]["+str(j_mayor)+"]= "+str(data[i_mayor][j_mayor])+" y el valor es "+str(valor_mayor)
            else:
                lista=[]
    #return (i_mayor,j_mayor,data[i_mayor][j_mayor],valor_mayor,lista_mayor) 
    return (valor_mayor,lista_mayor)            
            
def buscarVertical():
    i=0
    j=0
    c=0
    multi=1
    valor_mayor=-1
    i_mayor=0
    j_mayor=0
    lista= []
    lista_mayor=[]
    for i in range (17):
        for j in range (20):
            for c in range (4):
                lista=lista+ [i+c,j,data[i+c][j]]
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
                lista_mayor=lista
                #print "---indice mayor horizontal: ["+str(i_mayor)+"]["+str(j_mayor)+"]= "+str(data[i_mayor][j_mayor])+" y el valor es "+str(valor_mayor) 
            else:
                lista=[]
    #return (i_mayor,j_mayor,data[i_mayor][j_mayor],valor_mayor,lista_mayor)  
    return (valor_mayor,lista_mayor)             
            
def buscarDiagonal():
    i=0
    j=0
    c=0
    multi=1
    valor_mayor=-1
    i_mayor=0
    j_mayor=0
    lista= []
    lista_mayor=[]
    for i in range (17):
        for j in range (17):
            for c in range (4):
                lista=lista+ [i+c,j+c,data[i+c][j+c]]
                #print "data["+str(i)+"]["+str(j)+"]="+str(data[i][j])
                #print "["+str(i+c)+"]["+str(j+c)+"]="+str(data[i+c][j+c])
                multi=multi*data[i+c][j+c]
            result=multi
            #print "multi: "+ str(result)
            multi=1
            if (result>valor_mayor):
                valor_mayor=result
                i_mayor=i
                j_mayor=j
                lista_mayor=lista
                #print "---indice mayor horizontal: ["+str(i_mayor)+"]["+str(j_mayor)+"]= "+str(data[i_mayor][j_mayor])+" y el valor es "+str(valor_mayor)
            else:
                lista=[]
    #return (i_mayor,j_mayor,data[i_mayor][j_mayor],valor_mayor,lista_mayor) 
    return (valor_mayor,lista_mayor) 
    
    
def comparar (horizontal,vertical,diagonal):
    if(horizontal[0]>vertical[0] and horizontal[0]>diagonal[0]):
        return horizontal
    else:
        if(vertical[0]>diagonal[0] and vertical[0]>horizontal[0]):
            return vertical
        else:
            if(diagonal[0]>vertical[0] and diagonal[0]>horizontal[0]):
                return diagonal
        

    
   
#----------MAIN--------------------------
 
#----datos iniciales---------------------  

pfile=open('Tarea3.txt','r')
data=pfile.read()
pfile.close()
print""

#se sobre entiende que los delimitadores son espacios
data=np.genfromtxt(StringIO(data)) 

horizontal=buscarHorizontal()
#print "Horizontal : (valor total, lista) = "
#print str(horizontal)
#print ""

vertical=buscarVertical()
#print "Vertical   : (valor total, lista) = "
#print str(vertical)
#print ""

diagonal=buscarDiagonal()
#print "Diagonal   : (valor total, lista) = "
#print str(diagonal)
#print ""

mejor=comparar(horizontal,vertical,diagonal)
#print str(mejor)
print ""
print "--Resultado--"
print ""
print "Matriz["+str(mejor[1][0])+"]["+str(mejor[1][1])+"]="+str(mejor[1][2])
print "Matriz["+str(mejor[1][3])+"]["+str(mejor[1][4])+"]="+str(mejor[1][5])
print "Matriz["+str(mejor[1][6])+"]["+str(mejor[1][7])+"]="+str(mejor[1][8])
print "Matriz["+str(mejor[1][9])+"]["+str(mejor[1][10])+"]="+str(mejor[1][11])
print ""
print str(mejor[1][2])+" x "+str(mejor[1][5])+" x "+str(mejor[1][8])+" x "+str(mejor[1][11])+" = "+str(mejor[0])
        
    








