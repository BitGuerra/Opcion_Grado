piezas = float(input("Dgite la cantidad de piezas a comprar: "))
precio = float(input("Digite el precio de las piezas: "))

pago = piezas*precio

Banco, credito, empresa = 0, 0, 0

if pago > 500000:

	empresa = pago*55/100
	Banco = pago*30/100
	credito = pago*(100-30-55)/100
else:

	empresa = pago*70/100
	Banco = pago*30/100

print("El total es: ",pago)
print("El monto a pagar por la empresa es: ",empresa)
print("El el valor de prestamo del banco es: ",Banco)
print("El valor del credo del fabricante es: ",credito)

