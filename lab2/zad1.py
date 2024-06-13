import socket
import struct
import time

sockt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = b'\x1b' + 47 * b'\0'
sockt.sendto(data, ('ntp.task.gda.pl', 123))
received_msg, adrr = sockt.recvfrom(2048)

t = struct.unpack('!12I', received_msg)[10]
t -= 2208988800
print(time.ctime(t))

