import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 1100))  
server.listen()

try:
    while True:
        client_socket, addr = server.accept()
        client_socket.send("+OK POP3 server ready\r\n".encode())

        quit = False
        
        while not quit:
            try:
                request = client_socket.recv(1024).decode()
            except ConnectionResetError:
                break

            if not request:
                break
            
            print(f"otrzymana komenda {request.strip()}")
            
            command = request.strip().split(" ")[0].upper()
            
            if command == "USER":
                client_socket.send("+OK User accepted\r\n".encode())
            elif command == "PASS":
                client_socket.send("+OK Password accepted\r\n".encode())
            elif command == "STAT":
                client_socket.send("+OK 1 100\r\n".encode())  
            elif command == "LIST":
                client_socket.send("+OK 1 messages (100 octets)\r\n1 100\r\n.\r\n".encode())
            elif command == "RETR":
                client_socket.send("+OK 100 octets\r\nFrom: test1@dsmka.xyz\r\nTo: test2@dsmka.xyz\r\nSubject: Test\r\n\r\nBLABLABLABLABLABLA.\r\n.\r\n".encode())
            elif command == "QUIT":
                client_socket.send("+OK POP3 server signing off\r\n".encode())
                quit = True
            else:
                client_socket.send("-ERR Command not recognized\r\n".encode())
        
        client_socket.close()
        
except KeyboardInterrupt:
    print("\nerror")
finally:
    server.close()






    


