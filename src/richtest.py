from rich.console import Console
from rich.syntax import Syntax

my_code = """
# start network/port scan. [-sN], [[-O] -sP]
def process_scan(arguments):
    console = Console()
    if arguments.scanNetwork:
        with console.status("[bold green]Please wait...") as status:
            net_add = pre.check_address(arguments.scanNetwork)
            info = scan_network(net_add)
            console.log(f"[red]ping scanning {net_add}'s network")
        print(info)
    elif arguments.scanPort:
        if arguments.OS:
            show_os_info(arguments.scanPort)
        port_add = pre.check_address(arguments.scanPort)
        scan_service(port_add)
    else:
        print("[!] You should put ip address using ipv4 protocol")
        exit()
"""
syntax = Syntax(my_code, "python", theme="monokai", line_numbers=True)
console = Console()
console.print(syntax)
