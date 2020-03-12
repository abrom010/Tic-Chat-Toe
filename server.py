from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

HOST = '10.0.0.174'
PORT = 6667
                
def accept_incoming_connections():
    while True:
        connection, addr = server.accept()
        connection.send(bytes("You have connected, please type in your name: ","utf8"))
        Thread(target=handle_client, args=(connection,)).start()

def handle_client(connection):
    with connection:
        name = bytes("default","utf8")
        #name = connection.recv(1024)
        #print(name.decode()+" has connected")
        #connection.send(bytes("Welcome, "+name.decode(),"utf8"))
        while True: #while connection exists and data is coming
            data = connection.recv(1024) #buffer size
            print((name.decode()+": "+data.decode()))
            #connection.sendall(data) #Python specific function that sends entire

if __name__ == "__main__":           
    with socket(AF_INET, SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        ACCEPT_THREAD = Thread(target=accept_incoming_connections)
        ACCEPT_THREAD.start()
        ACCEPT_THREAD.join()
        server.close()
