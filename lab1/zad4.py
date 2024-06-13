import socket

user_ip = input("IP: ")


def hostname_function(ip):
    try:
        return socket.gethostbyaddr(user_ip)[0]
    except socket.herror:
        return "No hostname found"
    
hostname = hostname_function(user_ip)

print(hostname)
