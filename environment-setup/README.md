# Environment & Tools Setup

This project documents all commands and tools installed for my macOS cybersecurity lab.

## Tools Installed
- Homebrew
- Python + pip + virtualenv
- Docker Desktop
- nmap
- john
- sqlmap
- Wireshark
- AWS CLI

## Commands Used
- git add .
- git commit -m "Added full 12-month cybersecurity & cloud roadmap"
- git push
- code ~/cyber_projects/cyber-roadmap-2025
- cd ~/cyber_projects/cyber-roadmap-2025
- mkdir -p environment-setup/docs
- mkdir -p environment-setup/scripts
- touch environment-setup/README.md
- python3 log_monitor.py
- echo -e "Login successful\nLogin failed\nFailed password attempt" > test.log

## Network Mapper Results
- Subnet scanned: 10.x.x.x/20
- Number of devices found: (count from your CSV)
- CSV saved to docs/network_scan.csv

## Hardening Notes
- Avoid exposing unnecessary ports on local devices
- Use strong router admin passwords
- Disable unused services
- Regularly scan your own network for unknown devices