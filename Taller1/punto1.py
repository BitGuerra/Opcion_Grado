precio = float( input("Digite el valor bruto del producto: ") )

IVA = 19

PrecioIVA = precio* IVA/100

total = PrecioIVA + precio

print("El precio neto del producto es: ",total)
