import socket

ip_packet = "45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1 80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01 00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e"
split_packet = ip_packet.split(" ")

ip_proc = split_packet[:20]
tcp_udp = split_packet[20:]

def hex_to_dec(val):
    return int(val, 16)

def hex_to_ascii(val):
    return bytes.fromhex(val).decode('utf-8')

protocol_version = hex_to_dec(ip_proc[0][0])
protocol_type = hex_to_dec(ip_proc[9]) #tcp

source_ip_hex = ip_proc[12:16]
for i in range(len(source_ip_hex)):
    source_ip_hex[i] = str(hex_to_dec(source_ip_hex[i]))
source_ip = ".".join(source_ip_hex)

dest_ip_hex = ip_proc[16:20]
for i in range(len(dest_ip_hex)):
    dest_ip_hex[i] = str(hex_to_dec(dest_ip_hex[i]))
dest_ip = ".".join(dest_ip_hex)

if protocol_type == 6:

    source_port_hex = "".join(tcp_udp[:2])
    source_port = hex_to_dec(source_port_hex)

    destination_port_hex = "".join(tcp_udp[2:4])
    destination_port = hex_to_dec(destination_port_hex)
    data = hex_to_ascii("".join(tcp_udp[32:]))

    outputA = f"zad15odpA;ver;{protocol_version};srcip;{source_ip};dstip;{dest_ip};type;{protocol_type}"
    outputB = f"zad15odpB;srcport;{source_port};dstport;{destination_port};data;{data}"


    sockt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockt.sendto(outputA.encode(), ('127.0.0.1', 2911))
    received_msg, adrr = sockt.recvfrom(2048)
    print(received_msg)

    if received_msg.decode() == "TAK":
        sockt.sendto(outputB.encode(), ('127.0.0.1', 2911))
        received_msg, adrr = sockt.recvfrom(2048)
        print(received_msg)
    

else:

    source_port_hex = "".join(tcp_udp[:2])
    source_port = hex_to_dec(source_port_hex)

    destination_port_hex = "".join(tcp_udp[2:4])
    destination_port = hex_to_dec(destination_port_hex)

    data = hex_to_ascii("".join(tcp_udp[8:]))

    outputA = f"zad15odpA;ver;{protocol_version};srcip;{source_ip};dstip;{dest_ip};type;{protocol_type}"
    outputB = f"zad15odpB;srcport;{source_port};dstport;{destination_port};data;{data}"

    sockt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockt.sendto(outputA.encode(), ('127.0.0.1', 2910))
    received_msg, adrr = sockt.recvfrom(2048)
    print(received_msg)

    if received_msg.decode() == "TAK":
        sockt.sendto(outputB.encode(), ('127.0.0.1', 2911))
        received_msg, adrr = sockt.recvfrom(2048)
        print(received_msg)
    





