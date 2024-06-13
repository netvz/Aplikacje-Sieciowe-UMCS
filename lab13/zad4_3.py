import socket
import threading
import os

class ClientThread(threading.Thread):
    def __init__(self, connection: socket.socket):
        threading.Thread.__init__(self)
        self.connection = connection

    def run(self):
        try:
            request = self.connection.recv(1024).decode()
            request_parts = request.split()
            command = request_parts[0]

            if command == "GET_IMAGE":
                if len(request_parts) > 1:
                    filename = request_parts[1]
                    if os.path.isfile(filename):
                        filesize = os.path.getsize(filename)
                        header = f"SIZE {filesize} NAME {filename}\r\n"
                        self.connection.send(header.encode())

                        with open(filename, 'r') as f:
                            while chunk := f.read(1024):
                                self.connection.send(chunk)
                    else:
                        self.connection.send("plik nie istnieje\r\n".encode())
                else:
                    self.connection.send("brak nazwy pliku\r\n".encode())
            elif command == "LIST_FILES":
                files = os.listdir('.')
                files_list = "\n".join(files) + "\r\n"
                self.connection.send(files_list.encode())
            else:
                self.connection.send("zla komenda\r\n".encode())
        except Exception as e:
            print(e)
        finally:
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

                client_thread = ClientThread(connection)
                client_thread.start()
        except socket.error as e:            
            print(e)


s = Server('127.0.0.1', 2904)
s.run()
