#Importar librerias
import RPi.GPIO as GPIO
from time import sleep

#Cofiguracion modo BOARD
GPIO.setmode(GPIO.BOARD)

#Pin 7 como entrada  en configuracion PULL UP
GPIO.setup(7,GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:

	estado = GPIO.input(7)

	if estado == False:

		print("Precionado")

	else:

		print("No Precionado")
