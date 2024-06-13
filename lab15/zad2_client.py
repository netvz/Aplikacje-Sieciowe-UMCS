import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 10001))

try:
    
    sock.sendall("jaka dzis pogoda\r\n".encode())
    data = sock.recv(8192).decode()
    print(f"FROM SERVER: {data}")

finally:
    sock.close()