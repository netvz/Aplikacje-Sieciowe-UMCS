import socket 

sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
message = input("input your message: ")
try:
    sockIPv4.connect(('127.0.0.1', 2908))

    if len(message) < 20:
        message = message.ljust(20)
    else:
        message = message[:20]
    
    sockIPv4.send(message.encode())

    print(sockIPv4.recv(2048))
except socket.error:
    print("Connection error")

sockIPv4.close()