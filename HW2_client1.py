import socket

def run_client():
    host = '100.0.0.1'
    port = 12345
    last_char = None

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))
        print("Підключено до сервера.")
        client.sendall("start".encode())

        while True:
            server_data = client.recv(1024).decode()
            if not server_data or server_data == "stop":
                print("Гра закінчена.")
                break

            print(f"Сервер: {server_data}")
            last_char = server_data[-1] if server_data else None

            while True:
                client_word = input(f"Введіть слово, яке починається на '{last_char}': ")
                if client_word == "stop":
                    client.sendall(client_word.encode())
                    print("Ви вийшли з гри.")
                    return
                if not client_word.startswith(last_char):
                    print(f"Слово повинно починатися на '{last_char}'. Спробуйте ще раз.")
                else:
                    break

            client.sendall(client_word.encode())

if __name__ == "__main__":
    run_client()
