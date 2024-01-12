import socket
import json

SERVER_IP= "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

# Creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

while True:
    data,addr=sock.recvfrom(1024)
    if not data:
        break
    data=data.decode()
    data=json.loads(data)
    primoNumero=data["primoNumero"]
    operazione=data["operazione"]
    secondoNumero=data["secondoNumero"]

    ris=0
    if(operazione=="+"):
        ris=primoNumero+secondoNumero
    elif(operazione=="-"):
        ris=primoNumero-secondoNumero
    elif(operazione=="*"):
        ris=primoNumero*secondoNumero
    elif(operazione=="/"):
        ris=primoNumero/secondoNumero
    elif(operazione=="%"):
        ris=primoNumero%secondoNumero

    sock.sendto((str(ris)).encode(),addr)


