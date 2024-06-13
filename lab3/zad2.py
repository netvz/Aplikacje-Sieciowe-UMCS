import socket

tcp_segment = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29"

split_segment = tcp_segment.split(" ")

def hex_to_dec(val):
    return int(val, 16)

source_port_hex = "".join(split_segment[:2])
source_port = hex_to_dec(source_port_hex)

destination_port_hex = "".join(split_segment[2:4])
destination_port = hex_to_dec(destination_port_hex)

def hex_to_ascii(val):
    return bytes.fromhex(val).decode('utf-8')

data = hex_to_ascii("".join(split_segment[32:]))

output = f"zad13odp;src;{source_port};dst;{destination_port};data;{data}"



sockt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockt.sendto(output.encode(), ('127.0.0.1', 2909))
received_msg, adrr = sockt.recvfrom(2048)
print(received_msg)
