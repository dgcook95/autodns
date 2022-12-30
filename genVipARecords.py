#!/usr/bin/python3

# Example Usage
# getVipARecords.py -v 6 -i 2607:f4e8:b:a200::1/121 -p bos

from netaddr import IPNetwork
import optparse

parser = optparse.OptionParser()

parser.add_option("-v", "--version", dest="ipversion", default="ipv4", type="string", help="specify IP version")
parser.add_option("-i", "--ip block", dest="cidr", type="string", help="Enter CIDR Block")
parser.add_option("-p", "--pop", dest="cdnpop", type="string", help="specify cdn pop")
(options, args) = parser.parse_args()

ipversion = options.ipversion
cidr = options.cidr
cdnpop = options.cdnpop

def getIPv4A(ip, pop):
    record = 'https-'
    iplist = ip.split('.')
    iplist_len = len(iplist)-1
    for index, octet in enumerate(iplist):
        if index < iplist_len:
            record += octet + '-'
        elif index == iplist_len:
            record += octet + '.'
    record += pop + ' 3600 IN A ' + ip
    return record

def getIPv6AAAA(ip, pop):
    record = 'https-'
    iplist = ip.split(':')
    iplist_len = len(iplist)-1
    for index, octet in enumerate(iplist):
        if index < iplist_len:
            record += octet + '-'
        elif index == iplist_len:
            record += octet + '.'
    record += pop + '.ipv6 3600 IN AAAA ' + ip
    return record

def main():
    if '4' in ipversion:
        ip_range = IPNetwork(cidr)
        for address in ip_range:
            print(getIPv4A(str(address), cdnpop))
    elif '6' in ipversion:
        ip_range = IPNetwork(cidr)
        for address in ip_range:
            print(getIPv6AAAA(str(address), cdnpop))

if __name__=='__main__':
    main()