import socket
import base64
import random 
import numpy as np

def receive(client_socket):
    data = "".encode()
    try:
        while True:
            part = client_socket.recv(4096)
            if not part:
                break  
            data += part
    except socket.timeout:
        pass
    return data

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(2)
client_socket.connect(("localhost", 10000))
client_key = base64.b64encode("1234567890123456".encode()).decode()
client_socket.send(f"GET ws://localhost:10000/ HTTP/1.1\r\nHOST: localhost\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {client_key}\r\nSec-WebSocket-Version: 13\r\n\r\n".encode())
msg = receive(client_socket).decode(errors="ignore")
print(msg)

mask = random.randbytes(4)
message_bytes = input("tresc wiadomosci: ").encode()
message_len = len(message_bytes)

message = bytes([message_bytes[i] ^ mask[i % len(mask)] for i in range(len(message_bytes))])

frame = bytearray()
frame.append(0x81)
if(message_len <=125):
    frame.append(int('10000000', 2) | message_len)
elif (message_len <= 65535):
    frame.append(int('11111110', 2)) 
    frame.append(message_len.to_bytes(2, 'big'))
else: 
    frame.append(int('11111111', 2))
    frame.append(message_len.to_bytes(8, 'big'))

frame += mask
frame += message
client_socket.send(frame)


msg = receive(client_socket).decode(errors="ignore")
print(msg)

client_socket.close()
