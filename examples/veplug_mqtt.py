#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, os
import paho.mqtt.client as mqtt
from veplug import Vesocket


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process VE.Direct protocol with telnet socket')
    parser.add_argument('--host', help='Telnet host', default= 'localhost')
    parser.add_argument('--port', help='Telent TCP port', type=int, default= '2323')
    parser.add_argument('--device', help='Serial device', default= None)
    parser.add_argument('--mqttbroker', help='MQTT broker address', type=str, default='test.mosquitto.org')
    parser.add_argument('--mqttbrokerport', help='MQTT broker port', type=int, default='1883')
    parser.add_argument('--topicprefix', help='MQTT topic prefix', type=str, default='vesocket/')
    args = parser.parse_args()

    if args.host is not None and args.port is not None and args.device is None:
        ve = Vesocket(args.host, args.port)
    elif args.host is None and args.port is None and args.device is not None:
        ve = Veserial(args.device)
    else:
        print("Illegal input combination.")
        sys.exit( 2)

    client = mqtt.Client()
    client.connect(args.mqttbroker, args.mqttbrokerport, 60)
    client.loop_start()

    def mqtt_send_callback(packet):
        for key, value in packet.items():
            if key != 'SER#': # topic cannot contain MQTT wildcards
                client.publish(args.topicprefix + key, value)

    ve.convert_packet_loop(mqtt_send_callback, None)
