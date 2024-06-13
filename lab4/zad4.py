import socket

scket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
scket.bind(('127.0.0.1', 2002))

num1, adress = scket.recvfrom(2048)
operator, adress = scket.recvfrom(2048)
num2, adress = scket.recvfrom(2048)

msg = ""
operator = operator.decode()
num1 = int(num1.decode())
num2 = int(num2.decode())

if(operator=="+"):
    msg = num1 + num2
elif(operator=="-"):
    msg = num1 - num2
elif(operator=="*"):
    msg = num1 * num2
elif(operator=="/"):
    msg = num1 / num2


scket.sendto(msg.encode(), adress)       
scket.close()
    
    