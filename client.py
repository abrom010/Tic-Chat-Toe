import socket
import tkinter
from threading import Thread

HOST = '10.0.0.174'
PORT = 6667

main_window = tkinter.Tk()
main_window.title("Chat Lobby")

name_window = tkinter.Tk()

def set_name():
    main_window.attributes('-topmost', False)

    name_window.attributes('-topmost', True)
    name_window.title("")
    name_window.lift()

    name = tkinter.StringVar()
    name_entry = tkinter.Entry(name_window, textvariable=name, width=40)
    name_entry.pack(side=tkinter.LEFT)
    name_entry.bind("<Return>", lambda s: send_name(name))

    prompt = tkinter.Label(name_window, text="Enter your name.")
    prompt.pack()


def send_name(name,event=None):
    socket.send(bytes(name.get(), "utf8"))
    name_window.destroy()


def receive():
    while True:
        response = socket.recv(1024)
        text_box.insert(tkinter.END, "Server: " + response.decode())


def send(event=None):
        socket.send(bytes(msg.get(), "utf8"))
        text_box.insert(tkinter.END, "Me: " + msg.get())
        msg.set("")

if __name__ == "__main__":
    text_box = tkinter.Listbox(main_window, height=20, width=100)
    text_box.pack()

    message = tkinter.StringVar()

    entry = tkinter.Entry(main_window, textvariable=message, width=80)
    entry.bind("<Return>", send)
    entry.pack(side=tkinter.LEFT)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
        socket.connect((HOST, PORT))
        Thread(target=receive).start()
        set_name()
        main_window.mainloop()
