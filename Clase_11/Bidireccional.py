import serial
import time
from time import sleep

#Gestion de la conexion serial
arduino = serial.Serial("/dev/ttyACM0",115200,timeout = 20)
#Cantidad de datos a recibir
Ndata = int(input("digite la cantidad de datos que recibira de Arduino: "))

while True:
	#Pregunta al usuario la accion a realizar
	print("Digite la opcion:")
	print("1. Ver pulsadore 1 y 2")
	print("2. Ver apagar led 1")
	print("3. Ver prender led 1")
	opcion = input()

	if opcion == "1":

		#Espera hasta que llegue un dato al buffer
		while(arduino.inWaiting() ==  0 ):
			pass

		try:
			#Lectura del mensaje en el buffer
			mensaje = str(arduino.readline(),'utf-8')

		except UnicodeDecodeError:
			#En caso de error el mensaje se convierte en una cadena vacia
			mensaje = ""
			continue

		mensaje = mensaje.replace("\n","")
		codigo = mensaje.split()

		if len(codigo) == Ndata:

			#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
			PUL1 = codigo[0]
			PUL2 = codigo[1]
			print("Pulsador1:",PUL1,"  Pulsador2:",PUL2)
			#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	elif opcion == "2":
		# codigo 0L para apagar el diodo
		orden = "0L"
		# Escribe el codigo en el puerto serie
		arduino.write(orden.encode())
		sleep(0.01)
	elif opcion == "3":
		# Codigo para prender el diodo
		orden = "1L"
		# Escribe el codigo en el puerto serie
		arduino.write(orden.encode())
		sleep(0.01)
