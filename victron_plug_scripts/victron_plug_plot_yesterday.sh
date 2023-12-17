#!/bin/bash -l

victron_plug_plot.py < $VICTRON_PLUG_STORE_DIR/victron_plug_latest_$(date -d "yesterday" +\%y\%m\%d).log

