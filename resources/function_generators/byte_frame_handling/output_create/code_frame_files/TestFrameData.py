from resources.functions.convert_variable_to_bytes import convert_variable_to_bytes

def TestFrameData_data_code(self, endian="little"):
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
    variable1 = convert_variable_to_bytes(value=self.variable1, type ="int32_t", endian=endian)
    variable2 = convert_variable_to_bytes(value=self.variable2, type ="double", endian=endian)
    variable3 = convert_variable_to_bytes(value=self.variable3, type ="double", endian=endian)
    variable4 = convert_variable_to_bytes(value=self.variable4, type ="unsigned char", endian=endian)
    variable5 = convert_variable_to_bytes(value=self.variable5, type ="unsigned char", endian=endian)


    TestFrameData = variable1 + variable2 + variable3 + variable4 + variable5
    return TestFrameData
