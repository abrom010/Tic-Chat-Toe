import socket

HOST = '127.0.0.1'
PORT = 6667

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT))
    msg = input("Type here: ").encode()
    socket.sendall(msg) #bytes object type
    data = socket.recv(1024)

print('Received: ', repr(data.decode()))
