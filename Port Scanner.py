import socket

target = input("Enter IP address (example: 127.0.0.1): ")

ports = [21, 22, 23, 25, 53, 80, 110, 143, 443]

print(f"\nScanning {target}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")

    sock.close()

print("\nScan complete.")