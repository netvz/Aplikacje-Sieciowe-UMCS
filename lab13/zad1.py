import socket
import threading
import os

if not os.path.exists("uploads"):
    os.makedirs("uploads")

class ClientThread(threading.Thread):
    def __init__(self, connection: socket.socket):
        threading.Thread.__init__(self)
        self.connection = connection

    def run(self):
        try:
            file = None
            while True:
                data = self.connection.recv(8192).decode()
                if not data:
                    break

                lines = data.split('\n')
                for line in lines:
                    if line.startswith('UPLOAD'):
                        _, filename = line.split(maxsplit=1)
                        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                            self.connection.send("tylko pliki graficzne\n".encode())
                            continue
                        file_path = os.path.join("uploads", filename)
                        file = open(file_path, 'w')
                        self.connection.send(b"OK\n")
                    elif line.startswith('DATA'):
                        if file:
                            file.write(line[len('DATA '):].encode())
                        self.connection.send("OK\n".encode())
                    elif line.startswith('END'):
                        if file:
                            file.close()
                            file = None
                        self.connection.send(b"OK\n")
                    else:
                        self.connection.send("niewłaściwa komenda.\n".encode())
        except Exception as e:
            print(e)
        finally:
            if file and not file.closed:
                file.close()
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
            print(f"Socket error: {e}")


s = Server('127.0.0.1', 65432)
s.run()
