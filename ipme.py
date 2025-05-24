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

def get_working_ips(max_attempts=1000, max_working_ips=10):
    working_ips = []
    attempts = 0
    while len(working_ips) < max_working_ips and attempts < max_attempts:
        ip = random_ip()
        if ping_ip(ip):
            working_ips.append(ip)
        attempts += 1
    return working_ips

if __name__ == "__main__":
    working_ips = get_working_ips()

    if not working_ips:
        print("No responsive IPs found after multiple attempts. Exiting.")
        sys.exit(1)
    else:
        print(f"Responsive IPs found: {working_ips}")

        try:
            while True:
                for ip in working_ips:
                    if not ping_ip(ip):
                        print(f"IP {ip} is down!")
                    else:
                        print(f"IP {ip} is up.")
                time.sleep(5)

        except KeyboardInterrupt:
            print("\nExiting... Monitoring stopped.")
            sys.exit(0)
