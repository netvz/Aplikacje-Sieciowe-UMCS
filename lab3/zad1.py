import socket

udp_datagram = "ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 75 6e"
split_datagram = udp_datagram.split(" ")

def hex_to_dec(val):
    return int(val, 16)

source_port_hex = "".join(split_datagram[:2])
source_port = hex_to_dec(source_port_hex)

destination_port_hex = "".join(split_datagram[2:4])
destination_port = hex_to_dec(destination_port_hex)

def hex_to_ascii(val):
    return bytes.fromhex(val).decode('utf-8')

data = hex_to_ascii("".join(split_datagram[8:]))

output = f"zad14odp;src;{source_port};dst;{destination_port};data;{data}"
print(output)

sockt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockt.sendto(output.encode(), ('127.0.0.1', 2910))
received_msg, adrr = sockt.recvfrom(2048)
print(received_msg)
