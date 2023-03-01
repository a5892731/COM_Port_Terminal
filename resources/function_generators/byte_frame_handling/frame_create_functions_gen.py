'''
author: a5892731
creation date: 22.02.2023
update date:  01.03.2023

description:
this is a generator of files that contains functions that purpose are coding data to byte stream,
that can be sent via udp, com, etc.
generator mus be supported by input text file (in folder input)

input text file example:
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

import os


def generator(open_file, endian, input_folder = "input", output_folder = "output_create"):
    byte_number = 0
    output = []
    variables = []
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
        elif "int32_t" in line:
            variable_name = line[12::].rstrip(" {};\n")
            variables.append(variable_name)
            data_types.append("int()")
            output.append("    {0} = convert_variable_to_bytes(value=self.{0}, type =\"int32_t\", endian=endian)".
                          format(variable_name, ))
            return_value.append(variable_name)
        elif "int8_t" in line:
            variable_name = line[11::].rstrip(" {};\n")
            data_types.append("byte()")
            variables.append(variable_name)
            output.append("    {0} = convert_variable_to_bytes(value=self.{0}, type =\"unsigned char\", endian=endian)".
                          format(variable_name, ))
            return_value.append(variable_name)
        elif "double" in line:
            variable_name = line[11::].rstrip(" {};\n")
            data_types.append("int()")
            variables.append(variable_name)
            output.append("    {0} = convert_variable_to_bytes(value=self.{0}, type =\"double\", endian=endian)".
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



    file_name = "{}/{}.py".format(output_folder, open_file.rstrip(".txt"))

    file = open(file_name, "w")
    for line in output:
        print(line, file=file)

    print("---------------------------------------------------------------------------------")
    print("Instruction to File: {}".format(file_name))
    print(">>> add variables to your program:\n")


    if frame_name == "Header":
        for i in range(len(variables)):
            print("    {} = {}".format(variables[i], data_types[i]))
    else:
        for i in range(len(variables)):
            print("    self.{} = {}".format(variables[i], data_types[i]))




    #print("    self.last_frame = list()")



def find_input_files(adress="input"):
    os.chdir(adress)
    for root, dirs, files in os.walk('.', topdown=False, onerror=None, followlinks=True):
        pass
    os.chdir("..")
    return files

#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    input_data_address = "input"

    '''start byte number'''
    start_byte_number = 0
    '''endian   < = little ; > = big'''
    endian = "little"


    """run"""

    files_list = find_input_files(adress=input_data_address)
    print("input files: " + str(files_list))

    for file in files_list:
        generator(open_file=(file), endian=endian)




