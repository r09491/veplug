#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse, os
#import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from victron_plug import Victron_Socket, Victron_Serial
from victron_converters import FULL_CONVERTER, convert 


def parse_args():
    parser = argparse.ArgumentParser(description='Process VE.Direct protocol with telnet socket')

    parser.add_argument('--host', help='Telnet host', default= None)
    parser.add_argument('--port', help='Telent TCP port', type=int, default= None)
    parser.add_argument('--device', help='Serial device', default= None)
    parser.add_argument('--mqttbroker', help='MQTT broker address', type=str, default='test.mosquitto.org')
    parser.add_argument('--mqttbrokerport', help='MQTT broker port', type=int, default='1883')
    parser.add_argument('--topicprefix', help='MQTT topic prefix', type=str, default='VICTRON_PLUG/')

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
    

    broker = args.mqttbroker
    prefix = args.topicprefix
    converter = dict((k, v) for k,v in FULL_CONVERTER.items() if k != 'SER#')
    def mqtt_send_callback(packet, converter):
        converted = convert(packet, converter)
        msgs = ((prefix+k, v) for k, v in converted.items()) 
        publish.multiple(msgs, hostname=broker)

    try:
        vp.convert_packet_loop(mqtt_send_callback, converter)
    except KeyboardInterrupt:
        pass

    vp.plug.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
