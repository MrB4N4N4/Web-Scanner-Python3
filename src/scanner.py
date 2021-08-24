import check
import pyfiglet
import sys
from parser import parser

# pre-check. network, root, ...
if not check.is_root and check.get_localhost:
    exit()

# set parser
args = parser.parse_args()
if len(sys.argv) != 3:
    banner = pyfiglet.figlet_format("Web-Scanner")
    print(banner)
    print("[Guide]\nThis program is a simple scanner for network, ports.\n")
    print(parser.format_help())
    exit()

start_scanning(args)


def start_scanning(arguments):
    arg_net = arguments.scanNetwork
    arg_port = arguments.scanPort
    examine_addr(arg_net)
    examine_addr(arg_port)
    if arg_net:
        bandwidth_scan(arg_net)
    if arg_port:
        service_scan(arg_port)


"""
[Check list]
- root identification Done
- check network Done
- argument parse Done
- scanning process
- console printer(ft.rich) 
"""