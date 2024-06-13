import socket

sockt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hostname = 'localhost'.encode()

sockt.sendto(hostname, ('127.0.0.1', 2907))

received_msg, adrr = sockt.recvfrom(2048)

print(received_msg)