import socket
import threading

HOST = "127.0.0.1"
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def listen():
    while True:
        data = s.recv(3)
        print(data.decode(), end="")


def send_message():
    while True:
        text = f"{input()}\n"
        if text.strip() == "quit":
            s.close()
            return
        s.sendall(text.encode())


if __name__ == "__main__":
    thread1 = threading.Thread(target=listen, daemon=True)
    thread1.start()
    thread2 = threading.Thread(target=send_message)
    thread2.start()
