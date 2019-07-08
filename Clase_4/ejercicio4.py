codigos = []

for i in range(0,6):

	while True:
		try:

			code = float(input("{}. digite su codigo: ".format(i)))
			break

		except ValueError:

			print("DATO INVALIDO, INSETE DE NUEVO ! ! !")
			continue

	codigos.append(code)


print("Los codigos registrados son: ")
print(codigos)

