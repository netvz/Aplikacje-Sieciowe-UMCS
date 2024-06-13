import socket 
import sys 

def TCP_connect():
    hostname = sys.argv[1]
    port = int(sys.argv[2])

    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.connect((hostname, port))
        print("Connected")
        print(socket.getservbyport(port))
        tcp_socket.close()
        print("Closed")
    except socket.error:
        print("TCP connection unsuccessful")

TCP_connect()