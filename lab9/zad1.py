import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("httpbin.org", 80))
client_socket.send("GET /html HTTP/1.1 \r\nHOST: httpbin.org \r\n\r\n".encode())
msg = client_socket.recv(10000).decode()
msg = msg.split("\r\n\r\n")[1:][0].strip("")
f = open("file.html", "w")
f.write(msg)
f.close()

client_socket.close()