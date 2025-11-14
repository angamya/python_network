import socket
import threading

host='127.0.0.1'
port = 77777

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients=[]
nicknames=[]

def broadcast(message):
    for client in clients:
        client.send(message)

def connect(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            index=client.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            broadcast(f"{nickname} bye the chat!".encode('ascii') )
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address =server.accept()
        print(f"Connect with {str(address)}")

        client.send('NICK'.encode('ascii')) 
        nickname=client.recv(1024).decode('ascii')
