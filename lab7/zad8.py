import socket

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
    print("uehfuehf")    
    
    msg = recv_all_until(client_socket, ".".encode()).decode().split("\r\n")

    print("Ilość bajtów zajmowanych przez poszczegolne wiadomosci:")
    
    for i in range(1,5):
        print(msg[i])


else:
    print("zle dane logowania")
    exit

