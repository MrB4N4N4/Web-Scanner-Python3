import pre
import nmap3
from rich import print
from rich.table import Table
from rich.console import Console
from rich.markdown import Markdown

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


def scan_network(address):
    address = address.split(".")[:3]
    address.append("1/24")
    address = ".".join(address)
    nmap = nmap3.NmapScanTechniques()
    with console.status("[bold green]Please wait...") as status:
        console.log(f"start scanning {address} network\n")
        result = nmap.nmap_ping_scan(address)
    console.log("✅scanning network complete\n")
    return result


def scan_service(address):
    nmap = nmap3.Nmap()
    with console.status("[bold green]Please wait...") as status:
        console.log(f"start scanning {address} services\n")
        result = nmap.nmap_version_detection(address)
    console.log("✅scanning services complete\n")
    return result


def show_os_info(address):
    nmap = nmap3.Nmap()
    with console.status("[bold green]Please wait...") as status:
        console.log(f"getting information of [bold]Operating [bold]System\n")
        result = nmap.nmap_os_detection(address)
    console.log("✅getting [bold]OS[/bold] information complete\n")
    return result


def net_to_table(info):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("IP", width=15)
    table.add_column("Vendor", style="bold red")

    hosts = info.keys()
    # Extract information of nmap scan result
    for ip in hosts:
        if ip in ["stats", "runtime"]:
            continue
        try:
            table.add_row(ip,
                          info[ip]["macaddress"]["vendor"])
        except Exception as e:
            pass

    console.print("🔽[bold yellow] Network scan result!")
    console.print(table)


def port_to_table(info):
    """ Port scan result!!
    ip :
    os :
    columns : protocol, port, name, product, version"""
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Protocol")
    table.add_column("Port Number")
    table.add_column("Name")
    table.add_column("Product")
    table.add_column("Version")

    os_info, service_info = info[0], info[1]
    ip = list(os_info.keys())[0]

    os_info = os_info[ip]["osmatch"][0]
    service_info = service_info[ip]["ports"]

    # get os
    print("🔽[bold yellow] Port scan result!")
    print("IP: [bold]", ip)
    print("OS: [white]",
          os_info["name"], "| osfamily: ",
          os_info["osclass"]["osfamily"])
    # port scan proto, port num, name, product, version
    for port in service_info:
        try:
            table.add_row(port["protocol"],
                          port["portid"],
                          port["service"]["name"],
                          port["service"]["product"],
                          port["service"]["version"])
        except Exception as e:
            pass
    console.print(table)
