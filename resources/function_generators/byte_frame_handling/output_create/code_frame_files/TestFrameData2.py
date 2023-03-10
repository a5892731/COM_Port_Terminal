from resources.functions.convert_variable_to_bytes import convert_variable_to_bytes

def TestFrameData2_data_code(self, endian="little"):
    """
    enum Id: TestFrameData2
    {
        int16_t variable6 {};
        int16 variable7 {};
        double variable8 {};
    };
    """
    variable6 = convert_variable_to_bytes(value=self.variable6, type ="unsigned char", endian=endian)
    variable7 = convert_variable_to_bytes(value=self.variable7, type ="unsigned char", endian=endian)
    variable8 = convert_variable_to_bytes(value=self.variable8, type ="double", endian=endian)


    TestFrameData2 = variable6 + variable7 + variable8
    return TestFrameData2
