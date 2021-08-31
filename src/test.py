info = {
    '172.30.1.6': {
        'osmatch': {},
        'ports': [],
        'hostname': [],
        'macaddress': {'addr': '00:0C:29:CD:81:55', 'addrtype': 'mac', 'vendor': 'VMware'},
        'state': {'state': 'up', 'reason': 'arp-response', 'reason_ttl': '0'}
    },
    '172.30.1.22': {
        'osmatch': {},
        'ports': [],
        'hostname': [],
        'macaddress': {'addr': '00:D8:61:16:5A:38', 'addrtype': 'mac', 'vendor': 'Micro-star Intl'},
        'state': {'state': 'up', 'reason': 'arp-response', 'reason_ttl': '0'}
    },
    '172.30.1.30': {
        'osmatch': {},
        'ports': [],
        'hostname': [],
        'macaddress': None,
        'state': {'state': 'up', 'reason': 'localhost-response', 'reason_ttl': '0'}
    },
    'stats': {
        'scanner': 'nmap',
        'args': '/usr/bin/nmap -oX - -sP 172.30.1.1/24',
        'start': '1630398488',
        'startstr': 'Tue Aug 31 04:28:08 2021',
        'version': '7.91',
        'xmloutputversion': '1.05'
    },
    'runtime': {
        'time': '1630398493',
        'timestr': 'Tue Aug 31 04:28:13 2021',
        'summary': 'Nmap done at Tue Aug 31 04:28:13 2021; 256 IP addresses (3 hosts up) scanned in 5.17 seconds',
        'elapsed': '5.17',
        'exit': 'success'
    }
}
ip = "172.30.1.6"
print(info[ip]["macaddress"]["vendor"])
