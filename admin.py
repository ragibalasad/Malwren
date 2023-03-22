################## A D M I N #########################
import socket

HEADER = 64
PORT = 5050
SERVER = "192.168.1.102"
ADDR = (SERVER, PORT)
FORMATE = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMATE)
    msg_length = len(message)
    send_lenght = str(msg_length).encode(FORMATE)
    send_lenght += b' ' * (HEADER-len(send_lenght))

    client.send(send_lenght)
    client.send(message)


################## A D M I N #########################
send("2004528")
################## A D M I N #########################

while True:
    inp = input("@admin~$ ")
    send(inp)