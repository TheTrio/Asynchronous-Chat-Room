import socket
import threading
from termcolor import cprint, colored

HOST = "127.0.0.1"
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def color_address(host, port):
    return colored(f"{host}:{port}", "yellow", attrs=["bold"])


my_addr, my_port = s.getsockname()

cprint(f"Connected with {color_address(HOST, PORT)}", "magenta", attrs=["bold"])
cprint(
    f"You are identified as {color_address(my_addr, my_port)}", "green", attrs=["bold"]
)


def listen():
    while True:
        data = s.recv(1024)
        addr, message = data.decode().split("-", maxsplit=1)
        cprint(color_address(*addr.split(":")), "yellow", end=" ")
        print("sent", end=" ")
        cprint(message, "blue", end="")


def send_message():
    while True:
        text = f"{input()}\n"
        if text.strip() == "quit":
            s.close()
            cprint(
                f"Disconnected with {color_address(HOST, PORT)}",
                "magenta",
                attrs=["bold"],
            )
            return
        s.sendall(text.encode())


if __name__ == "__main__":
    thread1 = threading.Thread(target=listen, daemon=True)
    thread1.start()
    thread2 = threading.Thread(target=send_message)
    thread2.start()
