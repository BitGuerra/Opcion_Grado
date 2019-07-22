#Importa las librerias para conectar con Firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Importar credenciales
cred = credentials.Certificate('credenciales.json')

#Indica el link de la base de datos
firebase_admin.initialize_app(cred, { 'databaseURL':'AQUI URL FIREBASE DATABASE' })

#Crea un referencia a un nodo especifico en la base de datos
nodo = db.reference('OpcionG/dato')

#Extrae la informacion del nodo dato en OpcionG
mensaje = nodo.get()

#para modifica la informacion del no use .set()

while True:

	print( mensaje )
