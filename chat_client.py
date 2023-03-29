import socket
import threading

# Constants
SERVER = '127.0.0.1'
PORT = 12345

# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(input('Enter your nickname: ').encode('utf-8'))
            else:
                print(message)
        except:
            print("Error! Connection closed.")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode('utf-8'))

# Request and set nickname
print("Enter your nickname: ")
nickname = input()

# Start threads for receiving and sending messages
receive
