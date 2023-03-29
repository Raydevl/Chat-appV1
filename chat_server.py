import socket
import threading

# Constants
SERVER = '127.0.0.1'
PORT = 12345

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f'{nickname} left the chat!'.encode('utf-8'))
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname is {nickname}!")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()
``
##This is incomplete i think, we need to replace the IP adress with the home computer IP adress, and debug for any code errors.
