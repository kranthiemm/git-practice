# Network Check Script
# Learning Git with a real Python file

devices = [
    "192.168.1.4",
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.3"
]

def check_device(ip):
    print(f"Checking device: {ip}")

for device in devices:
    check_device(device)

import subprocess

def check_reachability(ip):
    result = subprocess.run(
        ["ping", "-n", "1", ip],
        stdout=subprocess.DEVNULL
    )
    if result.returncode == 0:
        print(f"{ip} is REACHABLE ✅")
    else:
        print(f"{ip} is UNREACHABLE ❌")

for device in devices:
    check_reachability(device)