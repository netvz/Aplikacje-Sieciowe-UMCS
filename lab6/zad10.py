import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 2005))
server_socket.listen()

client_socket, address = server_socket.accept()
client_socket.send("220 dsmka.wintertoad.xyz ESMTP\r\n".encode())
    
while True:
    data = client_socket.recv(2048)
    if not data:
        break
        
    command = data.decode().strip()
        
    if command.startswith("EHLO"):
        client_socket.send("250-dsmka.wintertoad.xyz\r\n250-AUTH LOGIN PLAIN\r\n250 SIZE 10240000\r\n".encode())
    elif command == "AUTH LOGIN":
        client_socket.send("334 VXNlcm5hbWU6\r\n".encode())
    elif command == "BASE64_ENCODED_USERNAME":
        client_socket.send("334 UGFzc3dvcmQ6\r\n".encode())
    elif command == "BASE64_ENCODED_PASSWORD":
        client_socket.send("235 2.7.0 Authentication successful\r\n".encode())
    elif command.startswith("MAIL FROM:"):
        client_socket.send("250 2.1.0 Ok\r\n".encode())
    elif command.startswith("RCPT TO:"):
        client_socket.send("250 2.1.5 Ok\r\n".encode())
    elif command == "DATA":
        client_socket.send("354 End data with <CR><LF>.<CR><LF>\r\n".encode())
        while True:
            data = client_socket.recv(1024)
            if data.strip() == ".".encode():
                break
        client_socket.send("250 2.0.0 Ok: queued as ABC123\r\n".encode())
    elif command == "QUIT":
        client_socket.send("221 2.0.0 Bye\r\n".encode())
        break
    else:
        client_socket.send("Podaj wlasciwa komende\r\n".encode())
    
client_socket.close()
server_socket.close()




