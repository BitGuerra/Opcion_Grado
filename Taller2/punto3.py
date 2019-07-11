numero = 0
menor = 50
pos = 0
c = 0
prom = 0

while True:

	try:

		longitud = int(input("\nDigite la cantidad de notas que desea ingresar: "))

		if longitud > 0:
			break

		else:

			print("\nDATO INVALIDO")

	except ValueError:

		print("\nDATO INVALIDO")
		continue

numeros = [0 for i in range(0,longitud)]

for i in range(0,longitud):

	while True:

		try:
			numero = float(input("\nDigite un la nota{}: ".format(i+1)))

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

print("\nLas notas regitradas son: ")

for i in numeros:

	print(i)
	c += i

prom = c/(longitud-1)

print("\nLa nota eliminada fue:",menor,"\n")
print("El promedio es:",prom,"\n")

