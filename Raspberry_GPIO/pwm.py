#importar librerias
import RPi.GPIO as GPIO
from time import sleep

#cofiguracion de los pines
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)

#Configuracion del pin 37 como PWM a una frecuencia de 50Hz
pwm = GPIO.PWM(37,50)

#Inicio del PWM al 0% del ciclo
pwm.start(0)

try:
	while True:
			ciclo = int(input("Digite el ciclo del PWM 0~100: "))
			pwm.ChangeDutyCycle( ciclo )
			sleep(0.01)

except KeyboardInterrupt:
	pass

pwm.stop()
GPIO.cleanup()



