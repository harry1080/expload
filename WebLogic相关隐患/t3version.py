#!/usr/bin/env python
# coding: utf-8

import sys
from urllib.parse import urlparse
import socket

def parseURL(url):
    _ = urlparse(url)

    scheme = _.scheme
    hostname = _.hostname
    port = _.port

    if not port:
        if scheme == 'http':
            port = 80
        elif scheme == 'https':
            port = 443
        else:
            port = 7001

    return hostname, port

def t3conn(hostname, port):
    sock = socket.create_connection((hostname, port), 3)
    headers = b't3 10.3.6\nAS:255\nHL:19\n\n'
    sock.sendall(headers)
    data = sock.recv(1024)
    sock.close()
    return data

hostname, port = parseURL(sys.argv[1])
data = t3conn(hostname, port)
if b'HELO' in data:
    version = data[5:13]
    print(str(version).strip("b'"))