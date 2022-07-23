import socket
import requests

# API
URL = "https://api.ngrok.com/endpoints"
headers = {'Ngrok-Version': "2",
           'Authorization': "Bearer 2CI6sbfv4heZOCdC02O7xFtGEyc_5zWyf7cr8oNDLWQH4EXhE"}
response = requests.request("GET", URL, headers=headers).text
print(response.split(',')[6].strip()[12:32])  # gets ip and port
# print(response.split(',')[6].strip()[12:26])  # gets ip
# print(response.split(',')[6].strip()[27:32])  # gets port


# Variables
HEADER = 64
PORT = int(response.split(',')[6].strip()[27:32])
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = response.split(',')[6].strip()[12:26]
ADDR = (SERVER, PORT)
# ADDR = (input("IP: "), int(input("Port: ")))
# player_number = 1

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# receive_message = "0,0"
receive_message = ""


def send(msg):
    # global receive_message
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


    # receive_message = client.recv(2048).decode(FORMAT)
    # player_number = receive_message[0:1]
    # player_move = receive_message[2:3]
    # print(player_number, player_move)


def receive():
    global receive_message
    receive_message = client.recv(2048).decode(FORMAT)
    print(receive_message)


def get_player_move():
    global receive_message
    player_move = receive_message[2:3]
    return player_move


def get_player_number():
    global receive_message
    # global player_number
    player_number = receive_message[0:1]
    # player_number = 1
    return player_number





# def send(self, data):
#     """
#     :param data: str
#     :return: str
#     """
#     try:
#         self.client.send(str.encode(data))
#         reply = self.client.recv(2048).decode()
#         return reply
#     except socket.error as e:
#         return str(e)

# input_message = 1
# while input_message != "exit":
#     input_message = str(input())
#     send(input_message)
#
# send(DISCONNECT_MESSAGE)
