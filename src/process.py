import pre
import nmap3
from rich import print


# start network/port scan
def start_scanning(arguments):
    if arguments.scanNetwork:
        net_add = pre.check_address(arguments.scanNetwork)
        scan_network(net_add)
    elif arguments.scanPort:
        port_add = pre.check_address(arguments.scanPort)
        scan_service(port_add)
    else:
        print("[-] You should put ip address using ipv4 protocol")
        exit()


def scan_network(address):
    address = address.split(".")[:3]
    address.append("1/24")
    address = ".".join(address)

    nmap = nmap3.NmapScanTechniques()
    result = nmap.nmap_ping_scan(address)
    print(result)


def scan_service(address):
    nmap = nmap3.Nmap()
    print(nmap.nmap_os_detection(address))
