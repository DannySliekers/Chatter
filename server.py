import socket
import threading

HOST = ''
PORT = 4444

message_queue = []
unique_ids_connected = []


def generate_messages_for_unique_id():
    pass


#todo add a message for every single unique id connected
def handle_send_message(package):
    message_package = '___'.join(package)
    message_queue.append(message_package)


def handle_get_message(unique_id):
    for messages in message_queue:
        message_package = messages.split('___')
        if unique_id == message_package[0]:
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


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, adress = s.accept()
        print('Connected by', adress)
        client_thread = threading.Thread(target=handle_action(conn))
        client_thread.start()