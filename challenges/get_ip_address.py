# Write a function to find the domain name from the 
# IP address. The function will accept an IP address, 
# make a DNS request, and return the domain name that 
# maps to that IP address while using records of PTR 
# DNS. You can import the Python socket library.

import socket

def get_domain_name(ip_address):

    domain_name  = socket.gethostbyaddr(ip_address)

    return domain_name[0]