from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import time
import pickle
import os
import sys

PORT = 6667
connections = {}
serverTime = "%H:%M:%S %p"
chatTime = "%H:%M %p"
serverNameList = []

for filename in os.listdir():
    if ("log.txt" in filename) or ("users.txt" in filename):
        os.remove(filename)

with open("config.txt","r") as file:
	HOST = file.read().splitlines()[0]

logfile = time.strftime("%H:%M:%S").replace(":", "_") + "log.txt"
usersfile = time.strftime("%H:%M").replace(":","_") + "users.txt"
userSession = {}

#sessionHistory = open(logfile, "a+")

def accept_incoming_connections():
    while True:
        connection, addr = server.accept()
        #print(addr)
        Thread(target=handle_client, args=(connection, addr)).start()

def handle_client(connection, addr):
        name = connection.recv(1024).decode()
        print(time.strftime(serverTime) + " Log: " + name + " connected")
        userSession = {"Time":time.strftime("%H:%M:%S"), "IP":addr[0], "username":name}
        #print(connection)

        with open(usersfile, "a") as file:
            tempString = ""
            for i in userSession:
                tempString += i + ": " + userSession[i] + ", "
            file.write(tempString[:len(tempString)-2] + "\n")
            file.close()

        with open(logfile, "a") as file:
            file.write(time.strftime(serverTime) + " Log: " + name + " connected\n")
        '''with open(logfile, "r") as file:
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
                with open(logfile, "a") as file:
                    file.write(time.strftime(serverTime) + " " + name + ": " + message + "\n")
                message = time.strftime(chatTime) + " " + name+": " + message

                for c in connections.keys():
                    c.send(bytes(message, "utf8"))
                #data = bytes(time.strftime(chatTime) + " " + name+": "+connection.recv(1024).decode(),"utf8") #buffer size
            except:
                connection.close()
                del connections[connection]
                serverNameList.remove(name)

                with open(logfile, "a") as file:
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
        os.remove(logfile)
        os.remove(usersfile)
