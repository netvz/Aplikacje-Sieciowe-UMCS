import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("212.182.24.27", 2904))
client_socket.send("LIST_FILES\r\n".encode())
msg = client_socket.recv(4096).decode()
print("pliki:\n", msg)

filename = "image.png"  

client_socket.send(f"GET_IMAGE {filename}\r\n".encode())

response_header = client_socket.recv(1024).decode()

if response_header.startswith("SIZE"):
    parts = response_header.split()
    size = int(parts[1])
    received_filename = parts[3]

    f = open(filename, 'w')
    remaining = size
    while remaining > 0:
        data = client_socket.recv(min(1024, remaining))
        if not data:
            break
        f.write(data)
        remaining -= len(data)
        
    print(f"zapisano jako: {filename}")
else:
    print("błąd serwera")

client_socket.close()
