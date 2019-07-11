while True:

	try:

		longitud = int(input("\nDigite la cantidad de numeros que desea ingresar: "))

		if longitud > 0:
			break

		else:

			print("\nDATO INVALIDO")

	except ValueError:

		print("\nDATO INVALIDO")
		continue

numeros = [0 for i in range(0,longitud)]

numero = 0
menor = 50
pos = 0

for i in range(0,longitud):

	while True:

		try:
			numero = float(input("\n{}.Digite un numero: ".format(i+1)))

			if numero > 0:
				break

			else:
				print("\nDATO INVALIDO")

		except ValueError:

				print("\nDATO INVALIDO")
				continue

	numeros[i] = numero

	if numero < menor:

		menor = numero
		pos = i

del numeros[pos]

print("\nLos numeros regitrados son: ")

for i in numeros:

	print(i)

print("\n El numero eliminado fue:",menor,"\n")

