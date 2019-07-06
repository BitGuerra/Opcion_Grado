print("Bienvenido al Gym !!!")

edad = int(input("Cual es la edad del cliente? "))

pago = 120000
total = 0
decuento = 0

if edad >= 0 and edad < 20:

	descuento = pago*30/100
	total = pago - descuento

elif edad >= 20 and edad <30:

	descuento = pago*25/100
	total = pago - descuento

elif edad >= 30 and edad <40:

	descuento = pago*15/100
	total = pago - descuento

elif edad >= 40:

	descuento = pago*50/100
	total = pago - descuento

print("El total a pagar es:",total)
print("con un descuento de:",descuento)
