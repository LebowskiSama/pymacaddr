import socket
import getmac
from tabulate import tabulate
import time
import argparse

parser = argparse.ArgumentParser(description='Sniff out machines on local network')
parser.add_argument('-m', '--monitor', help='monitor continuously', action='store_true')
args = parser.parse_args()

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


def print_probe():
    print(tabulate(macs, headers=['Local-ip','Hostname', 'MacID']))
    print('\nNo. of connected devices: ' + str(len(macs) - 1) + '\n')

if args.monitor:
    while True:
        probe('192.168.0.')
        probe('192.168.1.')
        print_probe()
        time.sleep(1)
        macs.clear()
else:
    probe('192.168.0.')
    probe('192.168.1.')
    print_probe()