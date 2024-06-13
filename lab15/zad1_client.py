import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 10000))

try:

    while True:

        msg = input("message: ")
        sock.sendall(msg.encode())

        data = sock.recv(4096).decode()
        print(f"FROM SERVER: {data}")

finally:
    sock.close()