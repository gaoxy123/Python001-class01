# -*- coding:utf8 -*-

import os
import socket


def parse_ip(ip_str):
    ip_from, ip_to = ip_str.split('-')
    ip_0, ip_1, ip_2, ip_from_3 = ip_from.split('.')
    ip_to_3 = ip_to.split('.')[3]
    for i in range(int(ip_from_3), int(ip_to_3)+1):
        yield '.'.join([ip_0, ip_1, ip_2, str(i)])


def check_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(0.1)
        s.connect((ip, port))
        s.shutdown(1)
        print('{}:{} is open'.format(ip, port))
        return True
    except:
        return False
    finally:
        s.close()


def check_ping(ip):
    result = os.popen('ping -c 1 -t 2 %s' % ip).read()
    if 'packet loss' in result:
        return False
    print('can ping:%s' % ip)
    return True
