#El siguente algoritmo responde a la siguiente estructura en la base de datos

#	+OpcionG
#	    +-dato:1
#	    +-dato1:0
#	    +-dato2:0
#	    +-dato3:0

# los nodos dato y dato1 controlan el encendodo de dos diodos led respectivamente
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('credenciales.json')
firebase_admin.initialize_app(cred,
{ 'databaseURL':'LINK AQUI' })
nodo = db.reference('OpcionG')


while True:
	#Para ver todos los datos de la base de datos -> .get()
	#El metodo .get() retorna un diccionario de la estructura de la base de datos
	Estructura = nodo.get()

	#Se toma solamente los valores de dato y dato1
	#Por que van a controlar los diodos led

	led1 = Estructura['dato']
	led2 = Estructura['dato1']

	if led1 == 1:

		print("Prende led 1")

	elif led1 == 0:

		print("Apaga led 1")

	if led2 == 1:

		print("Prende led 2")

	elif led2 == 0:

		print("Apaga led 2")




