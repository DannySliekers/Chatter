from tkinter import *
import socket

HOST = 'localhost'
PORT = 4444

def connect():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bytes(input.get(), 'utf-8'))
        data = s.recv(1024)
        return data

def send_message():
    chat_box.configure(state=NORMAL)
    message = connect().decode('utf-8')
    chat_box.insert(END, message + '\n')
    input.delete(0, END)
    chat_box.configure(state=DISABLED)

window = Tk()
window.title("Chatter")

input = Entry(window, width=120)
input.grid(row=1, column=0)

send = Button(window, text="Send", width=10, command=send_message)
send.grid(row=1, column=1)

chat_box = Text(window, height=20, width=100)
chat_box.configure(state=DISABLED)
chat_box.grid(row=0, column=0, columnspan=2)

window.mainloop()
