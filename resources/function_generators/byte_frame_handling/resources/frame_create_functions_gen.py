'''
author: a5892731
creation date: 22.02.2023
update date:  01.03.2023

description:
this is a generator of files that contains functions that purpose are coding data to byte stream,
that can be sent via udp, com, etc.
generator mus be supported by input_frames text file (in folder input_frames)

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


def frame_create_functions_gen(open_file, endian, input_folder = "input_frames", output_folder = "output_create"):
    byte_number = 0
    output = []
    variable_list = []
    data_types = []
    return_value = []

    file = open("{}/{}".format(input_folder, open_file), "r")

    comment = ''
    for comment_line in file:
        comment += "    " + comment_line

    file = open("{}/{}".format(input_folder, open_file), "r")

    output.append("from resources.functions.convert_variable_to_bytes import convert_variable_to_bytes")
    output.append("")


    for line in file:
        if "struct" in line:
            frame_name = line[7::].rstrip("\n")
            output.append("def {}_data_code(self, endian=\"{}\"):".format(frame_name, endian))
            output.append("    \"\"\"")
            output.append(comment)
            output.append("    \"\"\"")
        elif "enum Id" in line:
            frame_name = line[9::].rstrip("\n")
            output.append("def {}_data_code(self, endian=\"{}\"):".format(frame_name, endian))
            output.append("    \"\"\"")
            output.append(comment)
            output.append("    \"\"\"")

        elif "char" in line:
            variable_name = line.rstrip(" {};\n").lstrip("char ")
            data_types.append("str()")
            variable_list.append(variable_name)
            output.append("    {0} = convert_variable_to_bytes(value=self.{0}, type =\"unsigned char\", endian=endian)".
                          format(variable_name, ))
            return_value.append(variable_name)
        elif "int8_t" in line:
            variable_name = line.rstrip(" {};\n").lstrip("int8_t ")
            data_types.append("int()")
            variable_list.append(variable_name)
            output.append("    {0} = convert_variable_to_bytes(value=self.{0}, type =\"unsigned char\", endian=endian)".
                          format(variable_name, ))
            return_value.append(variable_name)
        elif "int8" in line:
            variable_name = line.rstrip(" {};\n").lstrip("int8 ")
            data_types.append("int()")
            variable_list.append(variable_name)
            output.append("    {0} = convert_variable_to_bytes(value=self.{0}, type =\"unsigned char\", endian=endian)".
                          format(variable_name, ))
            return_value.append(variable_name)
        elif "int16_t" in line:
            variable_name = line.rstrip(" {};\n").lstrip("int16_t ")
            data_types.append("int()")
            variable_list.append(variable_name)
            output.append("    {0} = convert_variable_to_bytes(value=self.{0}, type =\"unsigned char\", endian=endian)".
                          format(variable_name, ))
            return_value.append(variable_name)
        elif "int16" in line:
            variable_name = line.rstrip(" {};\n")
            variable_name = variable_name.lstrip("int16 ")
            data_types.append("int()")
            variable_list.append(variable_name)
            output.append("    {0} = convert_variable_to_bytes(value=self.{0}, type =\"unsigned char\", endian=endian)".
                          format(variable_name, ))
            return_value.append(variable_name)
        elif "int32_t" in line:
            variable_name = line.rstrip(" {};\n").lstrip("int32_t ")
            variable_list.append(variable_name)
            data_types.append("int()")
            output.append("    {0} = convert_variable_to_bytes(value=self.{0}, type =\"int32_t\", endian=endian)".
                          format(variable_name, ))
            return_value.append(variable_name)
        elif "int32" in line:
            variable_name = line.rstrip(" {};\n").lstrip("int32 ")
            data_types.append("int()")
            variable_list.append(variable_name)
            output.append("    {0} = convert_variable_to_bytes(value=self.{0}, type =\"unsigned char\", endian=endian)".
                          format(variable_name, ))
            return_value.append(variable_name)
        elif "float" in line:
            variable_name = line.rstrip(" {};\n").lstrip("float ")
            data_types.append("float()")
            variable_list.append(variable_name)
            output.append("    {0} = convert_variable_to_bytes(value=self.{0}, type =\"double\", endian=endian)".
                          format(variable_name, ))
            return_value.append(variable_name)
        elif "double" in line:
            variable_name = line.rstrip(" {};\n").lstrip("double ")
            data_types.append("float()")
            variable_list.append(variable_name)
            output.append("    {0} = convert_variable_to_bytes(value=self.{0}, type =\"double\", endian=endian)".
                          format(variable_name, ))
            return_value.append(variable_name)
        elif "int64_t" in line:
            variable_name = line.rstrip(" {};\n").lstrip("int64_t ")
            variable_list.append(variable_name)
            data_types.append("int()")
            output.append("    {0} = convert_variable_to_bytes(value=self.{0}, type =\"int32_t\", endian=endian)".
                          format(variable_name, ))
            return_value.append(variable_name)
        elif "int64" in line:
            variable_name = line.rstrip(" {};\n").lstrip("int64 ")
            variable_list.append(variable_name)
            data_types.append("int()")
            output.append("    {0} = convert_variable_to_bytes(value=self.{0}, type =\"int32_t\", endian=endian)".
                          format(variable_name, ))
            return_value.append(variable_name)


    output.append("")



    #output.append("    self.last_frame = [self.FRAMES_ID[\"{0}\"], self.FRAMES_DLC[\"{0}\"],".format(frame_name))
    #for value in  return_value:
    #    output.append("                 self.{},".format(value))
    #output.append("                 ]")



    output.append("")
    return_value_str=""
    for value in return_value:
        return_value_str += value + " + "

    return_value = frame_name + " = " + return_value_str.rstrip(" + ")

    output.append("    " + return_value)
    output.append("    " + "return " + frame_name)

    file_name = "{}/{}.py".format(output_folder, frame_name)

    file = open(file_name, "w")

    for line in output:
        print(line, file=file)


    return frame_name, variable_list, data_types, None


def find_input_files(adress="input_frames"):
    os.chdir(adress)
    for root, dirs, files in os.walk('..', topdown=False, onerror=None, followlinks=True):
        pass
    os.chdir("../..")
    return files


#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    os.chdir("..")
    input_data_address = "input_frames"

    '''start byte number'''
    start_byte_number = 0
    '''endian   < = little ; > = big'''
    endian = "little"

    """run"""

    files_list = find_input_files(adress=input_data_address)
    print("input_frames files: " + str(files_list))

    for file in files_list:
        frame_create_functions_gen(open_file=(file), endian=endian)




