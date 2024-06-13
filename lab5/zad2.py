import socket
import random

scket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
scket.bind(('127.0.0.1', 2912))
scket.listen()

connection, adress = scket.accept()

random_number = random.randint(1, 1000)
print(random_number)

while True:
    msg = connection.recv(2048)
    try:
        client_number = int(msg.decode())
    except:
        connection.send("only integers are accepted!\n".encode())
        continue
    
    if client_number < random_number:
        connection.send("too small :(\n".encode())
    elif client_number > random_number:
        connection.send("too big :(\n".encode())
    else:
        connection.send("perfect!".encode())
        connection.close()
        break

connection.close()
scket.close()
    
    