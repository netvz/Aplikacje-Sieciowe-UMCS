import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("dsmka.wintertoad.xyz", 110))
client_socket.recv(2048)
client_socket.send("USER test1@wintertoad.xyz\r\n".encode())
msg = client_socket.recv(2048)
if(msg.startswith("+OK")):
    client_socket.send("PASS P@ssw0rd\r\n".encode())
else:
    print("zle dane logowania")
    exit

msg = client_socket.recv(2048).decode()

if(msg.startswith("+OK")):
    client_socket.send("STAT\r\n".encode())
    msg = client_socket.recv(2048)

    print("Ilosc bajtów zajmowanych przez wiadomości: " + msg.split(" ")[2])

else:
    print("zle dane logowania")
    exit

