'''
author a5892731
date 2022-12-02
update 2022-03-10


https://docs.python.org/3/library/struct.html
Format	\	C Type	\	Python type	\	Standard size
c	\	char	\	bytes of length 1	\	1       >>>>>>>>>>>>>>>>> char
b	\	signed char	\	integer	\	1               >>>>>>>>>>>>>>>>> int8
B	\	unsigned char	\	integer	\	1           >>>>>>>>>>>>>>>>> int8_t
?	\	_Bool	\	bool	\	1                   >>>>>>>>>>>>>>>>> bool
h	\	short	\	integer	\	2                   >>>>>>>>>>>>>>>>> int16
H	\	unsigned short	\	integer	\	2           >>>>>>>>>>>>>>>>> int16_t
i	\	int	\	integer	\	4                       >>>>>>>>>>>>>>>>> int32
I	\	unsigned int	\	integer	\	4           >>>>>>>>>>>>>>>>> int32_t
l	\	long	\	integer	\	4                   >>>>>>>>>>>>>>>>>
L	\	unsigned long	\	integer	\	4           >>>>>>>>>>>>>>>>>
q	\	long long	\	integer	\	8               >>>>>>>>>>>>>>>>> int64
Q	\	unsigned long long	\	integer	\	8       >>>>>>>>>>>>>>>>> int64_t
e	\	-6	\	float	\	2                       >>>>>>>>>>>>>>>>>
f	\	float	\	float	\	4                   >>>>>>>>>>>>>>>>> float
d	\	double	\	float	\	8                   >>>>>>>>>>>>>>>>> double
'''



from struct import pack

def convert_variable_to_bytes(value=0, type="int32_t", endian="little"):
    def convert_data(value, type=">i"):
        try:
            out = bytearray(pack(type, value))
        except:
            out = bytearray(pack(type, 0))
        return out

    if type == "char":
        struct_type = "c"
    elif type == "bool":
        struct_type = "?"
    elif type == "int8":
        struct_type = "b"
    elif type == "int8_t":
        struct_type = "B"
    elif type == "bool":
        struct_type = "?"
    elif type == "int16":
        struct_type = "h"
    elif type == "int16_t":
        struct_type = "H"
    elif type == "int32":
        struct_type = "i"
    elif type == "int32_t":
        struct_type = "I"
    elif type == "float":
        struct_type = "f"
    elif type == "double":
        struct_type = "d"
    elif type == "int64":
        struct_type = "q"
    elif type == "int64_t":
        struct_type = "Q"
    else:
        print("error: convert to bytes >>> type error")
        return b''

    if endian == "little" and type != "char" and type != "int8_t" and type != "int8":
        struct_endian = "<"
    elif endian == "big" and type != "char" and type != "int8_t" and type != "int8":
        struct_endian = ">"
    else:
        struct_endian = ""

    return convert_data(value, type=struct_endian + struct_type)