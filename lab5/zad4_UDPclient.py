import socket
import time 

sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

start_time = time.time()

sckt.sendto("vin diesel".encode(), ("127.0.0.1", 2002))
sckt.recv(2048)

end_time = time.time()

print(f"UDP: {end_time-start_time}")

#UDP: 0.00021767616271972656
#czemu niższy czas: nie musi się łączyć i pakiety są mniejsze 