import socket
import threading

AUTH = "2004528"
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMATE = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
connections = []
super_client = None
target_client = None

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    #print(f"[NEW CONNECION] {addr} connected.")
    connections.append(conn)

    command("list")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMATE)

        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMATE)

            # Check for admin client
            if msg == AUTH:
                super_client = conn

            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            print(f"[{addr}] {msg}")
    
    conn.close   


def command(cmd):
    if cmd == "list":
        for client in connections:
            client.split(",")


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()