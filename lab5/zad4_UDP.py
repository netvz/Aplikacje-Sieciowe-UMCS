import socket

scket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
scket.bind(('127.0.0.1', 2002))

msg, adress = scket.recvfrom(2048)   
scket.sendto(msg, adress)       
scket.close()
    
    