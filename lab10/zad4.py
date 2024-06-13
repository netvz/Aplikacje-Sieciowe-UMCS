import socket
import base64
import hashlib

def receive(client_socket):
    data = "".encode()
    try:
        while True:
            part = client_socket.recv(4096)
            if not part:
                break
            data += part
    except socket.timeout:
        pass
    return data

def decode_message(data):
    length = data[1] & 127
    if length == 126:
        masks = data[4:8]
        message_data = data[8:]
    elif length == 127:
        masks = data[10:14]
        message_data = data[14:]
    else:
        masks = data[2:6]
        message_data = data[6:]

    decoded = bytearray()
    for i in range(len(message_data)):
        decoded.append(message_data[i] ^ masks[i % 4])
    return decoded.decode()

def encode_message(message):
    message_bytes = message.encode()
    message_len = len(message_bytes)
    frame = bytearray()

    frame.append(0x81) 

    if message_len <= 125:
        frame.append(message_len)
    elif message_len <= 65535:
        frame.append(126)
        frame += message_len.to_bytes(2, byteorder='big')
    else:
        frame.append(127)
        frame += message_len.to_bytes(8, byteorder='big')

    frame += message_bytes
    return frame

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 10000))
server_socket.listen()

while True:
    client_socket, addr = server_socket.accept()
    request = receive(client_socket).decode()
    headers = request.split('\r\n')
    websocket_key = ""
    for header in headers:
        if "Sec-WebSocket-Key" in header:
            websocket_key = header.split(': ')[1]

    response_key = base64.b64encode(hashlib.sha1((websocket_key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode()).digest()).decode()
    handshake_response = (f"HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: {response_key}\r\n\r\n")
    client_socket.send(handshake_response.encode())

    while True:
        try:
            data = receive(client_socket)
            if not data:
                break
            
            message = decode_message(data)
            print(message)
            
            response = encode_message(message)
            client_socket.send(response)
        except Exception as e:
            print(e)
            break

    client_socket.close()
