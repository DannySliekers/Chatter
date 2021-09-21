import socket
import threading

HOST = ''
PORT = 4444

message_queue = []
unique_ids_connected = []


def handle_sign_out(package):
    for index, unique_id in enumerate(unique_ids_connected):
        if unique_id == package:
            unique_ids_connected.pop(index)


# todo add a message for every single unique id connected
def handle_send_message(package):
    for i in range(len(unique_ids_connected)):
        message_queue.append('___'.join((unique_ids_connected[i], package[1])))


def handle_get_message(unique_id):
    for index, messages in enumerate(message_queue):
        message_package = messages.split('___')
        if unique_id == message_package[0]:
            message_queue.pop(index)
            return message_package[1]


def handle_sign_in(unique_id):
    unique_ids_connected.append(unique_id)


def handle_action(conn):
    with conn:
        package_received = conn.recv(1024).decode('utf-8').split('___')
        if package_received[0] == 'SIGNIN':
            handle_sign_in(package_received[1])
        elif package_received[0] == 'GETMESSAGE':
            if not message_queue:
                conn.sendall(b' ')
            else:
                message = handle_get_message(package_received[1])
                conn.sendall(bytes(message, 'utf-8'))
        elif package_received[0] in unique_ids_connected:
            handle_send_message(package_received)
        elif package_received[0] == 'SIGNOUT':
            handle_sign_out(package_received[1])


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, adress = s.accept()
        print('Connected by', adress)
        client_thread = threading.Thread(target=handle_action(conn))
        client_thread.start()
