#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import argparse

from vesocket import Vesocket

def print_data_callback(packet, converter):
    print(packet)


def parse_args():
    parser = argparse.ArgumentParser(description='Process VE.Direct protocol with telnet socket')

    parser.add_argument('--host', help='Telnet host', default= 'localhost')
    parser.add_argument('--port', help='Telent TCP port', type=int, default= '2323')
    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    
    try:
        ve = Vesocket(args.host, args.port)
    except ConnectionRefusedError:
        print("Cannot connect to Telnet server. Running?")
        return 1

    try:
        print(ve.read_data_loop(print_data_callback, None))
    except KeyboardInterrupt:
        pass
    
    ve.socket.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())


        
    sys.exit(0)
