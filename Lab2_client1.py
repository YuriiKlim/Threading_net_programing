import socket


def client():
    host = '127.0.0.1'
    port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = input("Напишіть повідомлення: ")

    while message.lower().strip() != 'exit':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(f"Відповідь від сервера: {data}")
        message = input("Напишіть повідомлення: ")

    client_socket.close()


if __name__ == '__main__':
    client()
