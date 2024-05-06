# Завдання 1
# Реалізуйте клієнт-серверний додаток, що дозволяє двом
# користувачам грати в гру «Хрестики — нулики». Один із
# гравців ініціює гру. Якщо другий гравець підтверджує, то
# гра починається. Гру можна припинити. Той хто припинив
# гру — програв. Після завершення гри можна ініціювати повторний матч.
import socket

def handle_client(conn, addr):
    print(f"Підключено {addr}")
    game_active = False
    last_char = None
    server_turn = True

    try:
        while True:
            if server_turn:
                server_word = input(f"Введіть слово, яке починається на '{last_char}': ")
                if game_active and last_char and not server_word.startswith(last_char):
                    print(f"Слово має починатися на '{last_char}'.")
                    continue
                conn.sendall(server_word.encode())
                last_char = server_word[-1] if server_word else None
                server_turn = False

            data = conn.recv(1024).decode()
            if not data or data == "stop":
                break
            if data == "start":
                game_active = True
                print("Гра розпочалася.")
                continue

            client_word = data
            print(f"Клієнт: {client_word}")
            if game_active and last_char and not client_word.startswith(last_char):
                print(f"Слово має починатися на '{last_char}'.")
                server_turn = True
                continue
            last_char = client_word[-1] if client_word else None
            server_turn = True
    finally:
        conn.close()
        print(f"З'єднання з {addr} завершено.")


def run_server():
    host = '100.0.0.1'
    port = 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen()
        print(f"Сервер чекає на з'єднання на {host}:{port}")
        conn, addr = server.accept()
        handle_client(conn, addr)


if __name__ == "__main__":
    run_server()



