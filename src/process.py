import pre
import nmap3
from rich import print
from rich.table import Table
from rich.console import Console
from time import sleep

console = Console()


# start network/port scan. [-sN], [[-O] -sP]
def process_scan(arguments):
    info = []
    net_add = pre.check_address(arguments.scanNetwork)
    if net_add:
        info.append(scan_network(net_add))
    else:
        port_add = pre.check_address(arguments.scanPort)
        if arguments.OS:
            info.append(show_os_info(arguments.scanPort))
        info.append(scan_service(port_add))
    return info


def scan_network(address: str):
    address = address.split(".")[:3]
    address.append("1/24")
    address = ".".join(address)
    nmap = nmap3.NmapScanTechniques()
    with console.status("[bold green]Please wait...") as status:
        console.log(f"start scanning {address} network\n")
        result = nmap.nmap_ping_scan(address)
    console.log("✅scanning network complete\n")
    return result


def scan_service(address: str):
    nmap = nmap3.Nmap()
    with console.status("[bold green]Please wait...") as status:
        console.log(f"start scanning {address} services\n")
        result = nmap.nmap_version_detection(address)
    console.log("✅scanning services complete\n")
    return result


def show_os_info(address: str):
    nmap = nmap3.Nmap()
    with console.status("[bold green]Please wait...") as status:
        console.log(f"getting information of [bold]Operating [bold]System\n")
        result = nmap.nmap_os_detection(address)
    console.log("✅getting [bold]OS[/bold] information complete\n")
    return result


def dic_to_chart(info: dict[str]):
    # get ip address from nmap result
    print(info)
    hosts = info.keys()
    data = dict()
    for ip in hosts:
        print(info[ip])





