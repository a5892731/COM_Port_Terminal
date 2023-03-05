from resources.function_generators.byte_frame_handling.resources.frame_create_functions_gen import frame_create_functions_gen
from resources.function_generators.byte_frame_handling.resources.frame_decode_functions_gen import frame_decode_functions_gen

import os


class FrameHandlerFunctionsGenerator():
    def __init__(self):
        """get dictionary of frames IDs"""
        self.get_frame_IDs()
        """define output/input files addresses"""
        self.define_file_addresses()
        """init program options"""
        self.conversion_options()
        """init program variables"""
        self.init_program_variables()

        """find input files"""
        self.find_input_files(adress=self.input_data_address)

        """text data to generate in convert_received_data file"""
        self.convert_received_data_text_data_init()

    def get_frame_IDs(self):
        """should be in text file in future"""
        self.FRAMES_IDs = \
            {
            "TestFrameData": 100,
            "TestFrameData2": 101,
            }
    def init_program_variables(self):
        self.frame_name_list = list() #list of frame names
        self.variables = list() # list of lists that contains variables per frame name
        self.data_types = list() # list of lists that contains data types of variables per frame name


    def define_file_addresses(self):
        self.input_data_address = "input_frames"
    def conversion_options(self):
        '''endian   < = little ; > = big'''
        self.endian = "little"

    def convert_received_data_text_data_init(self):
        self.import_folder_address = "resources.function_generators.byte_frame_handling.output_decode.TestFrameData"
        self.create_class_name = "ConvertReceivedDataBody"
        self.next_state_name = "StoreData"
        self.data_buffer_bytes_source = "states_data.UdpRead.data_buffer"
        self.store_self_source = "states_data.ConvertReceivedData"

        self.content_of_convert_received_data_file = ""

    def first_input_check(self):
        print(">>>       {}".format(self.files))
        print(">>>       {}".format(self.FRAMES_IDs))
        if len(self.files) == (len(self.FRAMES_IDs) + 1):
            print(">>> correct: number of files and data ID is correct")
        else:
            print(">>> error: number of files don't match number of IDs in self.FRAMES_IDs variable")

    def second_input_check(self):
        for i in range(len(self.frame_name_list)):
            print(">>>       File: {}.py".format(self.frame_name_list[i]))
            for ii in range(len(self.variables[i])):
                print(">>>       variable {}: {} {}".format(ii +1, self.variables[i][ii], self.data_types[i][ii],))





    def find_input_files(self, adress="input_frames"):
        os.chdir(adress)
        for root, dirs, files in os.walk('.', topdown=False, onerror=None, followlinks=True):
            pass
        os.chdir("..")
        self.files = files


    def frame_data_files_gen(self):

        for file in self.files:
            _, _, _ = frame_create_functions_gen(open_file=(file), endian=self.endian,
                                                                               input_folder=self.input_data_address,
                                                                               output_folder="output_create")


            frame_name, variable_list, data_types = frame_decode_functions_gen(open_file=(file), endian=self.endian,
                                                                               input_folder=self.input_data_address,
                                                                               output_folder="output_decode")

            self.frame_name_list.append(frame_name)
            self.variables.append(variable_list)
            self.data_types.append(data_types)


    def main_decode_function_gen(self):



        self.content_of_convert_received_data_file = ""

if __name__ == "__main__":

    g = FrameHandlerFunctionsGenerator()

    '''check correction of input files'''
    g.first_input_check()
    g.frame_data_files_gen()
    g.main_decode_function_gen()
    g.second_input_check()

