## Server
import socket


server = socket.socket(socket.AF_INET, #use IP4
                       socket.SOCK_STREAM) #use TCP

server.bind(('127.0.0.1', 8080))
server.listen(1)

while True:
    print("waiting...")
    client, address = server.accept()
    print(f"conection fron {address}")

    date = client.recv(1024)