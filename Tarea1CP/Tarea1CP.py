import time

def factor_primo(n):
    factor = 1
    # Eliminar cualquier factor de 2
    while n % 2 ==0:
        factor = 2
        n = n/2

    # Eliminar el resto de los factores impares
    p = 3
    while n != 1:
        while n % p == 0:
            factor = p
            n = n/p
        p+=2

    return factor

start = time.time()
for i in range (100) : a = factor_primo (600851475143)

    #Calculo de tiempo de ejecucion

tiempo = (time.time() - start)
print "El resultado %s ha retornado despues de %s segundos luego de 100 iteraciones. " % (a, tiempo)    


