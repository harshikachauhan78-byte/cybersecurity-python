from collections import Counter

log_file = "server.log"

failed = 0
successful = 0
ips = []
failed_ips = Counter()

with open(log_file, "r") as file:
    for line in file:
        parts = line.strip().split()

        ip = parts[-1]
        ips.append(ip)

        if "failed" in line.lower():
            failed += 1
            failed_ips[ip] += 1
        elif "successful" in line.lower():
            successful += 1

print("=" * 40)
print("LOG ANALYSIS REPORT")
print("=" * 40)

print(f"Total Entries       : {len(ips)}")
print(f"Successful Logins   : {successful}")
print(f"Failed Logins       : {failed}")
print(f"Unique IP Addresses : {len(set(ips))}")

print("\nSuspicious IPs (More than 3 failed attempts):")

found = False
for ip, count in failed_ips.items():
    if count >= 3:
        print(f"{ip} --> {count} failed attempts")
        found = True

if not found:
    print("No suspicious IPs found.")