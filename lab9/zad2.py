import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("httpbin.org", 80))
client_socket.send(f"GET /image/png HTTP/1.1\r\nHost: httpbin.org\r\n\r\n".encode())
msg = client_socket.recv(4096)
client_socket.close()
msg = msg.split("\r\n\r\n")[1:][0].strip("")
f = open("oubrazek.png", "w")
f.write(msg)
f.close()

