import time
# suma los digitos uno por uno , de forma recursiva
def contador(resultado):
	if resultado<10:
		return resultado
	else :
		return contador(int(resultado/10))+ resultado%10

#Ingresa  valor de a
numero= 0
numaux1=0
#ingresa el valor de b
numero2 = 0
numaux2=0
aux = 0
#itera los valores de a y b
while (numero<100):
	numero2=0
	while (numero2<100):
		potencia = numero**numero2 
		if (aux<contador(potencia)):
			aux = contador(potencia)
			numaux = numero
			numaux2 = numero2
		numero2 =numero2 + 1
		
	numero = numero + 1
print("la suma digital maxima para a^b" )
print("a: \n")
print(numaux)
print("b: \n")
print(numaux2)
print("la suma es \n")
print(aux)

time.sleep(5.5) 
