#!/usr/bin/env python
def tokenize(ip_address):
    tokens = ip_address.split('.')
    return tokens

def binary_rep(tokens, CIDR):
    octet_one = int(tokens[0])
    octet_two = int(tokens[1])
    octet_three = int(tokens[2])
    octet_four = int(tokens[3])
    CIDR = int(CIDR)

    lst1 = []
    lst2 = []
    lst3 = []
    lst4 = []

    while(octet_one):
        if octet_one&1 == 1:
            lst1.append(str(1))
        else:
            lst1.append(str(0))
        octet_one = octet_one >> 1
    str_result = ''.join(reversed(lst1))

    while(octet_two):
        if octet_two&1 == 1:
            lst2.append(str(1))
        else:
            lst2.append(str(0))
        octet_two = octet_two >> 1
    str_result = str_result +''.join(reversed(lst2))

    while(octet_three):
        if octet_three&1 == 1:
            lst3.append(str(1))
        else:
            lst3.append(str(0))
        octet_three = octet_three >> 1
    str_result = str_result +''.join(reversed(lst3))

    while(octet_four):
        if octet_four&1 == 1:
            lst4.append(str(1))
        else:
            lst4.append(str(0))
        octet_four = octet_four >> 1
    str_result = str_result +''.join(reversed(lst4))
    return str_result[:CIDR]

tokens = tokenize(ip_address="192.168.224.100")
print 'NETWORK BITS:',binary_rep(tokens, "24")
