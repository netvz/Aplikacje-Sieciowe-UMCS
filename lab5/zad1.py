import socket


sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.connect(("127.0.0.1", 2912))

while True:
    number = input("Give a number from 1 to 1000: ")
    sckt.send(str(number).encode())
    server_msg = sckt.recv(2048).decode()
    print(server_msg)
    if server_msg == "perfect!":
        break
       
sckt.close()