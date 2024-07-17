import socket
import pyautogui
import time
import keyboard


class Server:
    server = 0
    client_socket = 0
    address = 0

    def __init__(self):
        # init server
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((socket.gethostname(), 1234))
        self.server.listen(5)
        self.init_client_socket()
        self.handler()

    def init_client_socket(self):
        self.client_socket, self.address = self.server.accept()
        print(f"connection formm {self.address} has been established")

    def handler(self):
        while True:
            m_k = self.client_socket.recv(1024).decode()
            if m_k == 'm':
                x, y = pyautogui.position()
                pyautogui.sleep(2)
                self.client_socket.send(str(x).encode())
                self.client_socket.send(str(y).encode())
                print()
            else:
                while True:
                    print("k")
                    time.sleep(0.2)
                    key = keyboard.read_key()
                    self.client_socket.send(key.encode())




Server()