from resources.functions.convert_bytes_to_variable import convert_bytes_to_variable

def Header_data_decode(self, frame):
    """
    struct Header
    {
    private:
        int8_t ID {};
        int8_t DLC {};
    };
    """
    try:
        self.ID = convert_bytes_to_variable(bytes = frame["data"][0:1], data_type = "B")
        self.DLC = convert_bytes_to_variable(bytes = frame["data"][1:2], data_type = "B")
    except TypeError:
        print("Header_data_decode(frame): except TypeError: TypeError: unhashable type: 'slice'")

