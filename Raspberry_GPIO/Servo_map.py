from escalar import map

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)

pwm = GPIO.PWM(37,50)
pwm.start(0)

try:
	while True:

		opcion = float(input("Digite la posicion de servo 0%~100%: "))

		tiempo  = map(opcion,0,100,0.1e-3,3e-3)

		ciclo = tiempo*100/20e-3

		print("Ciclo: ",ciclo)

		pwm.ChangeDutyCycle( ciclo )
		sleep(0.01)

except KeyboardInterrupt:
	pass

pwm.stop()
GPIO.cleanup()
print("\n")




