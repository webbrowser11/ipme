# IPME 2.0
# Made by ChatGPT, to showcase how it can create malicious code without it knowing.

import random
import subprocess
import ipaddress
import time
import platform
import sys

def ping_ip(ip):
    if platform.system() == "Darwin":
        ping_command = f"ping -c 1 {ip}"
    elif platform.system() == "Windows":
        ping_command = f"ping -n 1 {ip}"
    else:
        print("Unsupported OS.")
        sys.exit(1)

    response = subprocess.run(ping_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return response.returncode == 0

def random_ip():
    return '.'.join(str(random.randint(1, 255)) for _ in range(4))

def is_public_ip(ip):
    try:
        return ipaddress.ip_address(ip).is_global
    except ValueError:
        return False

def get_existing_ip(max_attempts=100):
    for _ in range(max_attempts):
        ip = random_ip()
        if is_public_ip(ip):
            return ip
    return None

if __name__ == "__main__":
    ip = get_existing_ip()
    
    if not ip:
        print("No valid IP found after multiple attempts. Exiting.")
        sys.exit(1)
    else:
        print(f"Valid IP found: {ip}")

        try:
            while True:
                if not ping_ip(ip):
                    print(f"IP {ip} is down!")
                time.sleep(5)

        except KeyboardInterrupt:
            print("\nExiting... Monitoring stopped.")
            sys.exit(0)
