import socket

scket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
scket.bind(('127.0.0.1', 2911))

msg, adress = scket.recvfrom(2048)   
msg = msg.decode()
msg_chopped = msg.split(";")

if(msg != (msg_chopped[0] == "'zad15odpA'") and (msg_chopped[1] == "'ver'") and (msg_chopped[3] == "'srcip'") and (msg_chopped[5] == "'dstip'") and (msg_chopped[7] == "'type'")):
    scket.sendto("BAD_SYNTAX".encode(), adress)       

if(msg == "zad15odpA;ver;4;srcip;212.182.24.27;dstip;192.168.0.2;type;6"):
    scket.sendto("TAK".encode(), adress)
    msg2, adress = scket.recvfrom(2048)
    msg2 = msg2.decode()
    msg2_chopped = msg2.split(";")

    if(msg2 != (msg2_chopped[0] == "'zad15odpb'") and (msg2_chopped[1] == "'srcport'") and (msg2_chopped[3] == "'dstport'") and (msg2_chopped[5] == "'data'")):
        scket.sendto("BAD_SYNTAX".encode(), adress)

    if(msg2 == "zad15odpB;srcport;2900;dstport;47526;data;network programming is fun"):
        scket.sendto("TAK".encode(), adress)
    else:
        scket.sendto("NIE".encode(), adress)

else:
    scket.sendto("NIE".encode(), adress)
 
scket.close()
    
