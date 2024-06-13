import socket

def part(address, port, path, range_header):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((address, port))
    request = f"GET {path} HTTP/1.1\r\nHost: {address}\r\nRange: {range_header}\r\n\r\n"
    client_socket.send(request.encode())
    response = client_socket.recv(1000000)
    client_socket.close()
    
    header, body = response.split(b"\r\n\r\n", 1)
    return body


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("212.182.24.27", 8080))

request = f"GET /image.jpg HTTP/1.1\r\nHost: httpbin.org\r\nAccept: text/html\r\nIf-Modified-Since: \r\n\r\n"

if():
    pass
else:
    part1 = part("212.182.24.27", 8080, "/image.jpg", "bytes=0-999999")
    part2 = part("212.182.24.27", 8080, "/image.jpg", "bytes=1000000-1999999")
    part3 = part("212.182.24.27", 8080, "/image.jpg", "bytes=2000000-")

img = part1 + part2 + part3

f = open("czesci.jpg", "w")
f.write(img)
f.close()


