import socket

HOST = ''
PORT = 4444

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, adress = s.accept()
    with conn:
        print('Connected by', adress)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)
