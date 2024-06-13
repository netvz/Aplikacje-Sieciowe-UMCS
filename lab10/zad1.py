import socket
import base64

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 10000))
client_key = base64.b64encode("1234567890123456".encode()).decode()
client_socket.send(f"GET ws://localhost:10000/ HTTP/1.1\r\nHOST: localhost\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {client_key}\r\nSec-WebSocket-Version: 13\r\n\r\n".encode())
msg = client_socket.recv(10000).decode(errors="ignore")
print(msg)
client_socket.close()

