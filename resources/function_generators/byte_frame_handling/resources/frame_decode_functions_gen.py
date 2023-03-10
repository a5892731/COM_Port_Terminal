'''
author: a5892731
creation date: 22.02.2023
update date:  01.03.2023

description:
this is a generator of files that contains functions that purpose are decoding data from byte stream,
that was received via udp, com, etc.
generator must be supported by input_frames text file (in folder input_frames)

input_frames text file example:
----------------------------->>>
struct Header
{
private:
    int32_t ID {};
    int8_t DLC {};
    int8_t reserved0 {};
    int8_t reserved1 {};
    int8_t reserved2 {};
};
####### for a header of dataframe
----------------------------
enum Id: TurbidityFrame
{
    int32_t TurbidityGain {};
    double TurbiditySensorVoltage {};
    double TurbiditySensorFTU {};
    int8_t TurbidityGainA {};
    int8_t TurbidityGainB {};
};
####### for a DATA_convert functions (for the various frames depends from its header ID)
-----------------------------<<<

data stream should by construct like: HEADER+DATA


after execution of those script, check output_create files and instructions shown in terminal window.
'''


'''
this is a generator for creating functions for decoding UDP frames
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

import os

def frame_decode_functions_gen(open_file, endian, input_folder = "input_frames", output_folder = "outpu_create"):
    byte_number = 0
    output = []
    file = open(input_folder + "/" + open_file, "r")

    variable_list = []
    data_types = []

    comment = ''
    for comment_line in file:
        comment += "    " + comment_line

    file = open(input_folder + "/" + open_file, "r")

    output.append("from resources.functions.convert_bytes_to_variable import convert_bytes_to_variable")
    output.append("")


    for line in file:
        if "struct" in line:
            frame_name = line[7::].rstrip("\n")
            output.append("def {}_data_decode(self, frame):".format(frame_name))
            output.append("    \"\"\"")
            output.append(comment)
            output.append("    \"\"\"")
            #output.append("    data = {}")
            output.append("    try:")
        elif "enum Id" in line:
            frame_name = line[9::].rstrip("\n")
            output.append("def {}_data_decode(self, frame):".format(frame_name))
            output.append("    \"\"\"")
            output.append(comment)
            output.append("    \"\"\"")
            #output.append("    data = {}")
            output.append("    try:")
        elif "char" in line:
            variable_name = line.rstrip(" {};\n").lstrip("char ")
            output.append(
                "        self.{} = convert_bytes_to_variable(bytes = frame[\"data\"][{}:{}], data_type = \"B\")"
                    .format(variable_name, byte_number, byte_number + 1))
            byte_number += 1
            variable_list.append(variable_name)
            data_types.append("str()")
        elif "int8_t" in line:
            variable_name = line.rstrip(" {};\n").lstrip("int8_t ")
            output.append(
                "        self.{} = convert_bytes_to_variable(bytes = frame[\"data\"][{}:{}], data_type = \"B\")"
                .format(variable_name, byte_number, byte_number + 1))
            byte_number += 1
            variable_list.append(variable_name)
            data_types.append("int()")
        elif "int8" in line:
            #variable_name = line[9::].rstrip(" {};\n")
            variable_name = line.rstrip(" {};\n").lstrip("int8 ")
            output.append(
                "        self.{} = convert_bytes_to_variable(bytes = frame[\"data\"][{}:{}], data_type = \"B\")"
                    .format(variable_name, byte_number, byte_number + 1))
            byte_number += 1
            variable_list.append(variable_name)
            data_types.append("int()")
        elif "int16_t" in line:
            variable_name = line.rstrip(" {};\n").lstrip("int16_t ")
            output.append(
                "        self.{} = convert_bytes_to_variable(bytes = frame[\"data\"][{}:{}], data_type = \"B\")"
                    .format(variable_name, byte_number, byte_number + 1))
            byte_number += 2
            variable_list.append(variable_name)
            data_types.append("int()")
        elif "int16" in line:
            variable_name = line.rstrip(" {};\n").lstrip("int16 ")
            output.append(
                "        self.{} = convert_bytes_to_variable(bytes = frame[\"data\"][{}:{}], data_type = \"B\")"
                    .format(variable_name, byte_number, byte_number + 1))
            byte_number += 2
            variable_list.append(variable_name)
            data_types.append("int()")
        elif "int32_t" in line:
            variable_name = line.rstrip(" {};\n").lstrip("int32_t ")
            output.append(
                "        self.{} = convert_bytes_to_variable(bytes = frame[\"data\"][{}:{}], data_type = \"{}i\")"
                .format(variable_name, byte_number, byte_number + 4, endian_translate(endian)))
            byte_number += 4
            variable_list.append(variable_name)
            data_types.append("int()")
        elif "int32" in line:
            variable_name = line.rstrip(" {};\n").lstrip("int32 ")
            output.append(
                "        self.{} = convert_bytes_to_variable(bytes = frame[\"data\"][{}:{}], data_type = \"B\")"
                    .format(variable_name, byte_number, byte_number + 1))
            byte_number += 4
            variable_list.append(variable_name)
            data_types.append("int()")
        elif "float" in line:
            variable_name = line.rstrip(" {};\n").lstrip("float ")
            output.append(
                "        self.{} = convert_bytes_to_variable(bytes = frame[\"data\"][{}:{}], data_type = \"{}d\")"
                    .format(variable_name, byte_number, byte_number + 8, endian_translate(endian)))
            byte_number += 4
            variable_list.append(variable_name)
            data_types.append("float()")
        elif "double" in line:
            variable_name = line.rstrip(" {};\n").lstrip("double ")
            output.append(
                "        self.{} = convert_bytes_to_variable(bytes = frame[\"data\"][{}:{}], data_type = \"{}d\")"
                .format(variable_name, byte_number, byte_number + 8, endian_translate(endian)))
            byte_number += 8
            variable_list.append(variable_name)
            data_types.append("float()")
        elif "int64_t" in line:
            variable_name = line.rstrip(" {};\n").lstrip("int64_t ")
            output.append(
                "        self.{} = convert_bytes_to_variable(bytes = frame[\"data\"][{}:{}], data_type = \"B\")"
                    .format(variable_name, byte_number, byte_number + 1))
            byte_number += 8
            variable_list.append(variable_name)
            data_types.append("int()")
        elif "int64" in line:
            variable_name = line.rstrip(" {};\n").lstrip("int64 ")
            output.append(
                "        self.{} = convert_bytes_to_variable(bytes = frame[\"data\"][{}:{}], data_type = \"B\")"
                    .format(variable_name, byte_number, byte_number + 1))
            byte_number += 8
            variable_list.append(variable_name)
            data_types.append("int()")


    output.append("    except TypeError:")
    output.append("        print(\"{}_data_decode(frame): except TypeError: TypeError: unhashable type: 'slice'\")".
                  format(frame_name))

    output.append("")

    file = open("{}/{}.py".format(output_folder, frame_name), "w")


    for line in output:
        print(line, file=file)

    return frame_name, variable_list, data_types, byte_number



def find_input_files(adress="input_frames"):
    os.chdir(adress)
    for root, dirs, files in os.walk('..', topdown=False, onerror=None, followlinks=True):
        pass
    os.chdir("../..")
    return files

def endian_translate(endian):
    if endian == "little":
        return "<"
    elif endian == "big":
        return ">"
    else:
        return endian

if __name__ == "__main__":

    os.chdir("..")
    input_data_address = "input_frames"

    '''start byte number'''
    start_byte_number = 0
    '''endian   < = little ; > = big'''
    endian = "<"




    """run"""

    files_list = find_input_files(adress=input_data_address)
    print("input_frames files: " + str(files_list))

    for file in files_list:
        frame_decode_functions_gen(open_file=(file), endian=endian, input_folder = input_data_address, output_folder = "output_decode")

