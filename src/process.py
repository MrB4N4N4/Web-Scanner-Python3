import pre
import nmap3
from rich import print
from rich.console import Console
from time import sleep

console = Console()


# start network/port scan. [-sN], [[-O] -sP]
def process_scan(arguments):
    info = []
    if arguments.scanNetwork:
        net_add = pre.check_address(arguments.scanNetwork)
        info.append(scan_network(net_add))

    elif arguments.scanPort:
        if arguments.OS:
            info.append(show_os_info(arguments.scanPort))
        port_add = pre.check_address(arguments.scanPort)
        info.append(scan_service(port_add))
    else:
        print("[!] You should put ip address using ipv4 protocol")
        exit()


def scan_network(address: str):
    address = address.split(".")[:3]
    address.append("1/24")
    address = ".".join(address)
    nmap = nmap3.NmapScanTechniques()
    with console.status("[bold green]Please wait...") as status:
        console.log(f"start scanning {address} network")
        result = nmap.nmap_ping_scan(address)
    console.log("complete")
    return result


def scan_service(address: str):
    nmap = nmap3.Nmap()
    with console.status("[bold green]Please wait...") as status:
        console.log(f"start scanning {address} services")
        result = nmap.nmap_version_detection(address)
    console.log("complete scanning services")
    return result


def show_os_info(address: str):
    nmap = nmap3.Nmap()
    with console.status("[bold green]Plese wait...") as status:
        console.log(f"getting information of [bold]Operating [bold]System")
        result = nmap.nmap_os_detection(address)
    console.log("complete getting OS information")
    return result
