import socket
import getmac
from tabulate import tabulate

macs = []

def probe(variant):
    for i in range (0, 255):
        probe_dest = variant + str(i)
        hostname = socket.gethostbyaddr(probe_dest)[0]
        if hostname == probe_dest:
            pass
        else:
            mac_address = getmac.get_mac_address(ip=probe_dest, network_request=True)
            macs.append([probe_dest, 'Default-Gateway' if hostname == '_gateway' else hostname, mac_address if mac_address is not None else 'local-machine'])

probe('192.168.0.')
probe('192.168.1.')

print(tabulate(macs, headers=['Local-ip','Hostname', 'MacID']))
print('\nNo. of connected devices: ' + str(len(macs) - 1))