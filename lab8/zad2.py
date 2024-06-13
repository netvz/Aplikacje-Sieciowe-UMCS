import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("dsmka.wintertoad.xyz", 143))
client_socket.recv(2048)
client_socket.send("A1 LOGIN test1@wintertoad.xyz P@ssw0rd\r\n".encode())
msg = client_socket.recv(2048).decode()
if(msg.startswith("A1 OK")):
    client_socket.send("A2 STATUS INBOX (MESSAGES)\r\n".encode())
    msg = client_socket.recv(2048).decode()
    if not msg.startswith("A2 BAD"):
        number = msg.split("\r\n")[0].split(" ")[-1].strip(")")
        print(f"liczba wiadomosci w skrzynce: {number}")
else:
    print("zle dane logowania")
    exit

