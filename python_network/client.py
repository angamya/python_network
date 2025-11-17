import socket
import threading

nickname=input("Write a nickname: ")

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 77777))

def receive():
    while True:
        try:
            message=client.recv(1024).decode("ascii")
            if message =="NICK":
                pass
            else:
                print(message)
        except:
            print("an error occured!")
            client.close()
            break
        #lolipop
            

            

