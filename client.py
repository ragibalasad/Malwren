import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMATE = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
