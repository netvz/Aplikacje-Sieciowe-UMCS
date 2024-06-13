import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 143))
server_socket.listen()

while True:
    client_socket, addr = server_socket.accept()
    client_socket.send("* OK IMAP4rev1 Service Ready\r\n".encode())

    while True:
        try:
            request = client_socket.recv(1024).decode()
            
            if not request:
                break
            
            print(f"otrzymana komenda: {request.strip()}")
            
            command = request.split()
            
            if command[1] == "LOGIN":
                client_socket.send(f"{command[0]} OK LOGIN completed\r\n".encode())
            elif command[1] == "LIST":
                response = f"{command[0]} OK LIST completed\r\n"
                client_socket.send(response.encode())
            elif command[1] == "SELECT":
                response = f"{command[0]} OK SELECT completed\r\n"
                client_socket.send(response.encode())
            elif command[1] == "STORE":
                response = f"{command[0]} OK STORE completed\r\n"
                client_socket.send(response.encode())
            elif command[1] == "EXPUNGE":
                response = f"{command[0]} OK EXPUNGE completed\r\n"
                client_socket.send(response.encode())
            else:
                response = f"{command[0]} BAD Command not recognized\r\n"
                client_socket.send(response.encode())
        
        except Exception as e:
            print(f"error: {e}")
            break

    client_socket.close()
