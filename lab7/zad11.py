import socket
import re
import base64


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
    length = len(msg[1:-1])
    for i in range(0, length):
        client_socket.send(f"RETR {i+1}\r\n".encode())
        msg = client_socket.recv(20480).decode()
        print(msg)

    data = re.findall(r"--sep(.*)--sep--", msg, re.DOTALL)[0]
    filename = re.findall(r"filename=\"(.*)\"", data)[0]
    file = base64.b64decode(re.findall(r"base64(.*)$", data, re.DOTALL)[0].replace("\n", ""))

    f = open(filename, "w")
    f.write(file)
    f.close()

    print(f"nazwa pliku: {filename}")

else:
    print("zle dane logowania")
    exit

