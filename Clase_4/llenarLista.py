
#Crear una lista vacia
lista = []
elemento = 0
#llenar la lista

for i in range(0,5):

	elemento = input("{}. Digite algo \n".format(i))

	lista.append( elemento )

#Imprimir lista

print("los elementos de la lista son:")
print(lista)
