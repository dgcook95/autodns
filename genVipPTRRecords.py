#!/usr/bin/python3

# Example Usage: genVipPTRRecords.py -v 4 -i 69.164.22.0/24 -p bos
# Currnently only takes /24 ipv4 blocks. Working on allowing larger+smaller CIDRs.

from netaddr import IPNetwork
import optparse
import ipaddress

parser = optparse.OptionParser()

parser.add_option("-v", "--version", dest="ipversion", default="ipv4", type="string", help="specify IP version")
parser.add_option("-i", "--ip block", dest="cidr", type="string", help="Enter CIDR Block")
parser.add_option("-p", "--pop", dest="cdnpop", type="string", help="specify cdn pop")
(options, args) = parser.parse_args()

ipversion = options.ipversion
cidr = options.cidr
cdnpop = options.cdnpop

def returnIPv4Zone(ip):
    ip = ip.split('.')[::-1]
    ip.pop(0)
    return '.'.join(ip) + '.in-addr.arpa.'

def returnIPv4PTR(ip, pop):
    hostname = 'https-'
    record_indicator = ip.split('.')[-1]
    iplist = ip.split('.')
    iplist_len = len(iplist)-1
    for index, octet in enumerate(iplist):
        if index < iplist_len:
            hostname += octet + '-'
        elif index == iplist_len:
            hostname += octet + '.'
    # TLD redacted for privacy reasons
    hostname += pop + '.${TLD}.'
    record = record_indicator + ' 3600 IN PTR ' + hostname
    return record

def returnIPv6Zone(ip):
    if '/' in ip:
        tempip = ip.split("/")[0]
        expanded_v6_addr_list = ipaddress.ip_address(tempip).exploded.split(":")[:3]
    else:
        expanded_v6_addr_list = ipaddress.ip_address(ip).exploded.split(":")[:3]
    templist = [char for octet in expanded_v6_addr_list for char in octet]
    templist.reverse()

    zone = ''

    for bit in templist:
        zone += str(bit) + '.'

    zone += 'ip6.arpa.'
    return zone

def returnIPv6PTR(ip, pop):
    hostname = 'https-'
    iplist = ip.split(':')
    iplist_len = len(iplist)-1
    for index, octet in enumerate(iplist):
        if index < iplist_len:
            hostname += octet + '-'
        elif index == iplist_len:
            hostname += octet + '.'
    # TLD redacted for privacy reasons
    hostname += 'ipv6.' + pop + '.${TLD}.'
    record_indicator = ''
    expanded_v6_addr_list = ipaddress.ip_address(ip).exploded.split(":")[-5:]
    templist = [char for octet in expanded_v6_addr_list for char in octet]
    templist.reverse()
    record_indicator = ''
    for x in templist:
        record_indicator += str(x) + '.'
    record = record_indicator[:-1] + ' 3600 IN PTR ' + hostname
    return record

def main():
    if '4' in ipversion:
        print('\nrDNS Zone is: ' + returnIPv4Zone(cidr) + '\n')
        ip_range = IPNetwork(cidr)
        for address in ip_range:
            print(returnIPv4PTR(str(address), cdnpop))
    elif '6' in ipversion:
        print('\nrDNS Zone is: ' + returnIPv6Zone(cidr) + '\n')
        ip_range = IPNetwork(cidr)
        for address in ip_range:
            print(returnIPv6PTR(str(address), cdnpop))

if __name__=='__main__':
    main()
