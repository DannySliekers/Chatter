from tkinter import *
import socket

HOST = 'localhost'
PORT = 4444

def send_message():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        if not input.get():
            s.sendall(b' ')
        else:
            s.sendall(bytes(input.get(), 'utf-8'))

def print_message():
    message, name = get_messages()
    chat_box.configure(state=NORMAL)
    formatted_output = name + ': ' + message + '\n'
    chat_box.insert(END, formatted_output)
    input.delete(0, END)
    chat_box.configure(state=DISABLED)
    window.after(500, print_message)

def get_messages():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = s.recv(1024).decode('utf-8')
        name = str(s.getsockname())
        return message, name


window = Tk()
window.title("Chatter")

input = Entry(window, width=120)
input.grid(row=1, column=0)

send = Button(window, text="Send", width=10, command=send_message)
send.grid(row=1, column=1)

chat_box = Text(window, height=20, width=100)
chat_box.configure(state=DISABLED)
chat_box.grid(row=0, column=0, columnspan=2)

window.after(500, print_message)
window.mainloop()
