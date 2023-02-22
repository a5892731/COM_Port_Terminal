'''
this is a generator for creating functions for decoding UDP frames
https://docs.python.org/3/library/struct.html
Format	\	C Type	\	Python type	\	Standard size
c	\	char	\	bytes of length 1	\	1
b	\	signed char	\	integer	\	1
B	\	unsigned char	\	integer	\	1
?	\	_Bool	\	bool	\	1
h	\	short	\	integer	\	2
H	\	unsigned short	\	integer	\	2
i	\	int	\	integer	\	4
I	\	unsigned int	\	integer	\	4
l	\	long	\	integer	\	4
L	\	unsigned long	\	integer	\	4
q	\	long long	\	integer	\	8
Q	\	unsigned long long	\	integer	\	8
e	\	-6	\	float	\	2
f	\	float	\	float	\	4
d	\	double	\	float	\	8
'''

def generator(open_file):
    byte_number = 0
    output = []
    file = open(open_file, "r")

    variable_list = []

    comment = ''
    for comment_line in file:
        comment += "    " + comment_line

    file = open(open_file, "r")

    for line in file:


        if "struct" in line:
            frame_name = line[6::].rstrip("\n")
            output.append("def {}_data_decode(frame):".format(frame_name))
            output.append("    \"\"\"")
            output.append(comment)
            output.append("    \"\"\"")
            output.append("    data = {}")
            output.append("    try: = {}")
            print(frame_name)
        elif "enum Id" in line:
            frame_name = line[9::].rstrip("\n")
            output.append("def {}_data_decode(frame):".format(frame_name))
            output.append("    \"\"\"")
            output.append(comment)
            output.append("    \"\"\"")
            output.append("    data = {}")
            output.append("    try:")
            print(frame_name)
        elif "int32_t" in line:
            variable_name = line[12::].rstrip(" {};\n")
            output.append("        data[\"{}\"] = convert_bytes_to_variable(bytes = frame[\"data\"][{}:{}], data_type = \"{}i\")"
                          .format(variable_name, byte_number, byte_number + 4, endian))
            byte_number += 4
            variable_list.append(variable_name)
            print(variable_name)
        elif "int8_t" in line:
            variable_name = line[11::].rstrip(" {};\n")
            output.append("        data[\"{}\"] = convert_bytes_to_variable(bytes = frame[\"data\"][{}:{}], data_type = \"B\")"
                          .format(variable_name, byte_number, byte_number + 1))
            byte_number += 1
            variable_list.append(variable_name)
            print(variable_name)
        elif "double" in line:
            variable_name = line[11::].rstrip(" {};\n")
            output.append("        data[\"{}\"] = convert_bytes_to_variable(bytes = frame[\"data\"][{}:{}], data_type = \"{}d\")"
                          .format(variable_name, byte_number, byte_number + 8, endian))
            byte_number += 8
            variable_list.append(variable_name)
            print(variable_name)
    output.append("    except TypeError:")
    output.append("        print(\"{}_data_decode(frame): except TypeError: TypeError: unhashable type: 'slice'\")".
                  format(frame_name))
    output.append("        return self.data[\"data\"]")


    output.append("")
    for variable in variable_list:
        output.append("    self.{} = data[\"{}\"]".format(variable, variable))
    output.append("")

    output.append("    return data")





    file = open("outpu_create.txt", "w")


    for line in output:
        print(line, file=file)



if __name__ == "__main__":

    '''frame shape'''
    file1 = "header.txt"
    file2 = "ThrusterFrame.txt"
    file3 = "ThrusterSettings.txt"
    file4 = "LightsSettings.txt"
    file5 = "TurbiditySettings.txt"
    file6 = "DigitalInputsFrame.txt"


    '''start byte number'''
    start_byte_number = 0
    '''endian   < = little ; > = big'''
    endian = "<"


    """run"""
    generator(file6)
    print()
    print(">>> open outpu_create.txt file")