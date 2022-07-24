import socket
import threading

# Variables
HEADER = 64
PORT = 5050
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
lock = threading.Lock()
all_clients = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.\n")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 2}")

            print(f"[{addr}] {msg}")
            with lock:
                for c in all_clients:
                    c.sendall(f"{msg}".encode(FORMAT))

    conn.close()


def start():
    server.listen(2)  # Max connections: 2
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        with lock:
            all_clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        print(all_clients)


print("[STARTING] server is starting...")
start()
