import socket
from time import sleep

HEADER = 64
PORT = 5050
SERVER = "192.168.1.102"
ADDR = (SERVER, PORT)
FORMATE = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        client.connect(ADDR)
        print(f"Connected to {SERVER}:{PORT}")
    except:
        print("Couldn't connect to the server! Reconnecting...")
        sleep(1)
        continue
    break

def send(msg):
    message = msg.encode(FORMATE)
    msg_length = len(message)
    send_lenght = str(msg_length).encode(FORMATE)
    send_lenght += b' ' * (HEADER-len(send_lenght))

    client.send(send_lenght)
    client.send(message)

send(DISCONNECT_MESSAGE)