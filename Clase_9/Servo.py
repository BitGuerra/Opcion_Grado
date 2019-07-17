#Importar librerias
import RPi.GPIO as GPIO
from time import sleep

#Configuracion como BOARD
GPIO.setmode(GPIO.BOARD)
#Configuracion del pin 37 como salida
GPIO.setup(37,GPIO.OUT)

#Cofiguracion de la frecuencia del pwm en la variable PWM
pwm = GPIO.PWM(37,50)
#inicio del pwm
pwm.start(0)

try:
	while True:

		opcion = float(input("Digite la posicion de servo 0ms ~ 2ms: "))

		ciclo  = (opcion/1000)*100/20e-3

		print("Ciclo: ",ciclo)

		pwm.ChangeDutyCycle( ciclo )
		sleep(0.01)

except KeyboardInterrupt:
	pass

pwm.stop()
GPIO.cleanup()
print("\n")


