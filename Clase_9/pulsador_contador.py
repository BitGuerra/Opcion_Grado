import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
#Modo PULL DOWN (Con resistencia y conexion a 3.3V)
GPIO.setup(7,GPIO.IN)

C = 0

while True:

	estado = GPIO.input(7)

	if  estado==True:

		while estado ==True:

			estado = GPIO.input(7)

		C += 1
		print(C)
