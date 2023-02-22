'''
author a5892731
date 2022-12-02
update x
'''
from struct import pack

def convert_variable_to_bytes(value=0, type="int32_t", endian="little"):
    def convert_data(value, type=">i"):
        try:
            out = bytearray(pack(type, value))
        except:
            out = bytearray(pack(type, 0))
        return out

    if type == "int32_t" or type == "int32":
        struct_type = "i"
    elif type == "signed char":
        struct_type = "b"
    elif type == "unsigned char" or type == "int8_t":
        struct_type = "B"
    elif type == "double":
        struct_type = "d"
    else:
        print("error: convert to bytes >>> type error")
        return b''

    if endian == "little" and type != "signed char" and type != "unsigned char" and type != "int8_t":
        struct_endian = "<"
    elif endian == "big" and type != "signed char" and type != "unsigned char" and type != "int8_t":
        struct_endian = ">"
    else:
        struct_endian = ""

    return convert_data(value, type=struct_endian + struct_type)