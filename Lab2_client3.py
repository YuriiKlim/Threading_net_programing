import socket

def run_client():
    host = '127.0.0.1'
    port = 8080
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))
        while True:
            text_to_translate = input("Введіть текст (або натисніть enter для виходу): ")
            if text_to_translate == "":
                break
            client.sendall(text_to_translate.encode())
            translated_text = client.recv(1024).decode()
            print(f"Перекладений текст: {translated_text}")

if __name__ == "__main__":
    run_client()
