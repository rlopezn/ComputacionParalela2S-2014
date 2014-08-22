import time
# suma los digitos uno por uno , de forma recursiva
def contador(resultado):
	if resultado<10:
		return resultado
	else :
		return contador(int(resultado/10))+ resultado%10
# verifica que el valor ingresado sea menor que 100 (el enunciado de la tarea lo pide asi)
def menor100(num):
	if num>100:
		while (num>100):
			num = int (input ("Numeros menores que 100 \n "))
		return num
	else :
		return num
#Ingresa  valor de a
numero= int(input("Ingresar a \n " ))
numero = menor100(numero)
#ingresa el valor de b
numero2 = int(input("Ingresar b \n"))
numero2 = menor100(numero2)
#calcula la potencia
potencia1 = numero**numero2
potencia2 = numero2**numero 
# recibe la suma de la funcion contador
suma1= contador(potencia1)
suma2= contador(potencia2)
#decide cual es mayor
if(suma1<suma2):
	print("Suma digital maxima pertenece  a b^a \n ")
	print(suma2)
elif(suma1== suma2):
	print("Suma digital es la misma para ambos casos y es\n ")
	print(suma2)
else:
	print("suma digital maxima pertenece a b^a \n")
	print(suma1)
	
time.sleep(5.5) 
