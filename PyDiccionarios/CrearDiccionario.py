#declara un diccionario vacio

Diccionario = {}

#LLena el diccionario
print('\n')

nombre = input('Digite su nombre: ')
Diccionario['nombre'] = nombre

Edad = int(input('Digite su edad: '))
Diccionario['Edad'] = Edad

Codigo = int(input('Digite su Codigo: '))
Diccionario['Codigo'] = Codigo

Cargo = input('Digite su cargo: ')
Diccionario['Cargo'] = Cargo

#Imprime el contenido del diccionario
print('\n')

for i in Diccionario:

	print(i,':',Diccionario[i])

print('\n')
