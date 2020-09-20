# Librería que nos permite trabajar con la red
import socket

# Definimos host y puerto
HOST = "127.0.0.1"
PUERTO = 8080

# Colores (ANSI)
blue = "\u001b[34m"
white = "\u001b[37m"
red = "\u001b[31m"

# Creamos un cable con el que nos vamos a conectar a alguien
cable = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Le decimos al cable con quién (127.0.0.1) y por dónde (8000) se va a conectar
cable.connect((HOST, PUERTO))

mensaje = ""

while mensaje != "/exit":
    # Obtenemos y guardamos el mensaje a enviar
    mensaje = input(blue+"Escribe tu mensaje: "+white)

    # Enviamos un mensaje
    cable.send(mensaje.encode())

# Cerramos el cable
cable.close()