from resources.functions.convert_bytes_to_variable import convert_bytes_to_variable

def Header_data_decode(self, frame):
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
    try:
        self.ID = convert_bytes_to_variable(bytes = frame["data"][0:4], data_type = "<i")
        self.DLC = convert_bytes_to_variable(bytes = frame["data"][4:5], data_type = "B")
        self.reserved0 = convert_bytes_to_variable(bytes = frame["data"][5:6], data_type = "B")
        self.reserved1 = convert_bytes_to_variable(bytes = frame["data"][6:7], data_type = "B")
        self.reserved2 = convert_bytes_to_variable(bytes = frame["data"][7:8], data_type = "B")
    except TypeError:
        print("Header_data_decode(frame): except TypeError: TypeError: unhashable type: 'slice'")

