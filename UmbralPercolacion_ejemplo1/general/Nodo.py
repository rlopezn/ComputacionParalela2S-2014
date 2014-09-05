__author__ = 'macbookpro'



def distancia(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) #Valor absoluto.



class Nodo:
    def __init__(self, pos=[0, 0], padre=None):
        self.pos = pos
        self.padre = padre
        self.h = distancia(self.pos, pos_f)

        if self.padre == None:
            self.g = 0
        else:
            self.g = self.padre.g + 1
        self.f = self.g + self.h

