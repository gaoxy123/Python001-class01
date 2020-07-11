# -*- coding:utf8 -*-

import os
import time
import json
import argparse
from multiprocessing.pool import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool

from utils import check_ping, parse_ip, check_port


class HostScanner(object):

    def __init__(self, args):
        self.f = args.f
        self.file_name = args.w
        self.m = args.m
        self.ip = [ip for ip in parse_ip(args.ip)] if args.f == 'ping' else args.ip
        self.cost_print = args.v

    def run_ping(self, ip):
        res = check_ping(ip)
        return {'ip': ip, 'can_ping': res}

    def run_tcp_port(self, port):
        res = check_port(self.ip, port)
        return {'ip': self.ip, 'port': port, 'is_open': res}


    def run(self):
        begin = int(time.time())
        pool = ProcessPool(args.n) if args.m == 'proc' else ThreadPool(args.n)
        if self.f == 'ping':
            result = pool.map(self.run_ping, self.ip)
        else:
            result = pool.map(self.run_tcp_port, [port for port in range(65535+1)])
        pool.close()
        pool.join()
        end = int(time.time())

        if self.cost_print:
            print('cost time:%s', end-begin)
        # print('result:', result)

        if self.file_name:
            with open(self.file_name, 'w') as f:
                f.write(json.dumps(result))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', type=str, choices=['proc', 'thread'], default='proc',  help='多线程or多进程')
    parser.add_argument('-n', type=int, help='进程或线程数量')
    parser.add_argument('-f', choices=['tcp', 'ping'], default='ping', help='执行方式')
    parser.add_argument('-ip', metavar='ip', required=True, help='ip eg. 192.0.0.1 192.0.0.1-192.0.0.100')
    parser.add_argument('-w', metavar='filename', help='扫描结果保存文件')
    parser.add_argument('-v', action='store_true', help='打印扫描器运行耗时')
    args = parser.parse_args()
    host_scanner = HostScanner(args)
    host_scanner.run()
