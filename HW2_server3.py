# Завдання 3
# Реалізуйте клієнт-серверний додаток , який дозволяє
# користувачам спілкуватися в одному чаті. Кожен користувач
# входить у чат під своїм логіном та паролем. Повідомлення,
# надіслане в чат, видно всім користувачам чату.
import socket
import threading

users = {
    "user1": "pass1",
    "user2": "pass2",
    "user3": "pass3"
}

clients = []


def client_handler(conn, addr):
    print(f"[+] Підключення: {addr}")

    conn.send("Логін: ".encode())
    username = conn.recv(1024).decode().strip()
    conn.send("Пароль: ".encode())
    password = conn.recv(1024).decode().strip()

    if username in users and users[username] == password:
        conn.send("Успішна автентифікація. Ви у чаті!\n".encode())
        clients.append(conn)
        broadcast(f"{username} приєднався до чату!\n".encode())
    else:
        conn.send("Помилка автентифікації.\n".encode())
        conn.close()
        return

    try:
        while True:
            message = conn.recv(1024)
            if not message:
                break
            broadcast(message, username)
    finally:
        clients.remove(conn)
        broadcast(f"{username} покинув чат.\n".encode())
        conn.close()


def broadcast(message, prefix=""):
    for client in clients:
        client.send(f"{prefix}: {message.decode()}".encode())


def run_server():
    host = 'localhost'
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Сервер запущений на {host}:{port}")

    try:
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=client_handler, args=(conn, addr))
            thread.start()
    except Exception as e:
        print(f"Помилка сервера: {e}")
    finally:
        server.close()


if __name__ == "__main__":
    run_server()
