import socket, sys, threading
import random

class ClientThread(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.connection = connection

    def run(self):
        number = random.randint(0, 1000)

        while True:
            data = self.connection.recv(8192)
            num = int(data.decode())

            if num < number:
                self.connection.send("too smol :( try again\n".encode())
            elif num > number:
                self.connection.send("too big :( try again\n".encode())
            elif num == number:
                self.connection.send("correcto :D \n".encode())
                self.connection.close()


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def run(self):
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((self.ip, self.port))
            server_socket.listen()

            while True:
                connection, address = server_socket.accept()

                c = ClientThread(connection)
                c.start()

        except socket.error as e:
            print("socket error")

s = Server('127.0.0.1', 10000)
s.run()