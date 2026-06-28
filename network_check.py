# Network Check Script
# Learning Git with a real Python file

devices = [
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.3"
]

def check_device(ip):
    print(f"Checking device: {ip}")

for device in devices:
    check_device(device)