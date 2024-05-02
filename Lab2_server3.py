# Завдання 3
#  Створіть клієнтсько-серверний додаток, де клієнт
# надсилає рядок тексту або слово на сервер для
# перекладу на іншу мову. Сервер повертає переклад і
# відправляє його клієнту. Наприклад, клієнт надсилає
# рядок "Hello, how are you?" на сервер, а сервер повертає
# переклад цього рядка на вказану мову.
import socket
import translators as ts


def translate(text, src, dest):
    try:
        return ts.translate_text(text, from_language=src, to_language=dest)
    except Exception as e:
        return f'Помилка при перекладі: {e}'


def handle_client(connection):
    try:
        while True:
            data = connection.recv(1024).decode()
            if not data:
                break
            print(f"Отримано текст для перекладу: {data}")
            translation = translate(data, 'en', 'uk')
            connection.sendall(translation.encode())
    finally:
        connection.close()


def run_server():
    host = '127.0.0.1'
    port = 8080
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen()
        print(f"Сервер запущено на {host}:{port}")
        while True:
            conn, addr = server.accept()
            print(f"З'єднано з {addr}")
            handle_client(conn)


if __name__ == "__main__":
    run_server()
