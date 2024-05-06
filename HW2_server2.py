# Завдання 2
# Реалізуйте клієнт-серверний додаток з можливістю надсилати файли. Один користувач ініціює надсилання файлу, другий
# підтверджує. Після підтвердження починається надсилання.
# Якщо відправка була вдалою, повідомте про це відправника.
import socket
import os

def receive_file(conn, file_path):
    with open(file_path, 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

def run_server():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen()
        print(f"Сервер працює на {host}:{port}")

        while True:
            conn, addr = server.accept()
            with conn:
                print(f"З'єднано з {addr}")
                while True:
                    filename = conn.recv(1024).decode()
                    if not filename:
                        break
                    print(f"Запит на відправку файлу: {filename}")
                    response = input("Ви бажаєте прийняти файл? (yes/no): ").lower()
                    if response == 'yes':
                        file_path = os.path.join('received_files', filename)
                        conn.sendall(b"OK")
                        receive_file(conn, file_path)
                        print(f"Файл {filename} успішно отримано.")
                    else:
                        conn.sendall(b"NO")
                        print("Відправка файлу відмовлена.")

if __name__ == "__main__":
    run_server()
