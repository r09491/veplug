#!/bin/bash -l

# To be called every 1 minute

# PIP install PATH to be added to CRONTAB

# To run in login shells VICTRON_PLUG_STORE_DIR is defined in '.profile'

# This is the serial variant

# CRONTAB example:
#  SHELL=/bin/bash
#  PATH=/home/r09491/.local/bin:/usr/bin:/bin
#
#  * * * * *  victron_plug_latest_serial_cron.sh
#  */15 * * * * victron_plug_watts_cron.sh && victron_plug_watt_hours_cron.sh
#

victron_plug_latest_single.py --device /dev/ttyUSB0 >> $VICTRON_PLUG_STORE_DIR/victron_plug_latest_$(date +\%y\%m\%d).log
