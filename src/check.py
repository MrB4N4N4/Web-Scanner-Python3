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
        print("[-]Error: " + str(e))
        res = False
    return res

