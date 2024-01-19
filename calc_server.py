import socket
import json

SERVER_IP= "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((SERVER_IP, SERVER_PORT))
    sock_server.listen()
    print(f"Server in ascolto su {SERVER_IP}:{SERVER_PORT}...")
    while True:
        sock_service, address_client= sock_server.accept()

        with sock_service as sock_client:
            while True:
                data,addr=sock_client.recvfrom(1024)
                if not data:
                    break
                data = data.decode()
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

                sock_client.sendall(str(ris).encode())


