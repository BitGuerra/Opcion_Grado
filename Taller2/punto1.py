longitud = int(input("\nDigite la cantidad de numeros que desea ingresar: "))

numeros = [0 for i in range(0,longitud)]

numero = 0
menor = 50
pos = 0

for i in range(0,longitud):

	numero = float(input("\n{}.Digite un numero: ".format(i+1)))

	numeros[i] = numero

	if numero < menor:

		menor = numero
		pos = i

del numeros[pos]

print("\n Los numeros regitrados son: ")

for i in numeros:

	print(i)

print("\n El numero eliminado fue:",menor,"\n")

