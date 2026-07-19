import socket

host = input("Host: ")
port = int(input("Port: "))

sock = socket.socket()
sock.settimeout(2)

sock.connect((host, port))

try:
    banner = sock.recv(1024)
    print(banner.decode(errors="ignore"))
except:
    print("No banner received.")

sock.close()