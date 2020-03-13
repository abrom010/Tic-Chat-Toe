import socket
import tkinter
from threading import Thread

HOST = '71.196.93.132'
PORT = 6667

mainWind = tkinter.Tk()     #create tkinter obj/window
nameWin = tkinter.Tk()
mainWind.title("Chat Lobby")
msg = tkinter.StringVar()   #create textbox at bottom of tkinter
nameInput = tkinter.StringVar()
nameInput.set("")

def init():
    #mainWind.wait_window()
    nameWin.title("")
    nameWin.lift()
    nameWin.attributes('-topmost', True)
    mainWind.attributes('-topmost', False)
    userName = tkinter.Entry(nameWin, textvariable=nameInput, width=40)
    userName.pack(side=tkinter.LEFT)
    userNamePrompt = tkinter.Label(nameWin, text="Enter your name.")
    userNamePrompt.pack()
    userName.bind("<Return>", nameSend)  #make own destroy function
    #nameWin.mainloop()

    #userName.bind("<Return>", nameWin.destroy)
    #nameWin.destroy()

def init2ElectricBoogaloo():
    init()


def recvServ():
    while True:
        response = socket.recv(1024)
        textBox.insert(tkinter.END, "Server: " + response.decode())
        #print("Server: " + response.decode())

def send(event=None):
        socket.send(bytes(msg.get(), "utf8"))
        textBox.insert(tkinter.END, "Me: " + msg.get())
        msg.set("")
        #textBox.pack()

def nameSend(event=None):
    socket.send(bytes(nameInput.get(), "utf8"))
    nameWin.destroy()

recvThread = Thread(target=recvServ)
sendThread = Thread(target=send)
initThread = Thread(target=init)

textBox = tkinter.Listbox(mainWind, height=20, width=100)
textBox.pack()

text = tkinter.Text(mainWind)


       #makes the window accept text?
print("Step 2")
#text.pack()
usrInput = tkinter.Entry(mainWind, textvariable=msg, width=80)
usrInput.pack(side=tkinter.LEFT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT))        #IP & port number
    #print(nameInput.get())
    recvThread.start()
    initThread.start()
    usrInput.bind("<Return>", send)
    print("Step 6")
    mainWind.mainloop()     #prevents infinite loop possibly
        # print(data.decode())
        #print('Received: ', repr(data.decode())) Echos back what server received
