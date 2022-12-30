#!/usr/bin/python3

# Example usage: cidrCalc.py -i 2607:f4e8:b:a200::1/121

from netaddr import IPNetwork
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--ip block", dest="cidr", type="string", help="Enter CIDR Block")
(options, args) = parser.parse_args()

cidr = options.cidr

def returnTotalAddresses(ip):
    return len(ip)

def returnStartAndEnd(ip):
    total = [addr for addr in ip]
    start_and_end = [ total[0], total[-1] ]
    return start_and_end

def main():
    ip_range = IPNetwork(cidr)
    templist = returnStartAndEnd(ip_range)
    first_ip_in_range = templist[0]
    last_ip_in_range = templist[1]

    if ':' in cidr:
        ip_version = 'IPv6'
    else:
        ip_version = 'IPv4'
    
    print('\nTotal ' + ip_version + ' addresses in range: ' + str(returnTotalAddresses(ip_range)) + '\n')
    print('First IP: ' + str(first_ip_in_range))
    print('Last IP: ' + str(last_ip_in_range) + '\n')

    user_answer = input('Display all IP addresses? [Y/y|N/n]: ')

    if 'y' or 'Y' in user_answer:
        print('\n')
        for address in ip_range:
            print(address)
    elif 'n' or 'N' in user_answer:
        print('\n')
        exit

if __name__=='__main__':
    main()