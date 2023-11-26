This is a Python library for decoding the Victron Energy VE.Direct text protocol used in their range of MPPT solar charge controllers.

This work is heavily based on the VEDirect package.

It does not read the stream from the serial port directly as provided by other Python packages (VEDirect). It reads data from the socket of a (Telnet) server which may in turn read the serial data from a Victron device. This was motivated to allow scripting in a termux environment running on an Android smartphone. Termux is not allowed to access the serial ports of the host environment system. However there is an app for Android allowing to read serial streams received via an OTG cable using Telnet.

The only Victron device I have is the smart solar controller MPPT 75/15. Its serial port is connected via a self-made USB UART connector and an OTG cable to the Android phone.

This library was tested on a 'Huaweii P9 light' flashed with 'Lineage OS' with 'Termux' from 'Fdroid' and the USB serial stream app from 'Google Play' installed in Android. In Termux 'python3' with 'pip3' is installed.  Unfortunately this phone cannot be charged with regular OTG cables connected.

To install:
* Clone the project
* Enter the directory 'vesocket'
* pip install .

To test
* Enter the directory 'examples'
* Plug the OTG cable into the phone
  -> Serial USB stream app is started automtically
* ./victron_print.py
  -> Dump output to the screen

The script 'victron_mqqt.py' is only ported but not tested yet.

