import socket
import time

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

start_time = time.time()

sckt.connect(("127.0.0.1", 2009))
sckt.send("vin diesel".encode())
sckt.recv(2048)

end_time = time.time()

print(f"TCP: {end_time-start_time}")

#TCP: 0.0003027915954589844
#musi się łączyć, pakiety są większe bo są sumy kontrolne, potrzebne są potwierdzenia od serwera i klienta 