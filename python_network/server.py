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
