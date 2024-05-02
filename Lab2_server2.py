# Завдання 2
# Реалізуйте клієнт-серверний додаток погоди. Клієнт
# звертається до сервера із зазначенням країни та міста.
# Сервер, отримавши запит, видає погоду на тиждень для
# вказаної місцевості. Використовуйте для реалізації додатку багатопотокові механізми. Дані про погоду мають
# бути наперед визначеними та взяті з файлу.
import socket
import threading
import json


def client_handler(conn, addr, weather_data):
    try:
        print(f"З'єднано з {addr}")
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            country, city = data.split(',')
            response = weather_data.get(country.strip(), {}).get(city.strip(), "No weather data available.")
            conn.sendall(json.dumps(response).encode())
    finally:
        conn.close()

def run_server():
    host = '127.0.0.1'
    port = 8080
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen()
        print(f"Сервер працює на {host}:{port}")
        with open('weather.json', 'r') as f:
            weather_data = json.load(f)
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=client_handler, args=(conn, addr, weather_data))
            thread.start()


if __name__ == "__main__":
    run_server()
