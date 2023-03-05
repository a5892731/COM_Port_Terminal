from resources.functions.convert_bytes_to_variable import convert_bytes_to_variable

def TestFrameData_data_decode(self, frame):
    """
    enum Id: TestFrameData
    {
        int32_t variable1 {};
        double variable2 {};
        double variable3 {};
        int8_t variable4 {};
        int8_t variable5 {};
    };
    """
    try:
        self.variable1 = convert_bytes_to_variable(bytes = frame["data"][0:4], data_type = "<i")
        self.variable2 = convert_bytes_to_variable(bytes = frame["data"][4:12], data_type = "<d")
        self.variable3 = convert_bytes_to_variable(bytes = frame["data"][12:20], data_type = "<d")
        self.variable4 = convert_bytes_to_variable(bytes = frame["data"][20:21], data_type = "B")
        self.variable5 = convert_bytes_to_variable(bytes = frame["data"][21:22], data_type = "B")
    except TypeError:
        print("TestFrameData_data_decode(frame): except TypeError: TypeError: unhashable type: 'slice'")

