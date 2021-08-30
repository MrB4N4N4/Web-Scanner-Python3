import os
import socket
import sys


def is_root():
    if os.geteuid() != 0:
        print("Are you Root?")
        return False
    return True


def get_localhost():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            res = s.getsockname()[0]
    except Exception as e:
        print(str(e))
        return False
    return res


def nmap_exist():
    if "nmap" in os.popen("dpkg -l | grep nmap").read():
        return True
    print("[!] You should install nmap first.\n   sudo apt-get install nmap")
    return False


# make address separated by dots.
def check_address(address, tmp=""):
    if address in ["localhost", "127.0.0.1"]:
        address = get_localhost()
    try:
        tmp = address.split(".")
        if len(tmp) != 4:
            print("[!] You should put ip address using ipv4 protocol")
            exit()
    except AttributeError as e:
        print("[!] You should put ip address using ipv4 protocol")
        exit()
    return address
