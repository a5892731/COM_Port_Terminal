'''
version 1.0
author: a5892731
date: 2021-03-03

------------------------
>>> Sources:
https://pyserial.readthedocs.io/en/latest/pyserial_api.html#serial.STOPBITS_ONE
https://docs.python.org/3/library/io.html#io.TextIOWrapper
------------------------
>>> Libs:
import serial
------------
import io
import os
import time
------------------------
'''

from resources.serial_port.system.com import SerialComPort
import time

#---------------------------------------------------------------<<< MAIN

if __name__ == "__main__":

    com = SerialComPort()

    while True:

        time.sleep(0.001)

        data = com.read_data()
        com.send_data(data)


