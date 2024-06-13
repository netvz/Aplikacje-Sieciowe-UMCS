import socket

sockt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "message".encode()
sockt.sendto(msg, ('127.0.0.1', 2901))
received_msg, adrr = sockt.recvfrom(2048)

print(received_msg)
