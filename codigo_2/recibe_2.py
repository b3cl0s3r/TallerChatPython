# Librería que nos permite trabajar con la red
import socket

# Definimos HOST y PUERTO
HOST = "127.0.0.1"
PUERTO = 8080

# Colores (ANSI)
white = "\u001b[37m"
red = "\u001b[31m"

# Creamos el cable
cable = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Enchufamos el cable a nosotros
cable.bind((HOST, PUERTO))

# Nos ponemos a escuchar
cable.listen()
print("Esperando mensajes...")

# Aceptamos la conexión que nos llegue.
#
# conn es el otro extremo del cable
# addr es información sobre su dirección (address)
conn, addr = cable.accept()

# while True es un bucle infinito.
while True: 
    # Esperamos a recibir un mensaje 
    data = conn.recv(1024)

    # Si no llegan datos, cerramos el bucle
    if not data: 
        break

    # Mostramos el mensaje por terminal
    print(red + "Mensaje recibido: " + white + data.decode())

# Cerramos el cable
cable.close()