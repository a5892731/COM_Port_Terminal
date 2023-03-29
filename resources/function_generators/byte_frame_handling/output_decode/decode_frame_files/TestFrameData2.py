from resources.functions.convert_bytes_to_variable import convert_bytes_to_variable

def TestFrameData2_data_decode(self, frame):
    """
    enum Id: TestFrameData2
    {
        int16_t variable6 {};
        int16 variable7 {};
        double variable8 {};
    };
    """
    try:
        self.variable6 = convert_bytes_to_variable(bytes = frame["data"][0:2], data_type = "<H")
        self.variable7 = convert_bytes_to_variable(bytes = frame["data"][2:4], data_type = "<h")
        self.variable8 = convert_bytes_to_variable(bytes = frame["data"][4:12], data_type = "<d")
    except TypeError:
        print("TestFrameData2_data_decode(frame): except TypeError: TypeError: unhashable type: 'slice'")

