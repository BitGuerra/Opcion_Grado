c = 0
numero = 0
for i in range(1,7):

	numero = int(input("Digite ({}): ".format(i)))

	if numero%2 == 0:

		c += 1

print("La cantidad de numeros pares es: ",c)
