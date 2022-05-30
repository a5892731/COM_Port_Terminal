from serial import Serial
from io import TextIOWrapper, BufferedRWPair

from resources.serial_port.system.read_data_files import DataImport


class SerialComPort:

    def read_configuration(self, data_file="PORT_COM.txt"):
        self.serial_parameters = DataImport(data_file, "dict")

    def serial_connection(self, ):
        self.ser = Serial()
        self.ser.baudrate = self.parameter("baudrate", "int", self.serial_parameters())
        self.ser.port = self.parameter("port", "str", self.serial_parameters())
        self.ser.bytesize = self.parameter("bytesize", "int", self.serial_parameters())
        self.ser.parity = self.parameter("parity", "str", self.serial_parameters())
        self.ser.stopbits = self.parameter("stopbits", "int", self.serial_parameters())
        self.ser.xonxoff = self.parameter("xonxoff", "bool", self.serial_parameters())
        self.ser.rtscts = self.parameter("rtscts", "bool", self.serial_parameters())
        self.ser.write_timeout = self.parameter("dsrdtr", "None", self.serial_parameters())
        self.ser.dsrdtr = self.parameter("dsrdtr", "bool", self.serial_parameters())
        self.ser.inter_byte_timeout = self.parameter("dsrdtr", "None", self.serial_parameters())
        self.ser.timeout = self.parameter("timeout", "float", self.serial_parameters())
        self.ser.exclusive = self.parameter("dsrdtr", "None", self.serial_parameters())
        self.ser.open()

        self.sio = TextIOWrapper(BufferedRWPair(self.ser, self.ser))

    def read_data(self):
        if self.ser.in_waiting > 0:
            line = self.sio.readline()
            # if line != "":
            # print(line, end = "\n")
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

    def parameter(self, name, type, serial_parameters):

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

