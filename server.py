from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import time

HOST = '10.0.0.174'
PORT = 6667
connections = {}
serverTime = "%H:%M:%S"
chatTime = "%H:%M"

def accept_incoming_connections():
    while True:
        connection, addr = server.accept()
        # connection.send(bytes("You have connected, please type in your name.","utf8"))    //Not needed, get name already from client side
        Thread(target=handle_client, args=(connection,)).start()

def handle_client(connection):
    with connection:
        name = connection.recv(1024)
        print(time.strftime(serverTime) + " Log: " + name.decode()+" connected")
        connections.update({connection : name})
        for c in connections.keys():
        	c.send(bytes(time.strftime(chatTime) + " Server: Welcome, "+name.decode()+"!","utf8"))
        while True: #while connection exists and data is coming
            try:
                data = bytes(time.strftime(chatTime) + " " + name.decode()+": "+connection.recv(1024).decode(),"utf8") #buffer size
            except:
                connection.close()
                del connections[connection]
                print(time.strftime(serverTime) + " Log: " + name.decode()+" left")
                for c in connections.keys():
                    c.send(bytes(time.strftime(chatTime) + " Server: " + name.decode()+" left","utf8"))
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
