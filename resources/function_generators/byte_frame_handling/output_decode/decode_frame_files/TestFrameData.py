from resources.functions.convert_bytes_to_variable import convert_bytes_to_variable

def TestFrameData_data_decode(self, frame):
    """
    enum Id: TestFrameData
    {
        int32_t variable1 {};
        int32 variable2 {};
        float variable3 {};
        int8_t variable4 {};
        int8 variable5 {};
    };
    """
    try:
        self.variable1 = convert_bytes_to_variable(bytes = frame[0:4], data_type = "<I")
        self.variable2 = convert_bytes_to_variable(bytes = frame[4:8], data_type = "<i")
        self.variable3 = convert_bytes_to_variable(bytes = frame[8:12], data_type = "<f")
        self.variable4 = convert_bytes_to_variable(bytes = frame[12:13], data_type = "B")
        self.variable5 = convert_bytes_to_variable(bytes = frame[13:14], data_type = "b")
    except TypeError:
        print("TestFrameData_data_decode(frame): except TypeError: TypeError: unhashable type: 'slice'")

