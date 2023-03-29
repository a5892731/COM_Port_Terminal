from resources.functions.convert_variable_to_bytes import convert_variable_to_bytes

def Header_data_code(self, endian="little"):
    """
    struct Header
    {
    private:
        int8_t ID {};
        int8_t DLC {};
    };
    """
    ID = convert_variable_to_bytes(value=self.ID, type ="int8_t", endian=endian)
    DLC = convert_variable_to_bytes(value=self.DLC, type ="int8_t", endian=endian)


    Header = ID + DLC
    return Header
