import socket

scket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
scket.bind(('127.0.0.1', 2002))

ip_adress, adress = scket.recvfrom(2048)   
hostname = socket.gethostbyaddr(ip_adress)
scket.sendto(hostname, adress)       
scket.close()
    
    