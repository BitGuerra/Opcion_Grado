codigos = []
nombres = []

cod = 0
nom = ""

for i in range(0,3):

	nom = input("\nDigite el nombre del estudiante a ingresar: ")
	nombres.append(nom)

	cod = input("Digite el codigo de {}:".format(nom))
	codigos.append(cod)

print("\nLos nombre y codigos registrados son:")

for i in range(0,3):

	print("{} - codigo: {}".format(nombres[i],codigos[i]))
