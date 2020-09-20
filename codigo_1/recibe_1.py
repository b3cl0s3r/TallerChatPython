# Librería que nos permite trabajar con la red
import socket

# Definimos HOST y PUERTO
HOST = "127.0.0.1"
PUERTO = 8080

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

# Esperamos a recibir un mensaje 
data = conn.recv(1024)

# Mostramos el mensaje por terminal
print(data.decode())

# Cerramos el cable
cable.close()



