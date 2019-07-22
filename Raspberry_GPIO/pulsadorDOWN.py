#importar librerias.
import RPi.GPIO as GPIO
from time import sleep

#Configuracion modo BOARD.
GPIO.setmode(GPIO.BOARD)
#Pin 37 como entrada en configuracion PULL DOWN
GPIO.setup(7,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:

	estado = GPIO.input(7)

	if  estado==True:

		print("Precinado")

	else:

		print("No Precionado")



