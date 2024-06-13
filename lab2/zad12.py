import socket 

sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
message = input("input your message: ")
try:
    sockIPv4.connect(('127.0.0.1', 2908))

    if len(message) < 20:
        message = message.ljust(20)
    else:
        message = message[:20]
    

    total_sent = 0
    while total_sent < len(message):
        sent = sockIPv4.send(message[total_sent:].encode())
        total_sent += sent

    received_message = b''
    while len(received_message) < 20:
        chunk = sockIPv4.recv(20 - len(received_message))
        received_message += chunk

    print(received_message)
except socket.error:
    print("Connection error")

sockIPv4.close()