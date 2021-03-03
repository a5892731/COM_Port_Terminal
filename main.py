'''
version 1.0



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



from system.com import SerialComPort
import time




#---------------------------------------------------------------<<< MAIN

if __name__ == "__main__":

    com = SerialComPort("COM2")

    while True:

        time.sleep(0.001)

        data = com.read_data()
        com.send_data(data)


