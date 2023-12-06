#!/bin/bash -l

# To be called every 1 minute

# PIP install PATH to be added to CRONTAB

# To run in login shells VICTRON_PLUG_STORE_DIR is defined in '.profile'

# This is the socket variant

# Under linux it was tested with the 'ser2net'
#  sudo apt update && sudo apt install ser2net
#
#  Change /etc/ser2net to use port '2323'
#   2323:telnet:600:/dev/ttyUSB0:19200 8DATABITS NONE 1STOPBIT
#   2324:telnet:600:/dev/ttyUSB1:19200 8DATABITS NONE 1STOPBIT
#   2325:telnet:600:/dev/ttyUSB2:19200 8DATABITS NONE 1STOPBIT
#   2326:telnet:600:/dev/ttyUSB3:19200 8DATABITS NONE 1STOPBIT
#
#  sudo service ser2net restart
#
# Under Android it was tested with the USB Serial App and Termux:
#   Start the USB Serial App
#   Execute in Termux

# CRONTAB example:
#  SHELL=/bin/bash
#  PATH=/home/r09491/.local/bin:/usr/bin:/bin
#
#  * * * * *  victron_plug_latest_socket_cron.sh
#  */15 * * * * victron_plug_watts_cron.sh && victron_plug_watt_hours_cron.sh
#

victron_plug_latest_single.py --host localhost --port 2323 >> $VICTRON_PLUG_STORE_DIR/victron_plug_latest_$(date +\%y\%m\%d).log
