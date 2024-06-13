import socket 

sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sockIPv4.connect(('127.0.0.1', 2900))

    for i in range(0,10):
        sockIPv4.send(input("Your message: ").encode())
        print(sockIPv4.recv(2048))
except socket.error:
    print("Connection error")


sockIPv4.close()