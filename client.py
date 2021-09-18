from tkinter import *
import socket

HOST = 'localhost'
PORT = 4444

def send_message():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bytes(input.get(), 'utf-8'))
        data = s.recv(1024)
    chat_box.configure(state=NORMAL)
    message = input.get()
    chat_box.insert(END, message + '\n')
    chat_box.configure(state=DISABLED)
    print('Received', data.decode('utf-8'))

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
