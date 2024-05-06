import socket

def send_file(server_ip, server_port, file_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((server_ip, server_port))
        filename = file_path.split('/')[-1]
        client.sendall(filename.encode())
        response = client.recv(1024).decode()
        if response == "OK":
            with open(file_path, 'rb') as f:
                while (chunk := f.read(1024)):
                    client.sendall(chunk)
            print("Файл успішно відправлено.")
        else:
            print("Сервер відмовив у прийомі файлу.")

def main():
    server_ip = 'localhost'
    server_port = 12345
    file_path = input("Введіть шлях до файлу для відправки: ")
    send_file(server_ip, server_port, file_path)

if __name__ == "__main__":
    main()
