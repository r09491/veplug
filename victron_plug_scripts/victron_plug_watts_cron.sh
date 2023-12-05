#!/bin/bash -l

# To be called every 15 minutes

victron_plug_watt_hours.py < $VICTRON_PLUG_STORE_DIR/victron_plug_latest_$(date +\%y\%m\%d).log >> \
			   $VICTRON_PLUG_STORE_DIR/victron_plug_watts_$(date +\%y\%m\%d).log

