import nmap3
import check

localhost = check.get_localhost()
if not localhost:
    exit()

nmap = nmap3.Nmap()
"""
[Check list]

- root identification
- check network
- console printer(ft.rich)
- argument parse

"""