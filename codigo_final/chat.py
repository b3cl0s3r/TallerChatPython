import socket
import threading 
import argparse
import os

# Cómo ejecutar:
# 1) python chat.py -P 8080 -t 4040 -u pepe
# 2) python chat.py -P 4040 -t 8080 -u juan

# Definimos host y puerto
HOST = "127.0.0.1"
PUERTO = 8080

# Colores (ANSI)
blue = "\u001b[34m"
white = "\u001b[37m"
red = "\u001b[31m"
clear = "\u001b[2K"
toLeft = "\u001b[10D"

# FUNCION QUE RECIBE MENSAJES
def recibir(cable, name):
  print("Esperando mensajes...")
  conn, addr = cable.accept()
  data = ""

  while data != "/exit": 
    data = conn.recv(1024).decode()
    print(toLeft + clear + data)

# FUNCION QUE ENVIA MENSAJES
def enviar(PCremoto, name):
  mensaje = ""
  while mensaje != "/exit":
    # Obtenemos y guardamos el mensaje a enviar
    mensaje = input()
    
    if mensaje != "/exit":
      #Añadimos al mensaje el nombre
      mensaje = red+name+": "+white+mensaje
    try:
      # Enviamos un mensaje
      PCremoto.send(mensaje.encode())
    except:
      print("Desconexion")
      break

## DONDE EMPIEZA EL CODIGO A EJECUTARSE 
# Proporcionamos 'argumentos' 
parser = argparse.ArgumentParser(description='Chat TCP en Python')
parser.add_argument('--port', '-P', type=int, required=True,
                    help='an integer for the accumulator')
parser.add_argument('--to', '-t', type=int, required=True,
                    help='an integer for the accumulator')
parser.add_argument('--name', '-u', type=str, required=True,
                    help='an integer for the accumulator')
args = parser.parse_args()

# Definimos nombre de usuario
USERNAME = args.name

# Definimos host y puerto
HOST = "127.0.0.1"
PUERTO = args.port

# Definimos host REMOTO y puerto
HOST_REMOTO = "127.0.0.1"
PUERTO_REMOTO = args.to

# Creamos el cable, nos ponemos a escuchar y nos conectamos al otro lado
cable = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
cable.bind((HOST, PUERTO))
cable.listen(1)

# Creamos un hilo que se ejecutara por su cuenta y esperara a recibir los mensajes
recibirMensajes = threading.Thread(target=recibir, args=(cable, USERNAME))
recibirMensajes.start()

# Creamos otro cable que se va a conectar con el ordenador remoto
PCremoto = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Intentamos conectarnos todo el rato
while True:
  try:
      PCremoto.connect((HOST_REMOTO, PUERTO_REMOTO))
      break
  except ConnectionRefusedError:
      print(red+"[!] Error. No se pudo establecer la conexión"+white)

# Borramos el mensaje de error de la pantalla e imprimos que se inició la conexión
os.system('cls' if os.name == 'nt' else 'clear')

# Llamamos a la función que se dedica a enviar mensajes
enviar(PCremoto, args.name)

# Manera sucia de cerrar el bloqueo de recv. Debe haber alguna manera mejor de frenar el bloqueo del hilo
cable.close()
PCremoto.close()
