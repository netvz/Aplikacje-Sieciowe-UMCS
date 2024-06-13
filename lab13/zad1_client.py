import socket
import os

def send_file(filename):
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        print("tylko pliki graficzne")
        return

    try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            client_socket.connect(("127.0.0.1", 65432))
            
            upload_command = f"UPLOAD {os.path.basename(filename)}\n"
            client_socket.send(upload_command.encode())
            response = client_socket.recv(8192).decode()
            if not response.startswith("OK"):
                print(response)
                return

            with open(filename, 'r') as file:
                while True:
                    file_data = file.read(8192 - len("DATA ")) 
                    if not file_data:
                        break
                    data_command = f"DATA {file_data.decode()}\n"
                    client_socket.send(data_command.encode())
                    response = client_socket.recv(8192).decode()
                    if not response.startswith("OK"):
                        print(response)
                        return

            end_command = "END\n"
            client_socket.send(end_command.encode())
            response = client_socket.recv(8192).decode()
            if not response.startswith("OK"):
                print(response)

    except socket.error as e:
        print(e)



filename = input("nazwa pliku: ")
if os.path.isfile(filename):
    send_file(filename)
else:
    print("plik nie istnieje")
