import pre
import pyfiglet
import sys
import process
import argparse


# pre-pre. network, root, nmap, ...
if not (pre.is_root() and pre.get_localhost() and pre.nmap_exist()):
    exit()

# set argument parser
parser = argparse.ArgumentParser(description="you should choose whether to scan network or port",
                                 usage="scanner.py -sN 127.0.0.1 | scanner -sP 127.0.0.30"
                                       " | scanner.py -O -sP 127.0.0.30")
parser.add_argument("-sN", "--scanNetwork", metavar="",
                    help="scan Network. Put host's bandwidth")
parser.add_argument("-sP", "--scanPort", metavar="",
                    help="scan opened ports of Host. Put host's address")
parser.add_argument("-O", "--OS", action="store_true",
                    help="show info of Operating system. Just add -O at port scan")
args = parser.parse_args()


# examine arguments
cnt = len(sys.argv)
if cnt < 3:
    banner = pyfiglet.figlet_format("Web-Scanner")
    print(banner)
    print("[Guide]\nThis program is a simple scanner for network, ports.\n\'nmap\' is required")
    print(parser.format_help())
    exit()

process.process_scan(args)
