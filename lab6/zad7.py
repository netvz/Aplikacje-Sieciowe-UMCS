import socket
import base64

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.connect(("dsmka.wintertoad.xyz", 587))
server_output = sckt.recv(2048)

def send_and_try(input, expected_output):
    sckt.send(f"{input}\r\n".encode())
    server_output = sckt.recv(2048)
    if (server_output.decode() != f"{expected_output}\r\n"):
        exit()

if (server_output.decode() != "220 dsmka.wintertoad.xyz ESMTP\r\n"):
    exit()

login = input("Login: ")
login_bytes = login.encode('ascii')
base64_login_bytes = base64.b64encode(login_bytes)
base64_login = base64_login_bytes.decode('ascii')

password = input("Haslo: ")
password_bytes = password.encode('ascii')
base64_password_bytes = base64.b64encode(password_bytes)
base64_password = base64_password_bytes.decode('ascii')

sender = input("Nadawca: ")
receiver = input("Odbiorca: ")
subj = input("Temat wiadomości: ")
msg = input("Wiadomość: ")

send_and_try("EHLO fedora", "250-dsmka.wintertoad.xyz\r\n250-PIPELINING\r\n250-SIZE 10240000\r\n250-ETRN\r\n250-AUTH PLAIN LOGIN\r\n250-AUTH=PLAIN LOGIN\r\n250-ENHANCEDSTATUSCODES\r\n250-8BITMIME\r\n250-DSN\r\n250 CHUNKING")
send_and_try("AUTH LOGIN", "334 VXNlcm5hbWU6")
send_and_try(base64_login, "334 UGFzc3dvcmQ6")
send_and_try(base64_password, "235 2.7.0 Authentication successful")
send_and_try(f"MAIL FROM: < {sender} >", "250 2.1.0 Ok")
send_and_try(f"RCPT TO: < {receiver}>", "250 2.1.5 Ok")
send_and_try("DATA", "354 End data with <CR><LF>.<CR><LF>")

sckt.send(f"To: <{receiver}>\r\n".encode())
sckt.send(f"From: <{sender}>\r\n".encode())
sckt.send(f"Subject: {subj}\r\n".encode())
sckt.send(f"Content-Type: multipart/mixed; boundary=sep\r\n--sep\r\n{msg}\r\n--sep\r\nContent-Type: text/plain; name=\"plik_tekstowy.txt\"\r\nContent-Disposition: attachment; filename=\"plik_tekstowy.txt\"\r\nContent-Transfer-Encoding: base64\r\nemFrb2Rvd2FuYSB3aWFkb21vc2MgcGxpa3UgCg==\r\n--sep--\r\n".encode())
sckt.send(".\r\n".encode())
server_output = sckt.recv(2048)
if (not server_output.decode().startswith("250")):
    exit()

send_and_try("QUIT", "221 2.0.0 Bye")
