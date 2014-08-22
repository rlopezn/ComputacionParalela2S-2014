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
#Ingresa primer valor de la potencia, la base
numero= int(input("Ingresar la base a^b \n " ))
numero = menor100(numero)
#ingresa el exponente 
numero2 = int(input("Ingresar exponente a^b \n"))
numero2 = menor100(numero2)
#calcula la potencia
potencia = numero**numero2
# recibe la suma de la funcion contador
suma = contador(potencia)
print("Suma digital")
print(suma)
time.sleep(5.5) 
