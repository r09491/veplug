This is a Python library for decoding the Victron Energy VE.Direct text protocol used in their range of MPPT solar charge controllers.

This work is heavily based on the [https://github.com/karioja/vedirect] (VEDirect) package. 

The VEDirect package directly reads the stream from the serial port. This library reads data from a (Telnet) server which may in turn get them from a Victron device. This provides scripting option in a termux environment running on a smartphone. Termux must not access the serial ports of the host environment system. However there is an Android app granted the right to read serial streams received via an OTG cable using Telnet.

The only Victron device I have is the smart solar controller MPPT 75/15. Its serial port is connected to the phone via a [https://www.bjoerns-techblog.de/2021/10/victron-smartsolar-laderegler-auslesen-grundlagen] (self-made USB UART connector) and an OTG cable.

This library was tested on my old 'Huaweii P9 light' flashed with 'Lineage OS' and 'Termux' from 'Fdroid' and the [https://play.google.com/store/search?q=usb%20serial%20telnet%20server&c=apps] (USB Serial Terminal Server) installed. In Termux 'python3' with 'pip3' are availanble. Unfortunately the phone cannot be charged with a regular OTG cables connected.

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

The script 'victron_mqtt.py' is only ported but not tested yet.
