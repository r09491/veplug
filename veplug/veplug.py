#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import serial
class Veplug():

    def __init__(self):
        self.header1 = ord('\r')
        self.header2 = ord('\n')
        self.hexmarker = ord(':')
        self.delimiter = ord('\t')
        self.key = ''
        self.value = ''
        self.bytes_sum = 0;
        self.state = self.WAIT_HEADER
        self.dict = {}

        self.plug = None
        self.read = None

    
    (HEX, WAIT_HEADER, IN_KEY, IN_VALUE, IN_CHECKSUM) = range(5)

    
    def input(self, byte):
        if byte == self.hexmarker and self.state != self.IN_CHECKSUM:
            self.state = self.HEX
            
        if self.state == self.WAIT_HEADER:
            self.bytes_sum += byte
            if byte == self.header1:
                self.state = self.WAIT_HEADER
            elif byte == self.header2:
                self.state = self.IN_KEY

            return None
        elif self.state == self.IN_KEY:
            self.bytes_sum += byte
            if byte == self.delimiter:
                if (self.key == 'Checksum'):
                    self.state = self.IN_CHECKSUM
                else:
                    self.state = self.IN_VALUE
            else:
                self.key += chr(byte)
            return None
        elif self.state == self.IN_VALUE:
            self.bytes_sum += byte
            if byte == self.header1:
                self.state = self.WAIT_HEADER
                self.dict[self.key] = self.value;
                self.key = '';
                self.value = '';
            else:
                self.value += chr(byte)
            return None
        elif self.state == self.IN_CHECKSUM:
            self.bytes_sum += byte
            self.key = ''
            self.value = ''
            self.state = self.WAIT_HEADER
            if (self.bytes_sum % 256 == 0):
                self.bytes_sum = 0
                return self.dict
            else:
                self.bytes_sum = 0
        elif self.state == self.HEX:
            self.bytes_sum = 0
            if byte == self.header2:
                self.state = self.WAIT_HEADER
        else:
            raise AssertionError()

        
    def read_packet_single(self):
        while True:
            data = self.read(1024)
            for byte in data:
                packet = self.input(byte)
                if (packet != None):
                    return packet
            
        
    def convert_packet_single(self, callbackFunction, converter = None):
        while True:
            data = self.read(1024)
            for byte in data:
                packet = self.input(byte)
                if (packet != None):
                    callbackFunction(packet, converter)
                    return
            

    def convert_packet_loop(self, callbackFunction, converter = None):
        while True:
            data = self.socket.recv(1024)
            for byte in data:
                packet = self.input(byte)
                if (packet != None):
                    callbackFunction(packet, converter)


class Vesocket(Veplug):

    def __init__(self, host, port):
        super().__init__()

        self.plug = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
        self.read = self.plug.recv
        self.plug.connect((host, port))


        
class Veserial(Veplug):

    def __init__(self, device, timeout = 60, baudrate = 19200):
        super().__init__()

        self.plug = serial.Serial(device, baudrate, timeout)
        self.read = self.plug.read

        
