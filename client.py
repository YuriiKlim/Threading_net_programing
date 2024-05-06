## Client
import socket


client = socket.socket(socket.AF_INET,     # use IP4
                       socket.SOCK_STREAM  # use TCP
                       )

client.connect(('127.0.0.1', 8080))

while True:
    data = input("Enter something: ")

    client.send(data.encode())

    if data == 'exit':
        break

client.close()