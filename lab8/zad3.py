import socket
   

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("dsmka.wintertoad.xyz", 143))
client_socket.recv(2048)
client_socket.send("A1 LOGIN test1@wintertoad.xyz P@ssw0rd\r\n".encode())
msg = client_socket.recv(2048).decode()
if(msg.startswith("A1 OK")):

    inboxes = []
    client_socket.send("A2 LIST \"\" *\r\n".encode())
    msg = client_socket.recv(2048).decode()
    if not msg.startswith("A2 BAD"):
        msg = msg.split("\r\n")[0:-2]
        print(len(msg))
        for i in range(0, len(msg)):
            msg[i] = msg[i].split(" ")
        inboxes = [sublist[-1] for sublist in msg]
    
    identifier = 3
    sum = 0
    for i in range(0, len(inboxes)):
        client_socket.send(f"A{identifier} STATUS {inboxes[i]} (MESSAGES)\r\n".encode())
        msg = client_socket.recv(2048).decode()
        if not msg.startswith(f"A{identifier} BAD"):
            number = int(msg.split("\r\n")[0].split(" ")[-1].strip(")"))
            sum += number
            identifier = identifier+1

    print(f"suma wiadomosci w skrzynkach: {sum}")

else:
    print("zle dane logowania")
    exit

