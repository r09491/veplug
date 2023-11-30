#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """
Outputs a single VEDirect record
"""

import sys
import os

import argparse

from veplug import Vesocket
from veconverters import LATEST_CONVERTER, convert 

def print_keys(packet, converter):
    converted = convert(packet, converter)
    print('\t'.join(converted.keys()))

def print_values(packet, converter):
    converted = convert(packet, converter)
    print('\t'.join(converted.values()))

    
def parse_args():
    parser = argparse.ArgumentParser(description='Process VE.Direct protocol with telnet socket')

    parser.add_argument('--host', help = 'Telnet host',
                        default = 'localhost')
    parser.add_argument('--port', help = 'Telent TCP port',
                        type=int, default = '2323')

    parser.add_argument('--device', help='Serial device', default= None)

    parser.add_argument('--keys', help = 'Keys for output',
                        default = ','.join([k for k in LATEST_CONVERTER.keys() if LATEST_CONVERTER[k] is not None]))

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    
    try:
        if args.host is not None and args.port is not None and args.device is None:
            ve = Vesocket(args.host, args.port)
        elif args.host is None and args.port is None and args.device is not None:
            ve = Veserial(args.device)
        else:
            print("Illegal input combination.")
            return 2

    except ConnectionRefusedError:
        print("Cannot connect to Telnet server. Running?")
        return 1
    
    latest_keys = [key.strip() for key in args.keys.split(',')]
    for key in latest_keys:
        if not key in LATEST_CONVERTER.keys() or LATEST_CONVERTER[key] is None:
            print(f"Illegal key '{key}' provided")
            return 2

    latest_converter = dict([(k, LATEST_CONVERTER[k]) for k in latest_keys])

    try:
        for output in [print_values]:
            ve.convert_packet_single( output, latest_converter)        
    except KeyboardInterrupt:
        pass

    ve.plug.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
