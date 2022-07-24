import socket
import requests

# API
URL = "https://api.ngrok.com/endpoints"
headers = {'Ngrok-Version': "2",
           'Authorization': "Bearer 2CI6sbfv4heZOCdC02O7xFtGEyc_5zWyf7cr8oNDLWQH4EXhE"}
response = requests.request("GET", URL, headers=headers).text


# print(response.split(',')[6].strip()[12:32])  # gets ip and port
# print(response.split(',')[6].strip()[12:26])  # gets ip
# print(response.split(',')[6].strip()[27:32])  # gets port


# Variables
HEADER = 64
PORT = int(response.split(',')[6].strip()[27:32])
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = response.split(',')[6].strip()[12:26]
ADDR = (SERVER, PORT)
receive_message = "0,0"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


# Send to server function
def send(msg):
    # global receive_message
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


# Receive from server function
def receive():
    global receive_message
    receive_message = client.recv(2048).decode(FORMAT)
    print(receive_message)


# Get player move (column number)
def get_player_move():
    global receive_message
    player_move = int(receive_message[2:3])
    return player_move


# Get player number (Player 1: 1, Player 2: 2)
def get_player_number():
    global receive_message
    player_number = int(receive_message[0:1])
    return player_number
