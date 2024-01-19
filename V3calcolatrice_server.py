import socket, json
from threading import Thread

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT=  22224
BUFFER_SIZE=1024

def ricevi_connessioni(sock_listen):
    while True:
        sock_service, addr_client= sock_listen.accept()
        print("\nConnessione ricevuta da %s" %str(addr_client))
        print("creo un thread per servire le richieste")
        try:
            Thread(target=ricevi_comandi, args=(sock_service, addr_client)).start()
        except:
            print("Il thread non si avvia")
            sock_listen.close()

def avvia_server(indirizzo,porta):
    try:
        print("avvio in corso...")
        sock_listen=socket.socket()
        sock_listen.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        sock_listen.bind((indirizzo,porta))
        sock_listen.listen(5)
        ricevi_connessioni(sock_listen)
        print("server in ascolto su %s. Termina con ko"% str((indirizzo,porta)))
    except socket.error as errore:
        print(f"Qualcosa è andato storto...\n{errore}")
    
def ricevi_comandi(sock, addr_client):
    print("In attesa di comandi da", addr_client)
    with sock as sock_client:
        while True:
            dati=sock_client.recv(BUFFER_SIZE).decode()
            if not dati:
                break
            dati=json.loads(dati)
            primoNumero=dati["primoNumero"]
            operazione=dati["operazione"]
            secondoNumero=dati["secondoNumero"]

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

            ris=str(ris)
            print(ris,type(ris))
            sock_client.sendall(str(ris).encode())

        sock.close()

if __name__ == '__main__': 
    avvia_server(SERVER_ADDRESS,SERVER_PORT)
print("Termina")

