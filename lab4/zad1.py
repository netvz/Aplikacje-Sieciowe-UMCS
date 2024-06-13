import socket
from datetime import datetime

scket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
scket.bind(('127.0.0.1', 2009))
scket.listen()

connection, adress = scket.accept()
msg = connection.recv(2048)   
print(msg)
now = datetime.now()
connection.send(now)       
connection.close()
scket.close()
    
    