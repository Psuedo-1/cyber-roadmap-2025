#!/usr/bin/env python3
import csv
import subprocess

# Change this to your local network
subnet = "10.117.128.0/20"

# Run nmap scan
print(f"Scanning subnet {subnet}...")
result = subprocess.run(["nmap", "-sn", subnet], capture_output=True, text=True)
lines = result.stdout.splitlines()

# Save IPs to CSV
with open("../docs/network_scan.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IP / Host"])
    for line in lines:
        if "Nmap scan report for" in line:
            ip = line.split()[-1]
            writer.writerow([ip])

print("Scan complete. Results saved to docs/network_scan.csv")