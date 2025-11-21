#!/usr/bin/env python3

# Simple log monitor for failed login attempts
log_file = "test.log"
alert_file = "failed_attempts.log"

with open(log_file, "r") as f:
    lines = f.readlines()

failed_attempts = [line for line in lines if "failed" in line.lower()]

with open(alert_file, "w") as f:
    for line in failed_attempts:
        f.write(line)

print(f"Found {len(failed_attempts)} failed attempts. Details saved in {alert_file}")