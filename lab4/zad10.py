import socket

scket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
scket.bind(('127.0.0.1', 2909))

msg, adress = scket.recvfrom(2048)   
msg = msg.decode()
msg_chopped = msg.split(";")

if(msg != (msg_chopped[0] == "'zad13odp'") and (msg_chopped[1] == "'src'") and (msg_chopped[3] == "'dst'") and (msg_chopped[5] == "'data'")):
    scket.sendto("BAD_SYNTAX".encode(), adress)       

if(msg == "zad13odp;src;2900;dst;35211;data;hello :)"):
    scket.sendto("TAK".encode(), adress)
else:
    scket.sendto("NIE".encode(), adress)
 
scket.close()
    
