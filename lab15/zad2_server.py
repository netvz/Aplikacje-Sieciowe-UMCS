import select, socket, ssl
import queue

def api_connection():
    request_path = f"/data/2.5/weather?lat=51.250559&lon=22.5701022&appid=d4af3e33095b8c43f1a6815954face64"
    request_headers = f"GET {request_path} HTTP/1.1\r\nHost: api.openweathermap.org\r\nConnection: close\r\n\r\n"

    context = ssl.create_default_context()

    with socket.create_connection(("api.openweathermap.org", 443)) as sock:
        with context.wrap_socket(sock, server_hostname="api.openweathermap.org") as ssock:
            ssock.sendall(request_headers.encode())

            response = bytearray()
            while True:
                data = ssock.recv(4096)
                if not data:
                    break
                response.extend(data)
    
    response = response.decode()
    response_body = response.split("\r\n\r\n", 1)[1]
    
    return response_body


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setblocking(0)
server_socket.bind(("localhost", 10001))
server_socket.listen(5)

inputs = [server_socket]
outputs = []

message_queues = {}

while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)

    for s in readable:
        if s is server_socket:
            client_socket, client_address = s.accept()
            client_socket.setblocking(0)
            inputs.append(client_socket)
            message_queues[client_socket] = queue.Queue()

        else:
            data = s.recv(4096)

            if data:
                if data.decode() == "jaka dzis pogoda\r\n":
                    msg = api_connection()
                    message_queues[s].put(msg.encode())
                    
                if s not in outputs:
                    outputs.append(s)
            else:
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]

    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            outputs.remove(s)
        else:
            s.send(next_msg)

    for s in exceptional:
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]


