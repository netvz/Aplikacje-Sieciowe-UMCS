import socket 
import sys 

def TCP_check():
    hostname = sys.argv[1]

    for port in range(1, 65535):
        try:
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_socket.connect((hostname, port))
            print(f"Connected by {port}")
            print(socket.getservbyport(port))
            tcp_socket.close()
        except socket.error:
            pass
TCP_check()