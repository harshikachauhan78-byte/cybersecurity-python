import socket

# Get website name from user
website = input("Enter a website (e.g., google.com): ")

try:
    ip = socket.gethostbyname(website)
    print(f"\nWebsite: {website}")
    print(f"IP Address: {ip}")
except socket.gaierror:
    print("Invalid website or unable to find IP address.")