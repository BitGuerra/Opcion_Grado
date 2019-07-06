
respuesta = ""


while respuesta != 's' and respuesta != 'S':

	numero = float(input("Digite un numero: "))

	if numero >= 0:

		print("El numero {} es positivo".format(numero))

	else:

		print("El numero {} es negativo".format(numero))

	respuesta = input("Desa salir S/N ?")
