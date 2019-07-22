#Importar librerias
import RPi.GPIO as GPIO
from time import sleep
from escalar import angle2cycle

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

		angulo = float(input("Digite la posicion de servo 0°~180°: "))

		#Convierte el angulo a ciclo de PWM
		ciclo  = angle2cycle(angulo)

		print("Ciclo: ",ciclo)

		pwm.ChangeDutyCycle( ciclo )
		sleep(0.01)

except KeyboardInterrupt:

	pwm.stop()
	GPIO.cleanup()
	print("\n")


