from resources.functions.convert_bytes_to_variable import convert_bytes_to_variable

def TestFrameData2_data_decode(self, frame):
    """
    enum Id: TestFrameData2
    {
        int16_t variable6 {};
        int16 variable7 {};
        int8_t variable8 {};
    };
    """
    try:
        self.variable6 = convert_bytes_to_variable(bytes = frame["data"][0:1], data_type = "B")
        self.variable7 = convert_bytes_to_variable(bytes = frame["data"][2:3], data_type = "B")
        self.variable8 = convert_bytes_to_variable(bytes = frame["data"][4:5], data_type = "B")
    except TypeError:
        print("TestFrameData2_data_decode(frame): except TypeError: TypeError: unhashable type: 'slice'")

