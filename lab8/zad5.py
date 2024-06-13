import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("dsmka.wintertoad.xyz", 143))
client_socket.recv(2048)
client_socket.send("A1 LOGIN test2@wintertoad.xyz P@ssw0rd\r\n".encode())
msg = client_socket.recv(2048).decode()
if(msg.startswith("A1 OK")):

    inboxes = []
    client_socket.send("A2 LIST \"\" *\r\n".encode())
    msg = client_socket.recv(2048).decode()
    if not msg.startswith("A2 BAD"):
        msg = msg.split("\r\n")[0:-2]
        for i in range(0, len(msg)):
            msg[i] = msg[i].split(" ")
        inboxes = [sublist[-1] for sublist in msg]
    
    for i in range(0, len(inboxes)):
        print(f"{i} {inboxes[i]}")
    inbox = int(input("wybierz skrzynke: "))
    
    client_socket.send(f"A3 SELECT {inboxes[inbox]}\r\n".encode())
    msg = client_socket.recv(2048).decode()
    number = input("podaj numer wiadomosci do usuniecia: ")
    client_socket.send(f"A4 STORE {number} +FLAGS \Deleted\r\n".encode())
    msg = client_socket.recv(2048).decode()
    if not msg.startswith(f"A4 BAD"):
        client_socket.send(f"A5 EXPUNGE\r\n".encode())
        msg = client_socket.recv(2048).decode()
        if not msg.startswith(f"A5 BAD"):
            print("usunieto")
   



else:
    print("zle dane logowania")
    exit

