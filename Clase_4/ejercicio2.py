nombres = []

name = ""
opcion = "S"

while opcion=="S" or opcion=="s":

	name = input("\nDigite el nombre a ingresar: ")
	nombres.append(name)

	opcion = input("\nDesea ingrasar otro nombre S/N: ")

cantidad = len(nombres)+1
print("\nla cantidad de nombres registrados es:",cantidad)

print("los nombres registrados son: ")

for i in nombres:

	print( i )
