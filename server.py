import socket
import threading

HOST = ''
PORT = 4444

message_queue = []

#todo add unique ids and handle messages that way also something something usernames
def handle_messages(conn):
    with conn:
        if not message_queue:
            conn.sendall(b' ')
        else:
            conn.sendall(message_queue.pop(0))
        data = conn.recv(1024)
        if data != b' ':
            message_queue.append(data)
            message_queue.append(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, adress = s.accept()
        print('Connected by', adress)
        client_thread = threading.Thread(target=handle_messages(conn))
        client_thread.start()