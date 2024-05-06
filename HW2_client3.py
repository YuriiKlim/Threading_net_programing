import socket


def client_program():
    host = 'localhost'
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    welcome_message = client.recv(1024).decode()
    print(welcome_message, end="")
    username = input()
    client.send(username.encode())

    password_message = client.recv(1024).decode()
    print(password_message, end="")
    password = input()
    client.send(password.encode())

    response = client.recv(1024).decode()
    print(response)

    if "Успішна автентифікація" in response:
        try:
            while True:
                message = input('-> ')
                client.send(message.encode())
                if message.lower() == 'exit':
                    break
        except KeyboardInterrupt:
            pass
        finally:
            client.close()


if __name__ == "__main__":
    client_program()
