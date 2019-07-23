#El siguente algoritmo responde a la siguiente estructura en la base de datos

#	+OpcionG
#	    +-dato:100
#	    +-dato1:200
#	    +-dato2:300
#	    +-dato3:400

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('credenciales.json')
firebase_admin.initialize_app(cred,
{ 'databaseURL':'LINK AQUI' })
nodo = db.reference('OpcionG')

#Para ver todos los datos de la base de datos
#El metodo .get() retorna un diccionario de la estructura de la base de datos
Estructura = nodo.get()

#Imprime el diccionario
print('\n',Estructura)

#Imprime el contenido del diccionario
for i in Estructura:
	print('El nodo {} tiene el valor {}'.format(i,Estructura[i]))






