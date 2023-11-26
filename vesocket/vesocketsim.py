#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, socket, time, argparse

class Vesocketsim:

    def __init__(self, host, port):
        self.dict = {'V': '12800', 'VS': '12800', 'VM': '1280', 'DM': '120',
                     'VPV': '3350', 'PPV': '130', 'I': '15000', 'IL': '1500',
                     'LOAD': 'ON', 'T': '25', 'P': '130', 'CE': '13500',
                     'SOC': '876', 'TTG': '45', 'Alarm': 'OFF', 'Relay': 'OFF',
                     'AR': '1', 'H1': '55000', 'H2': '15000', 'H3': '13000',
                     'H4': '230', 'H5': '12', 'H6': '234000', 'H7': '11000',
                     'H8': '14800', 'H9': '7200', 'H10': '45', 'H11': '5',
                     'H12': '0', 'H13': '0', 'H14': '0', 'H15': '11500',
                     'H16': '14800', 'H17': '34', 'H18': '45', 'H19': '456',
                     'H20': '45', 'H21': '300', 'H22': '45', 'H23': '350',
                     'ERR': '0', 'CS': '5', 'BMV': '702', 'FW': '1.19',
                     'PID': '0x204', 'SER#': 'HQ141112345', 'HSDS': '0'}

        self.socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))


    def convert(self, datadict):
        result = list()
        for key in self.dict:
            result.append(ord('\r'))
            result.append(ord('\n'))
            result.extend([ord(i) for i in key])
            result.append(ord('\t'))
            result.extend([ord(i) for i in datadict[key]])
        # checksum
        result.append(ord('\r'))
        result.append(ord('\n'))
        result.extend([ord(i) for i in 'Checksum'])
        result.append(ord('\t'))
        result.append((256 - (sum(result) % 256)) % 256)
        return result 

        
    def send_packet(self):
        packet = self.convert(self.dict)
        self.socket.write(bytes(packet))

        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A simple VE.Direct simulator using socket')
    parser.add_argument('--host', default = 'localhost', help='Socket host')
    parser.add_argument('--port', default = 2323, help='Socket TCP port')
    args = parser.parse_args()
    ve = Vesocketsim(args.host, args.port)
    while True:
        ve.send_packet()
        time.sleep(1)
