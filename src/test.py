from time import sleep
from rich.console import Console
from rich import print

console = Console()

with console.status("[bold green]Pleas wait...") as status:
    for i in range(3):
        sleep(1)
        console.log(f"tried {i} times")

print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:")
