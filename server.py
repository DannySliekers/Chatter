import socket

HOST = ''
PORT = 4444

message_queue = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, adress = s.accept()
        with conn:
            print('Connected by', adress)
            if not message_queue:
                conn.sendall(b' ')
            else:
                for message in message_queue:
                    conn.sendall(message_queue.pop(0))
            data = conn.recv(1024)
            message_queue.append(data)
            if not data: break