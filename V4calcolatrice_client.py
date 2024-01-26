import socket, json, sys, random, os, time, threading, multiprocessing
from random import *
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
NUM_WORKERS = 15
BUFFER_SIZE= 1024

def genera_richieste(SERVER_ADDRESS, SERVER_PORT):
    start_time_thread=time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
        sock_service.connect((SERVER_ADDRESS,SERVER_PORT))
        
        primoNumero=randint(1,10)
        indice=randint(0,4)
        secondoNumero=randint(1,10)
        vettore=['+','-','*','/','%']
        operazione=vettore[indice]
        print(primoNumero)
        print(operazione)
        messaggio={"primoNumero":primoNumero,
                    "operazione":operazione,
                    "secondoNumero":secondoNumero
                   }
        
        print(messaggio)
        messaggio=json.dumps(messaggio) #trasformiamo l'oggetto in una stringa
        sock_service.sendall(messaggio.encode("UTF-8"))
        data=sock_service.recv(BUFFER_SIZE)
        print("Risultato: ",data.decode())

        end_time_thread=time.time()
        print(f"{threading.current_thread().name} execution time =", end_time_thread - start_time_thread)


if __name__ == '__main__':
    start_time = time.time()
    threads = [threading.Thread(target=genera_richieste,args=(SERVER_ADDRESS,SERVER_PORT,))for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time = time.time()

    print("Total threads time=", end_time - start_time)