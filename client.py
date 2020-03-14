# from tkinter import *
import socket
import tkinter
import tkinter.font as font
from threading import Thread

HOST = '71.196.93.132'
PORT = 6667

main_window = tkinter.Tk()
main_window.title("Chat Lobby")

name_window = tkinter.Tk()

message = tkinter.StringVar()
name = tkinter.StringVar()

fontTemplate = font.Font(size=11)

def set_name():
    name_window.attributes('-topmost', True)
    name_window.title("Name")
    name_window.lift()

    prompt = tkinter.Label(name_window, text="Enter your name: ")
    prompt.pack(side=tkinter.LEFT)

    name_entry = tkinter.Entry(name_window, width=40)
    name_entry.pack(side=tkinter.LEFT)
    name_entry.bind("<Return>", lambda s: send_name(name_entry.get()))

def send_name(name,event=None):
    if name == "": name = "guest"
    socket.send(bytes(name, "utf8"))
    name_window.destroy()
    #main_window.attributes('-topmost', True)
    main_window.focus_force()
    entry = tkinter.Entry(main_window, textvariable=message, width=80, relief=tkinter.FLAT)
    entry.grid(sticky="W", row=1)
    users_box = tkinter.Listbox(main_window, width=20, height=22, relief=tkinter.FLAT)
    users_box.grid(sticky="N", row=0&1, column=1)
    #entry.pack(side=tkinter.LEFT)
    entry.bind("<Return>", send)
    buton = tkinter.Button(main_window, text="Send", command=send, width=20, relief=tkinter.FLAT)
    buton['font'] = font.Font(family='Helvetica', size=12)
    buton.grid(sticky="E", row=1)
    #buton.pack()

def receive():
    while True:
        response = socket.recv(1024)
        text_box.insert(tkinter.END, response.decode())

def send(event=None):
        socket.send(bytes(message.get(), "utf8"))
        message.set("")

if __name__ == "__main__":
    text_box = tkinter.Listbox(main_window, height=20, width=70, relief=tkinter.FLAT, font=fontTemplate)
    text_box.grid(sticky="W", row=0)
    #text_box.pack()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
        socket.connect((HOST, PORT))
        Thread(target=receive).start()
        set_name()
        main_window.mainloop()
