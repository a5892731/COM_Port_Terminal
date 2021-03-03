import serial
import io
import unicodedata

class SerialComPort:
    def __init__(self, com_number = "COM2"):

        self.ser = serial.Serial()
        self.ser.baudrate = 9600
        self.ser.port = com_number
        self.ser.bytesize = 8
        self.ser.parity = "N"
        self.ser.stopbits = 1
        self.ser.xonxoff = False
        self.ser.rtscts = False
        self.ser.write_timeout = None
        self.ser.dsrdtr = False
        self.ser.inter_byte_timeout = None
        self.ser.timeout = 0.01
        self.ser.exclusive = None
        self.ser.open()

        self.sio = io.TextIOWrapper(io.BufferedRWPair(self.ser, self.ser))

        #self.serialString = ""

    def read_data(self):
        if self.ser.in_waiting > 0:
            line = self.sio.readline()
            #if line != "":
            print(line, end = "\n")

            return line
        else:
            return ""

    def send_data(self, data):

        if data != "":
            self.sio.write(data)
            self.sio.flush()  # it is buffering. required to get the data out *now*



    def is_open(self):
        return self.serialPort.is_open
    def close_port(self):
        self.serialPort.close()
