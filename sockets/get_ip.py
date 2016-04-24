# -*- coding: utf-8 -*-
# @Author: prabhakar
# @Date:   2016-04-24 23:46:45
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-04-24 23:50:04
#Socket client example in python
 
import socket   #for sockets
import sys  #for exit
 
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print 'Socket Created'
 
host = 'csinsit.org'
 
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip
