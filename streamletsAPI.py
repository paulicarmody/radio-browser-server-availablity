#!/bin/env python

# !flask/bin/python
from flask import Flask, jsonify

import socket
import random

app = Flask(__name__)

@app.route('/api/v1.0/station', methods=['GET'])
def get_tasks():

    return jsonify( { 'url': get_radiobrowser_base_url_random() } )


def get_radiobrowser_base_urls():
    """
    Get all base urls of all currently available radiobrowser servers

    Returns:
    list: a list of strings

    """
    hosts = []
    # get all hosts from DNS
    ips = socket.getaddrinfo('all.api.radio-browser.info',
                             80, 0, 0, socket.IPPROTO_TCP)
    for ip_tupple in ips:
        ip = ip_tupple[4][0]

        # do a reverse lookup on every one of the ips to have a nice name for it
        host_addr = socket.gethostbyaddr(ip)
        # add the name to a list if not already in there
        if host_addr[0] not in hosts:
            hosts.append(host_addr[0])

    # sort list of names
    hosts.sort()
    # add "https://" in front to make it an url
    return list(map(lambda x: "https://" + x, hosts))


def get_radiobrowser_base_url_random():
    """
    Get a random available base url

    Returns:
    str: a random available base url

    """
    hosts = get_radiobrowser_base_urls()
    return random.choice(hosts)


if __name__ == '__main__':
    app.run()