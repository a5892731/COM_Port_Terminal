'''
author: a5892731
creation date: 22.03.2023
update date: xx.xx.xxxx

description:
this is a generator of files that contains functions that purpose are decoding data from byte stream,
that was received via udp, com, etc.
generator must be supported by input text file (in folder input)

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

import os

def generator(open_file, endian, input_folder = "input", output_folder = "outpu_create"):
    byte_number = 0
    output = []
    file = open(input_folder + "/" + open_file, "r")

    variable_list = []

    comment = ''
    for comment_line in file:
        comment += "    " + comment_line

    file = open(input_folder + "/" + open_file, "r")




    output.append("from resources.functions.convert_bytes_to_variable import convert_bytes_to_variable")
    output.append("")


    for line in file:


        if "struct" in line:
            frame_name = line[6::].rstrip("\n")
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
        elif "int32_t" in line:
            variable_name = line[12::].rstrip(" {};\n")
            output.append("        self.{} = convert_bytes_to_variable(bytes = frame[\"data\"][{}:{}], data_type = \"{}i\")"
                          .format(variable_name, byte_number, byte_number + 4, endian))
            byte_number += 4
            variable_list.append(variable_name)
        elif "int8_t" in line:
            variable_name = line[11::].rstrip(" {};\n")
            output.append("        self.{} = convert_bytes_to_variable(bytes = frame[\"data\"][{}:{}], data_type = \"B\")"
                          .format(variable_name, byte_number, byte_number + 1))
            byte_number += 1
            variable_list.append(variable_name)
        elif "double" in line:
            variable_name = line[11::].rstrip(" {};\n")
            output.append("        self.{} = convert_bytes_to_variable(bytes = frame[\"data\"][{}:{}], data_type = \"{}d\")"
                          .format(variable_name, byte_number, byte_number + 8, endian))
            byte_number += 8
            variable_list.append(variable_name)
    output.append("    except TypeError:")
    output.append("        print(\"{}_data_decode(frame): except TypeError: TypeError: unhashable type: 'slice'\")".
                  format(frame_name))


    output.append("")

    #output.append("    return data")
    #for variable in variable_list:
    #    output.append("    self.{} = data[\"{}\"]".format(variable, variable))
    #output.append("")

    #output.append("    return data")






    file = open("{}/{}.py".format(output_folder, frame_name), "w")

    for line in output:
        print(line, file=file)


def find_input_files(adress="input"):
    os.chdir(adress)
    for root, dirs, files in os.walk('.', topdown=False, onerror=None, followlinks=True):
        pass
    os.chdir("..")
    return files

if __name__ == "__main__":

    input_data_address = "input"

    '''start byte number'''
    start_byte_number = 0
    '''endian   < = little ; > = big'''
    endian = "<"




    """run"""

    files_list = find_input_files(adress=input_data_address)
    print("input files: " + str(files_list))

    for file in files_list:
        generator(open_file=(file), endian=endian, input_folder = input_data_address, output_folder = "output_decode")

