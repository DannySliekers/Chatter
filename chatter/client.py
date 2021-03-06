import tkinter as tk
import socket
import unique_id
import atexit

HOST = 'localhost'
PORT = 4444
UNIQUE_ID = unique_id.generate_unique_id()


def sign_out():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        package = '___'.join(('SIGNOUT', UNIQUE_ID))
        s.sendall(bytes(package, 'utf-8'))
        s.recv(1024)
        print("test")


def send_message():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        package = '___'.join((UNIQUE_ID, input.get()))
        s.sendall(bytes(package, 'utf-8'))
        s.recv(1024)


def print_message():
    message = get_messages()
    if message != ' ':
        chat_box.configure(state=tk.NORMAL)
        formatted_output = UNIQUE_ID + ': ' + message + '\n'
        chat_box.insert(tk.END, formatted_output)
        input.delete(0, tk.END)
        chat_box.configure(state=tk.DISABLED)
    window.after(500, print_message)


def get_messages():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        package = '___'.join(('GETMESSAGE', UNIQUE_ID))
        s.sendall(bytes(package, 'utf-8'))
        message = s.recv(1024).decode('utf-8')
        return message


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    package = '___'.join(('SIGNIN', UNIQUE_ID))
    s.sendall(bytes(package, 'utf-8'))
    s.recv(1024)

window = tk.Tk()
window.title("Chatter")

input = tk.Entry(window, width=120)
input.grid(row=1, column=0)

send = tk.Button(window, text="Send", width=10, command=send_message)
send.grid(row=1, column=1)

chat_box = tk.Text(window, height=20, width=100)
chat_box.configure(state=tk.DISABLED)
chat_box.grid(row=0, column=0, columnspan=2)

window.after(500, print_message)
atexit.register(sign_out)
window.mainloop()
