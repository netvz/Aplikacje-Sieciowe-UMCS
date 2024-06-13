import socket

sockt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


number1 = input("number: ").encode()
operator = input("operator: ").encode()
number2 = input("number: ").encode()

sockt.sendto(number1, ('127.0.0.1', 2902))
sockt.sendto(operator, ('127.0.0.1', 2902))
sockt.sendto(number2, ('127.0.0.1', 2902))

received_msg, adrr = sockt.recvfrom(2048)

print(received_msg)