import socket
import numpy as np


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("dsmka.wintertoad.xyz", 110))
client_socket.recv(2048)
client_socket.send("USER test1@wintertoad.xyz\r\n".encode())
msg = client_socket.recv(2048).decode()
if(msg.startswith("+OK")):
    client_socket.send("PASS P@ssw0rd\r\n".encode())
else:
    print("zle dane logowania")
    exit

msg = client_socket.recv(2048).decode()

def recv_all_until(sockfd, crlf):
    data = b""
    while not data.endswith(crlf):
        data = data + sockfd.recv(1)
    return data

if(msg.startswith("+OK")):
    client_socket.send("LIST\r\n".encode())
    
    msg = recv_all_until(client_socket, ".".encode()).decode().split("\r\n")
    
    msg_temp = msg[1:-1]
    msg_bytes = [int(msg_temp[i].split(" ")[1]) for i in range(0, len(msg_temp))]
    length = len(msg_bytes)

    maximum = np.max(msg_bytes)
    print(maximum)
    print(msg_bytes)

    for i in range(0, length):
        if(msg_bytes[i] == maximum):
            client_socket.send(f"RETR {i+1}\r\n".encode())
            msg = client_socket.recv(20480).decode()
            print(msg)
            break

else:
    print("zle dane logowania")
    exit

