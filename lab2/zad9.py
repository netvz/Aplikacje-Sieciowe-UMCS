import socket

sockt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = '127.0.0.1'.encode()

sockt.sendto(ip, ('127.0.0.1', 2906))

received_msg, adrr = sockt.recvfrom(2048)

print(received_msg)