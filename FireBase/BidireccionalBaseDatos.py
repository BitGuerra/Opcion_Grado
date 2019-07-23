#El siguente algoritmo responde a la siguiente estructura en la base de datos

#	+OpcionG
#	    +-dato:1
#	    +-dato1:1
#	    +-dato2:1
#	    +-dato3:1

#dato2 guardara informacion acerca del estado el pulsador1
#dato3 guardara informacion acerca del estado el pulsador2

import RPi.GPIO as GPIO
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(37,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

cred = credentials.Certificate('credenciales.json')
firebase_admin.initialize_app(cred,
{ 'databaseURL':'LINK AQUI' })

nodo = db.reference('OpcionG')

while True:

	#Lectura de los pulsadores
	pulsador1 = GPIO.input(7)
	pulsador2 = GPIO.input(37)

	#Diccionario para actualizar la base de datos
	diccionarioDB = {'dato2':pulsador1,'dato3':pulsador2}
	#Actualiza la base de datos
	nodo.update(diccionarioDB)

	#Optiene todos los valores de los nodos de la base de datos
	Estructura = nodo.get()

	#Toma solamente los valores que representan los estados de los diodos led
	led1 =Estructura['dato']
	led2 =Estructura['dato1']

	if led1 == 1:

		GPIO.output(11,True)

	elif led1 == 0:

		GPIO.output(11,False)

	if led2 == 1:

		GPIO.output(13,True)

	elif led2 == 0:

		GPIO.output(13,False)
