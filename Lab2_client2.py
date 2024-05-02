import socket

def run_client():
    host = '127.0.0.1'
    port = 8080
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))
        while True:
            country = input("Введіть країну: ")
            city = input("Введіть місто: ")
            client.sendall(f"{country}, {city}".encode())
            response = client.recv(1024).decode()
            print("Погода на тиждень:")
            print(response)
            if input("Ще один запит? (y/n): ").lower() != 'y':
                break


if __name__ == "__main__":
    run_client()
