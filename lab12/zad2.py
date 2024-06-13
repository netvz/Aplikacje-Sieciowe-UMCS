import socket, sys, threading
from datetime import datetime

class ClientThread(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.connection = connection

    def run(self):
        while True:
            data = self.connection.recv(8192)
            self.connection.send(data)


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
                date_string = f"{datetime.now()}"

                f = open("wszystkie_zdarzenia.txt", "w")
                f.write(date_string)
                f.write(str(address[0]))
                f.write("   ")
                f.write(str(address[1]))
                f.flush()

        except socket.error as e:
            print("socket error")

s = Server('127.0.0.1', 10000)
s.run()