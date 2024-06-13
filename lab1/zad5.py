import socket 

def ip_by_name(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return "Provide valid hostname"

name = input("Enter domain name: ")
print(ip_by_name(name))