from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

HOST = '10.0.0.174'
PORT = 6667
connections = {}

def accept_incoming_connections():
    while True:
        connection, addr = server.accept()
        connection.send(bytes("You have connected, please type in your name.","utf8"))
        Thread(target=handle_client, args=(connection,)).start()

def handle_client(connection):
    with connection:
        name = connection.recv(1024)
        print(name.decode()+" connected")
        connections.update({connection : name})
        connection.send(bytes("Welcome, "+name.decode()+"!","utf8"))
        while True: #while connection exists and data is coming
            try:
                data = bytes(name.decode()+": "+connection.recv(1024).decode(),"utf8") #buffer size
            except:
                connection.close()
                del connections[connection]
                print(name.decode()+" left")
                for c in connections.keys():
                    c.send(bytes(name.decode()+" left","utf8"))
                break
            for c in connections.keys():
                    c.send(data) #Python specific function that sends entire

if __name__ == "__main__":           
    with socket(AF_INET, SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        ACCEPT_THREAD = Thread(target=accept_incoming_connections)
        ACCEPT_THREAD.start()
        ACCEPT_THREAD.join()
        server.close()
