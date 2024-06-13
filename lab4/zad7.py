import socket 

#zadanie 2 lab 3 modyfikacja

sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sockIPv4.connect(('127.0.0.1', 2900))
    while True:
        msg = input("podaj wiadomosc do wyslania")
        if(len(msg) <= 20):
            sockIPv4.send()
            print(sockIPv4.recv(2048))
            break
        else:
            print("wiadomosc musi miec maksymalnie 20 znaków")
except socket.error:
    print("Connection error")

sockIPv4.close()

