import socket

scket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
scket.bind(('127.0.0.1', 2002))

hostname, adress = scket.recvfrom(2048)   
ip_adress = socket.gethostbyname(hostname)
scket.sendto(ip_adress, adress)       
scket.close()
    
    