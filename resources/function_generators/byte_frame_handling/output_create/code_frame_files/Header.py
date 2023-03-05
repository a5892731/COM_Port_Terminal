from resources.functions.convert_variable_to_bytes import convert_variable_to_bytes

def Header_data_code(self, endian="little"):
    """
    struct Header
    {
    private:
        int32_t ID {};
        int8_t DLC {};
        int8_t reserved0 {};
        int8_t reserved1 {};
        int8_t reserved2 {};
    };
    """
    ID = convert_variable_to_bytes(value=self.ID, type ="int32_t", endian=endian)
    DLC = convert_variable_to_bytes(value=self.DLC, type ="unsigned char", endian=endian)
    reserved0 = convert_variable_to_bytes(value=self.reserved0, type ="unsigned char", endian=endian)
    reserved1 = convert_variable_to_bytes(value=self.reserved1, type ="unsigned char", endian=endian)
    reserved2 = convert_variable_to_bytes(value=self.reserved2, type ="unsigned char", endian=endian)


    Header = ID + DLC + reserved0 + reserved1 + reserved2
    return Header
