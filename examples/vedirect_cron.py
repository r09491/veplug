#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """
Outputs a single VEDirect record
"""

import sys
import os
import argparse

from vesocket import Vesocket
from veserial.veconverters import LATEST_CONVERTER, convert 


def parse_args():
    parser = argparse.ArgumentParser(description='Process VE.Direct protocol with telnet socket')

    parser.add_argument('--host', help = 'Telnet host',
                        default = 'localhost')
    parser.add_argument('--port', help = 'Telent TCP port',
                        type=int, default = '2323')
    parser.add_argument('--keys', help = 'Keys for output',
                        default = ','.join([k for k in LATEST_CONVERTER.keys() if LATEST_CONVERTER[k] is not None]))

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    
    try:
        ve = Vesocket(args.host, args.port)
    except ConnectionRefusedError:
        print("Cannot connect to Telnet server. Running?")
        return 1
    
    keys = [key.strip() for key in args.keys.split(',')]
    for key in keys:
        if not key in LATEST_CONVERTER.keys() or LATEST_CONVERTER[key] is None:
            print(f"Illegal key '{key}' provided")
            return 2

    converter = dict([(k, LATEST_CONVERTER[k]) for k in keys])

    try:
        data = ve.read_data_single()
        result = convert(data, converter)
        print('\t'.join(result.keys()))
        print('\t'.join(result.values()))
    except KeyboardInterrupt:
        pass
    
    ve.socket.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
