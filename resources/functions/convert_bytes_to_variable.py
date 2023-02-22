'''
author a5892731
date 2022-12-01
update x
'''

from struct import unpack


def convert_bytes_to_variable(bytes, data_type=">f"):  # > big endian; f float
    try:
        variable = unpack(data_type, bytes)
    except:
        print("struct.error: variable len = {} data type = {}".format(len(bytes), data_type))
        '''for byte in bytes:
            print(byte)'''
        return None

    return [num for num in variable][0]