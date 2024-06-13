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
    non_flagged = []
    for i in range(0, len(inboxes)):
        client_socket.send(f"A{identifier} SELECT {inboxes[i]}\r\n".encode())
        msg = client_socket.recv(2048).decode()
        if not msg.startswith(f"A{identifier} BAD"):
            identifier = identifier+1
            client_socket.send(f"A{identifier} FETCH 1:* (FLAGS)\r\n".encode())
            msg = client_socket.recv(2048).decode()
            if not msg.__contains__("Invalid messageset"):
                msg = msg.split("\r\n")[0:-2]
                for i in msg:
                    if not i.__contains__("\Seen"):
                        non_flagged.append([int(word) for word in i.split() if word.isdigit()])
        for i in non_flagged:
            identifier = identifier+1
            client_socket.send(f"A{identifier} FETCH {i} BODY[]\r\n".encode())
            msg_cont = client_socket.recv(2048).decode()
            print(msg_cont)
            identifier = identifier+1
            client_socket.send(f"A{identifier} STORE {i} +FLAGS \Seen\r\n".encode())           
            
else:
    print("zle dane logowania")
    exit

