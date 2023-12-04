#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import argparse

from victron_plug import Victron_Socket, Victron_Serial

def print_data_callback(packet, converter):
    print(packet)


def parse_args():
    parser = argparse.ArgumentParser(description='Process VE.Direct protocol with telnet socket')

    parser.add_argument('--host', help = 'Telnet host', default = None)
    parser.add_argument('--port', help = 'Telnet TCP port', type=int, default = None)
    parser.add_argument('--device', help = 'Serial device', default = None)
    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    
    try:
        if args.host is not None and args.port is not None and args.device is None:
            vp = Victron_Socket(args.host, args.port)
        elif args.host is None and args.port is None and args.device is not None:
            vp = Victron_Serial(args.device)
        else:
            print("Illegal input combination.")
            return 2
        
    except ConnectionRefusedError:
        print("Cannot connect to Telnet server. Running?")
        return 1

    try:
        print(vp.read_packet_single())
    except KeyboardInterrupt:
        pass
    
    vp.plug.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())


        
    sys.exit(0)
