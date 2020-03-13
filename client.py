import socket
import tkinter
from threading import Thread

HOST = '71.196.93.132'
PORT = 6667

main_window = tkinter.Tk()
main_window.title("Chat Lobby")

name_window = tkinter.Tk()

def set_name():
    #main_window.attributes('-topmost', False)

    name_window.attributes('-topmost', True)
    name_window.title("Name")
    name_window.lift()

    prompt = tkinter.Label(name_window, text="Enter your name: ")
    prompt.pack(side=tkinter.LEFT)
    name = tkinter.StringVar()
    name_entry = tkinter.Entry(name_window, textvariable=name, width=40)
    name_entry.pack(side=tkinter.LEFT)
    name_entry.bind("<Return>", lambda s: send_name(name))

def send_name(name,event=None):
    socket.send(bytes(name.get(), "utf8"))
    name_window.destroy()
    main_window.attributes('-topmost', True)
    main_window.focus_force()

def receive():
    while True:
        response = socket.recv(1024)
        text_box.insert(tkinter.END, "Server: " + response.decode())

def send(event=None):
        socket.send(bytes(message.get(), "utf8"))
        #text_box.insert(tkinter.END, "Me: " + message.get())
        message.set("")

if __name__ == "__main__":
    text_box = tkinter.Listbox(main_window, height=20, width=100)
    text_box.pack()

    message = tkinter.StringVar()

    entry = tkinter.Entry(main_window, textvariable=message, width=80)
    entry.pack(side=tkinter.LEFT)
    entry.bind("<Return>", send)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
        socket.connect((HOST, PORT))
        Thread(target=receive).start()
        set_name()
        main_window.mainloop()
