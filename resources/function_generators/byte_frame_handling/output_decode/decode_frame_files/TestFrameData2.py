from resources.functions.convert_bytes_to_variable import convert_bytes_to_variable

def TestFrameData2_data_decode(self, frame):
    """
    enum Id: TestFrameData2
    {
        int32_t variable6 {};
        double variable7 {};
        int8_t variable8 {};
    };
    """
    try:
        self.variable6 = convert_bytes_to_variable(bytes = frame["data"][0:4], data_type = "<i")
        self.variable7 = convert_bytes_to_variable(bytes = frame["data"][4:12], data_type = "<d")
        self.variable8 = convert_bytes_to_variable(bytes = frame["data"][12:13], data_type = "B")
    except TypeError:
        print("TestFrameData2_data_decode(frame): except TypeError: TypeError: unhashable type: 'slice'")

