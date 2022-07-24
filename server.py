import socket
# import sys
import threading

HEADER = 64
PORT = 5050
# Server Machine IP
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# print(SERVER)
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
            # conn.send("Msg received".encode(FORMAT))
            with lock:
                for c in all_clients:
                    c.sendall(f"{msg}".encode(FORMAT))

    conn.close()

# currentId = "1"
# pos = ["1,", "2,"]
# def handle_client(conn):
#     global currentId, pos
#     conn.send(str.encode(currentId))
#     currentId = "2"
#     reply = ''
#     while True:
#         try:
#             data = conn.recv(2048)
#             reply = data.decode('utf-8')
#             if not data:
#                 conn.send(str.encode("Goodbye"))
#                 break
#             else:
#                 print("Received: " + reply)
#                 arr = reply.split(":")
#                 id = int(arr[0])
#                 pos[id] = reply
#
#                 if id == 1: nid = 2
#                 if id == 2: nid = 1
#
#                 reply = pos[nid][:]
#                 print("Sending: " + reply)
#
#             conn.sendall(str.encode(reply))
#         except:
#             break
#
#     print("Connection Closed")
#     conn.close()


def start():
    server.listen(2)  # Max connections: 2
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # server_command = input("Type \"exit\" to close server\n")
        # if server_command == "exit":
        #     sys.exit()
        conn, addr = server.accept()
        with lock:
            all_clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        print(all_clients)


# def get_connection_count():
#     return threading.active_count()-1


print("[STARTING] server is starting...")
start()

