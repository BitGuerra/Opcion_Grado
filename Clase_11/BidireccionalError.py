import serial
import time
from time import sleep

#Gestion de la conexion serial
arduino = serial.Serial("/dev/ttyACM0",115200,timeout = 20)

#Cantidad de datos a recibir
Ndata = int(input("digite la cantidad de datos que recibira de Arduino: "))
#Bandera para verificar errores
Error = True #Inicio en True para entrar al bucle en el que se consulta al buffer

while True:
	#Preguntal al usuario la accion a realizar
	print("Digite la opcion:")
	print("1. Ver pulsadore 1 y 2")
	print("2. Ver apagar led 1")
	print("3. Ver prender led 1")
	opcion = input()

	if opcion == "1":

		#Mientras el error UnicodeDecode sea True seguira consultando al buffer
		while Error:

			#Espera hasta que llegue un dato al buffer
			while(arduino.inWaiting() ==  0 ):
				pass

			try:
				#Lectura del mensaje del buffer
				mensaje = str(arduino.readline(),'utf-8')

			except UnicodeDecodeError:
				#Si el mensaje no puede codificarse, Error sera verdadero
				# entonces el agoritmo seguira consultando al buffer haciendo Error = True
				Error =True
				mensaje = ""
				continue

			mensaje = mensaje.replace("\n","")
			codigo = mensaje.split()

			if len(codigo) == Ndata:

				PUL1 = codigo[0]
				PUL2 = codigo[1]
				Error = False
				print("Pulsador1:",PUL1,"  Pulsador2:",PUL2)
		#Error se hace True para que en la proxina consulta el algoritmo entre al bucle
		Error = True

	elif opcion == "2":
		# codigo 0L para apagar el diodo
		orden = "0L"
		# Escribe el codigo 0L en el puerto serie
		arduino.write(orden.encode())
		sleep(0.01)
	elif opcion == "3":
		# Codigo para prender el diodo
		orden = "1L"
		# Escribe el codigo en el puerto serie
		arduino.write(orden.encode())
		sleep(0.01)
