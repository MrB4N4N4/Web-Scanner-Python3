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
    print("❗You should install nmap first.\n   sudo apt-get install nmap")
    return False


# chek address
def check_address(address, tmp=""):
    if address is None:
        return

    if address in ["localhost", "127.0.0.1"]:
        address = get_localhost()
    try:
        tmp = address.split(".")
        if len(tmp) != 4:
            print("❗You should input four integers with \".\"")
            exit()
        else:
            for e in tmp:
                if int(e) < 0 or int() > 255:
                    print("❗Integers must be 0 ~ 255")
                    exit()
    except AttributeError as e:
        raise e
        print("❗Unable to split address with \".\"")
        exit()
    return address
