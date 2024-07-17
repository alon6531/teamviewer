import socket
import time
import keyboard
import pyautogui


class Client:
    client = 0

    def __init__(self):
        # init client
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((socket.gethostname(), 1234))
        self.handler()

    def handler(self):
        while True:
            print("m or k")
            m_k = input()
            self.client.send(str(m_k).encode())
            if m_k == 'm':
                pyautogui.moveTo( int(self.client.recv(1024).decode()))
                pyautogui.moveTo(int(self.client.recv(1024).decode()))
            else:
                while True:
                    key = self.client.recv(1024).decode()
                    if key:
                        keyboard.send(key)
                        key = None


Client()