# Librería que nos permite trabajar con la red
import socket

# Definimos host y puerto
HOST = "127.0.0.1"
PUERTO = 8080

# Creamos un cable con el que nos vamos a conectar a alguien
cable = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Le decimos al cable con quién (127.0.0.1) y por dónde (8000) se va a conectar
cable.connect((HOST, PUERTO))

# Enviamos un mensaje
cable.send("Ey, que pasa".encode())

# Cerramos el cable
cable.close()