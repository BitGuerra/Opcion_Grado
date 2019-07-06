personas = float(input("Digite la cantidad de pesonas a ingresar: "))
socio = input("Hay un socio en el grupo S/N ? ")

pago = 7000*personas

total = 0

if socio == "S" or socio == "s":

	descuento = pago*20/100
	total = pago - descuento
	print("El total a pagar es: ",total)
	print("Con un descuento de:",descuento)
else:

	total = pago
	print("el total a pagar es:",total)
	print("No hay descuento !")
