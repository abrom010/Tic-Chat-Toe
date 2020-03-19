from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import time
import pickle
<<<<<<< HEAD

with open("config.txt","r") as file:
	HOST = file.read().splitlines()[0]
=======
import os
import sys
>>>>>>> 11e4632341a823b9bf936ede3b1d655de86d0680

PORT = 6667
connections = {}
serverTime = "%H:%M:%S %p"
chatTime = "%H:%M %p"
serverNameList = []

for filename in os.listdir():
    if "log.txt" in filename:
        os.remove(filename)

with open("config.txt","r") as file:
	HOST = file.read().splitlines()[0]

filename = time.strftime(serverTime).replace(":", "_") + "log.txt"

with open(filename, "a+"):
    pass
#sessionHistory = open(filename, "a+")

def accept_incoming_connections():
    while True:
        connection, addr = server.accept()
        Thread(target=handle_client, args=(connection,)).start()

def handle_client(connection):
        name = connection.recv(1024).decode()
        print(time.strftime(serverTime) + " Log: " + name + " connected")

        with open(filename, "a") as file:
            file.write(time.strftime(serverTime) + " Log: " + name + " connected\n")
        '''with open(filename, "r") as file:
            #connection.send(bytes(file.read(), "utf8"))
            #connection.send(bytes(file.read(), "utf8"))
            if file.read() == "":
                print("OK")
            else:
                connection.send(bytes(file.read(), "utf8"))
                print(file.read())'''
        connection.send(bytes(time.strftime(chatTime) + " Server: Welcome, " + name, "utf8"))

        for c in connections.keys():
            c.send(bytes(time.strftime(chatTime) + " Server: " + name + " has joined the chat!", "utf8"))

        serverNameList.append(name)
        connections.update({connection : name})

        for c in connections.keys():
            c.send(pickle.dumps(serverNameList))

        while True: #while connection exists and data is coming
            try:
                message = connection.recv(1024).decode()
                with open(filename, "a") as file:
                    file.write(time.strftime(serverTime) + " " + name + ": " + message + "\n")
                message = time.strftime(chatTime) + " " + name+": " + message

                for c in connections.keys():
                    c.send(bytes(message, "utf8"))
                #data = bytes(time.strftime(chatTime) + " " + name+": "+connection.recv(1024).decode(),"utf8") #buffer size
            except:
                connection.close()
                del connections[connection]
                serverNameList.remove(name)

                with open(filename, "a") as file:
                    file.write(time.strftime(serverTime) + " Log: " + name + " left" + "\n")
                print(time.strftime(serverTime) + " Log: " + name + " left")

                for c in connections.keys():
                    c.send(bytes(time.strftime(chatTime) + " Server: " + name + " has left","utf8"))
                    c.send(pickle.dumps(serverNameList))
                break

if __name__ == "__main__":
    with socket(AF_INET, SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        ACCEPT_THREAD = Thread(target=accept_incoming_connections)
        ACCEPT_THREAD.start()
        ACCEPT_THREAD.join()
        server.close()
        os.remove(filename)
