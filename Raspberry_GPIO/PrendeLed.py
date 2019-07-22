#Importar las librerias
import RPi.GPIO as GPIO
from time import sleep

#Cofiguracion de los pines como BOARD
GPIO.setmode(GPIO.BOARD)
#Pin 37 como salida
GPIO.setup(37, GPIO.OUT)

try:
	while True:

		GPIO.output(37,True)
		sleep(1)
		GPIO.output(37,False)
		sleep(1)

except KeyboardInterrupt:

	print("\n")
	GPIO.cleanup()



