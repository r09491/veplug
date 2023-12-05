#!/bin/bash -l

# To be called every 1 minute
victron_plug_latest_single.py --device /dev/ttyUSB0 >> $VICTRON_PLUG_STORE_DIR/victron_plug_latest_$(date +\%y\%m\%d).log
