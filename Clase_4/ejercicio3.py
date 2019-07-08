print("\n")

#-----------------------------------------------------------------------
#VALIDA LA ENTRADA DE LA BASE

while True:
	try:
		base = float(input("Digite el la medida de la base: "))
		break

	except ValueError:

		print("Dato invalido ! ! !")
		continue

#-----------------------------------------------------------------------
#VALIDA LA ENTRADA DE LA ALTURA

while True:
	try:
		altura = float(input("Digite el la medida de la altura: "))
		break

	except ValueError:

		print("Dato invalido ! ! !")
		continue

#-----------------------------------------------------------------------
#CALCULA E IMPRIME EL AREA
area = base*altura/2
print("El area del triangulo es:",area,"\n")
