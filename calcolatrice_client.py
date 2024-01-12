import socket
import json

SERVER_IP="127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024
NUM_MESSAGES = 5

#Creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    primoNumero=float(input("Inserisci il primo numero: "))
    operazione=input("Inserisci l'operazione (+,-,*,/,%)")
    secondoNumero=float(input("Inserisci il secondo numero: "))
    messaggio={"primoNumero":primoNumero,
               "operazione":operazione,
               "secondoNumero":secondoNumero}
    messaggio=json.dumps(messaggio) #trasformiamo l'oggetto in una stringa
    sock.sendto(messaggio.encode("UTF-8"), (SERVER_IP, SERVER_PORT))
    data=sock.recv(BUFFER_SIZE)
    print("Risultato: ",data.decode())

    risposta=(input("--- inserisci la tua risposta s-si n-no --- "))
    if(risposta=='n'):
        break

#Chiusura del socket
sock.close()
