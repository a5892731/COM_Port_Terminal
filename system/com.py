import serial
import io
import unicodedata
from system.read_data_files import DataImport

class SerialComPort:
    def __init__(self, com_number = "COM2", data_file = "PORT_COM.txt"):

        serial_parameters = DataImport(data_file, "dict")

        self.ser = serial.Serial()
        self.ser.baudrate = self.parameter("baudrate", "int", serial_parameters())
        self.ser.port = com_number
        self.ser.bytesize = self.parameter("bytesize", "int", serial_parameters())
        self.ser.parity = self.parameter("parity", "str", serial_parameters())
        self.ser.stopbits = self.parameter("stopbits", "int", serial_parameters())
        self.ser.xonxoff = self.parameter("xonxoff", "bool", serial_parameters())
        self.ser.rtscts = self.parameter("rtscts", "bool", serial_parameters())
        self.ser.write_timeout = self.parameter("dsrdtr", "None", serial_parameters())
        self.ser.dsrdtr = self.parameter("dsrdtr", "bool", serial_parameters())
        self.ser.inter_byte_timeout = self.parameter("dsrdtr", "None", serial_parameters())
        self.ser.timeout = self.parameter("timeout", "float", serial_parameters())
        self.ser.exclusive = self.parameter("dsrdtr", "None", serial_parameters())
        self.ser.open()

        self.sio = io.TextIOWrapper(io.BufferedRWPair(self.ser, self.ser))

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

    def parameter(self, name, type, serial_parameters, data_file = "PORT_COM.txt"):

        if type == "bool":
            if serial_parameters[name] == "False":
                return False
            elif serial_parameters[name] == "True":
                return True
        elif serial_parameters[name] == "int":
            return int(serial_parameters[name])
        elif type == "str":
            return serial_parameters[name]
        elif type == "int":
            return int(serial_parameters[name])
        elif type == "float":
            return float(serial_parameters[name])
        elif type == "None":
            return None
        else:
            return "wrong data"
