__author__ = 'macbookpro'

class Mapa:
    def __init__(self,matriz):
        self.mapa=matriz
        print "MAPA"
        print self.mapa
        #self.mapa=open(archivo,"r")
        self.fil = len(self.mapa)
        self.col = len(self.mapa[0])

    def __str__(self):
        salida = ""
        for f in range(self.fil):
            for c in range(self.col):
                if self.mapa[f][c] == 0:
                    salida += "  "
                if self.mapa[f][c] == 1:
                    salida += "0 "
                if self.mapa[f][c] == 2:
                    salida += "2 "
                if self.mapa[f][c] == 3:
                    salida += "3 "
                if self.mapa[f][c] == 4:
                    salida += "1 "
            salida += "\n"
        return salida

    def camino(self, lista):
        del lista[-1]
        for i in range(len(lista)):
            self.mapa[lista[i][0]][lista[i][1]] = 4

