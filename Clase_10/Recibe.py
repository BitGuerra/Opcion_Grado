import serial
from time import sleep

#Direccion "/dev/ttyACM0" donde se encuentra  conectado Arduino
#Velocidad de transmision y recepcion 115200 baudios

Ndatos = int(input("Digite la cantidad de datos a recibir: "));

arduino = serial.Serial("/dev/ttyACM0",115200)
Pulsador = 0
Potencimetro = 0

while True:

	#Verica si hay algun dato en el buffer
	if arduino.inWaiting() > 0:

		#Lectura del buffer
		mensaje = str(arduino.readline(), 'utf-8')

		#Quita caracteres inecesarios del mensaje recibido
		#mensaje = mensaje.replace("\n","")

		#Divide los datos en una lista
		#codigo = mensaje.split()

		#verifica si la lista tiene mas de un dato
		#if len(codigo) == Ndatos:

			#Toma los datos del la lista
			#Potenciometro = codigo[0]
			#Pulsador  = codigo[1]
			#print("Potenciometro:",Potenciometro,"  Pulsador:",Pulsador)

		sleep(0.1)
