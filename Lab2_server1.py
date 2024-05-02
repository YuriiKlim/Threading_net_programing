# Завдання 1
# Реалізуйте клієнт-серверний додаток з можливістю
# зворотного обміну повідомленнями. Для початку спілкування встановіть з’єднання. Після з’єднання використайте текстовий формат. У бесіді беруть участь лише дві
# особи. Після завершення спілкування сервер
import socket

def run_server():
    host = '127.0.0.1'
    port = 8080
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Сервер запущений на {host}:{port}, очікування з'єднань...")
    while True:
        conn, addr = server.accept()
        with conn:
            print(f"З'єднано з {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Повідомлення від клієнта: {data.decode()}")
                response = input("Введіть відповідь: ")
                conn.sendall(response.encode())
            print("З'єднання закрито, очікування нового учасника...")


if __name__ == '__main__':
    run_server()
