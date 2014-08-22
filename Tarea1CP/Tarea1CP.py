import time
def contador(resultado):
	if resultado<10:
		return resultado
	else :
		return contador(int(resultado/10))+ resultado%10
def menor100(num):
	if num>100:
		while (num>100):
			num = int (input ("Numeros menores que 100 \n "))
		return num
	else :
		return num

numero= int(input("Ingresar la base a^b \n " ))
numero = menor100(numero)
numero2 = int(input("Ingresar exponente a^b \n"))
numero2 = menor100(numero2)
potencia = numero**numero2
suma = contador(potencia)
print("Suma digital")
print(suma)
time.sleep(5.5) 
