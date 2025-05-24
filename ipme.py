# IPME 2.0
# Made by ChatGPT, to showcase how it can create malicious code without it knowing.

import random
import subprocess
import time
import platform
import sys
from ipaddress import ip_address, IPv4Address

def ping_ip(ip):
    system = platform.system()
    if system in ["Linux", "Darwin"]:
        ping_command = f"ping -c 1 -W 1 {ip}"
    elif system == "Windows":
        ping_command = f"ping -n 1 -w 1000 {ip}"
    else:
        print(f"Unsupported OS: {system}")
        return False

    result = subprocess.run(ping_command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def random_ip():
    return str(IPv4Address(random.randint(0, 2**32 - 1)))

def monitor_ip(ip):
    if not ping_ip(ip):
        print(f"IP {ip} is down!")
    else:
        print(f"IP {ip} is up.")

if __name__ == "__main__":
    try:
        while True:
            ip = random_ip()
            monitor_ip(ip)
            time.sleep(1)  # Adjust the sleep duration as needed

    except KeyboardInterrupt:
        print("\nExiting... Monitoring stopped.")
        sys.exit(0)
