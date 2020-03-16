from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import time
import pickle

HOST = '10.0.0.174'
PORT = 6667
connections = {}
serverTime = "%H:%M:%S %p"
chatTime = "%H:%M %p"

def accept_incoming_connections():
    while True:
        connection, addr = server.accept()
        Thread(target=handle_client, args=(connection,)).start()

def handle_client(connection):
        name = connection.recv(1024)
        print(time.strftime(serverTime) + " Log: " + name.decode() + " connected")
        for c in connections:
            c.send(pickle.dumps([True, [name]]))
        namesList = []
        namesList.append(name.decode())
        for c in connections.keys():
            #c.send(bytes(time.strftime(chatTime) + " Server: Welcome, " + name.decode()+"!","utf8"))
            namesList.append(connections[c].decode())
        print(namesList)
        for thing in namesList:
            data = pickle.dumps([True,[thing]])
            connection.send(data)
        connections.update({connection : name})
        while True: #while connection exists and data is coming
            try:
                data = bytes(time.strftime(chatTime) + " " + name.decode()+": "+connection.recv(1024).decode(),"utf8") #buffer size
            except:
                connection.close()
                del connections[connection]
                print(time.strftime(serverTime) + " Log: " + name.decode()+" left")
                #nameList.remove(name.decode())
                for c in connections.keys():
                    c.send(bytes(time.strftime(chatTime) + " Server: " + name.decode()+" left","utf8"))
                    c.send(pickle.dumps([False, [name.decode()]]))
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
