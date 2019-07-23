#El siguente algoritmo responde a la siguiente estructura en la base de datos

#	+OpcionG
#	    +-dato:100
#	    +-dato1:200
#	    +-dato2:300
#	    +-dato3:400

#dato2 guardara informacion acerca del estado el pulsador1
#dato3 guardara informacion acerca del estado el pulsador2

import RPi.GPIO as GPIO
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(37,GPIO.IN,pull_up_down = GPIO.PUD_UP)

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
