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



    def get_frame_IDs(self):
        """should be in text file in future"""
        self.FRAMES_ID = \
            {
            "TestFrameData": 100,
            "TestFrameData2": 101,
            }

    def init_program_variables(self):
        self.frame_name_list = list() #list of frame names
        self.variables = list() # list of lists that contains variables per frame name
        self.data_types = list() # list of lists that contains data types of variables per frame name
        self.dlc_list = list() # list that contains data byte len per frame name


    def define_file_addresses(self):
        self.input_data_address = "input_frames"

        self.convert_received_files_storage_folder = "output_decode/decode_frame_files/"
        self.convert_received_data_storage_folder = "output_decode/"

        self.prepare_data_to_send_files_storage_folder = "output_create/code_frame_files/"
        self.prepare_data_to_send_storage_folder = "output_create/"


    def conversion_options(self):
        '''endian   < = little ; > = big'''
        self.endian = "little"

    def convert_received_data_configuration(self):
        self.import_folder_address = "resources.function_generators.byte_frame_handling.output_decode.decode_frame_files"
        self.create_class_name = "ConvertReceivedDataBody"
        self.next_state_name = "StoreData"
        self.data_buffer_bytes_source = "states_data.UdpRead.data_buffer"
        self.store_self_source = "states_data.ConvertReceivedData"

        self.convert_received_data_file_name = "convert_received_data.py"
        self.content_of_convert_received_data_file = ""

    def convert_data_to_send_configuration(self):
        self.import_folder_address = "resources.function_generators.byte_frame_handling.output_create.code_frame_files"
        self.create_class_name = "PrepareDataToSendBody"
        self.next_state_name = "SendData"
        self.alternative_next_state_name = "StoreSendData"
        self.data_storage_class = "states_data"
        self.store_self_source = "states_data.PrepareDataToSend"

        self.convert_send_data_file_name = "prepare_data_to_send.py"
        self.content_of_convert_send_data_file = ""


    def first_input_check(self):
        print(">>>       {}".format(self.files))
        print(">>>       {}".format(self.FRAMES_ID))
        if len(self.files) == (len(self.FRAMES_ID) + 1):
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
            _, _, _, _ = frame_create_functions_gen(open_file=(file), endian=self.endian,
                                                    input_folder=self.input_data_address,
                                                    output_folder=self.prepare_data_to_send_files_storage_folder )

            frame_name, variable_list, data_types, dlc = \
                frame_decode_functions_gen(open_file=(file), endian=self.endian,
                                           input_folder=self.input_data_address,
                                           output_folder=self.convert_received_files_storage_folder )

            self.frame_name_list.append(frame_name)
            self.variables.append(variable_list)
            self.data_types.append(data_types)
            self.dlc_list.append(dlc)

    def main_decode_function_gen(self):
        def create_class():
            self.content_of_convert_received_data_file += \
                "from threading import Lock\n" + \
                "\n"

            self.content_of_convert_received_data_file += \
                "\n" + \
                "class {}():\n".format(self.create_class_name) + \
                "    \"\"\"\n" + \
                "    We define a state object which provides some utility functions for the\n" + \
                "    individual states within the state machine.\n" + \
                "    \"\"\"\n\n"

            self.content_of_convert_received_data_file += \
                "    \"\"\"Header function\"\"\"\n" + \
                "    from {}.Header import Header_data_decode".format(self.import_folder_address) + \
                "\n\n" + \
                "    \"\"\"Data convert functions\"\"\"\n"

            for name in self.frame_name_list:
                if "Header" not in name:
                    string = "    from {0}.{1} import {1}_data_decode\n".format(self.import_folder_address, name)
                    self.content_of_convert_received_data_file += string

            self.content_of_convert_received_data_file += "\n"

        def create_init_function():
            self.content_of_convert_received_data_file += \
                "    def __init__(self):\n" + \
                "        self.next_state = self.__class__.__name__\n" + \
                "        self.lock = Lock() # threading Lock mechanism\n" + \
                "        \"\"\"\n" + \
                "        self.lock.acquire() # lock before read/save data\n" + \
                "        self.lock.release() # unlock.\n" + \
                "        \"\"\"\n\n" + \
                "        self.init_identification_frame_numbers()\n" + \
                "        self.init_header_variables()\n" + \
                "        self.init_received_variables()" + "\n" + \
                "" + "\n"

        def create_init_identification_frame_numbers_function():
            self.content_of_convert_received_data_file += \
                "    def init_identification_frame_numbers(self):" + "\n" + \
                "        self.FRAMES_ID = {" + "\n"

            for name in self.FRAMES_ID:
                self.content_of_convert_received_data_file += \
                "                          \"{}\": {},\n".format(name, self.FRAMES_ID[name])

            self.content_of_convert_received_data_file += \
                "                         }" + "\n" + \
                "        self.FRAMES_DLC = {\n"

            for i in range(len(self.frame_name_list)):
                if "Header" not in self.frame_name_list[i]:

                    self.content_of_convert_received_data_file += \
                    "                           \"{}\": {},\n".format(self.frame_name_list[i], self.dlc_list[i])

            self.content_of_convert_received_data_file += \
                    "                          }" + "\n" + \
                    "" + "\n"

        def create_init_system_variables_function():

            self.content_of_convert_received_data_file += \
                "    def init_system_variables(self):" + "\n" + \
                    "        self.data_buffer_bytes = None" + "\n" + \
                    "" + "\n"

        def create_init_header_variables_function():
            self.content_of_convert_received_data_file += \
                    "    def init_header_variables(self):" + "\n"

            for i in range(len(self.frame_name_list)):
                if "Header" in self.frame_name_list[i]:
                    for ii in range(len(self.variables[i])):
                        self.content_of_convert_received_data_file += \
                        "        self.{} = {}\n".format(self.variables[i][ii], self.data_types[i][ii])

            self.content_of_convert_received_data_file += "\n"

        def create_init_received_variables_function():
            self.content_of_convert_received_data_file += \
                "    def init_received_variables(self):" + "\n"

            for i in range(len(self.frame_name_list)):
                if "Header" not in self.frame_name_list[i]:
                    self.content_of_convert_received_data_file += \
                    "        #{} variables\n".format(self.frame_name_list[i])
                    for ii in range(len(self.variables[i])):
                        self.content_of_convert_received_data_file += \
                        "        self.{} = {}\n".format(self.variables[i][ii], self.data_types[i][ii])

            self.content_of_convert_received_data_file += "\n"

        def create_identify_frames_func():
            dlc_number = self.frame_name_list.index("Header")
            header_dlc = self.dlc_list[dlc_number]

            self.content_of_convert_received_data_file += \
                "    def identify_frames(self, frame):" + "\n" + \
                "        self.Header_data_decode(frame)" + "\n" + \
                "        return frame[{}:]".format(header_dlc) + "\n" + \
                "" + "\n"

        def create_get_data_function():
            self.content_of_convert_received_data_file += \
                "    def get_data(self, states_data):" + "\n" + \
                "        self.lock.acquire() # lock before read/save data" + "\n" + \
                "        self.data_buffer_bytes = {}\n".format(self.data_buffer_bytes_source) + \
                "        self.lock.release() # unlock" + "\n" + \
                "" + "\n"

        def create_store_data_function():
            self.content_of_convert_received_data_file += \
                "    def store_data(self, states_data):" + "\n" + \
                "        self.lock.acquire()  # lock before read/save data" + "\n" + \
                "        #states_data.{} = self\n".format(self.create_class_name.rstrip("ody").rstrip("B")) + \
                "        self.lock.release()  # unlock" + "\n" + \
                "" + "\n"

        def create_decoding_data_in_frame_function():
            self.content_of_convert_received_data_file += \
                "    def decoding_data_in_frame(self, frame_data):" + "\n"

            operator = "if"

            for name in self.frame_name_list:
                if "Header" not in name:
                    self.content_of_convert_received_data_file += \
                        "        {} self.ID == self.FRAMES_ID[\"{}\"]:\n".format(operator, name) + \
                        "            self.{}_data_decode(frame_data)\n".format(name)
                    operator = "elif"
            self.content_of_convert_received_data_file += \
                "        else:" + "\n" + \
                "            print(\">>> error: unknown frame ID\")\n\n"

        def create_run_state_function():
            self.content_of_convert_received_data_file += \
                "    def run_state(self,  states_data, GUI_data):" + "\n" + \
                "        \"\"\"" + "\n" + \
                "        Handle events that are delegated to this State." + "\n" + \
                "        \"\"\"" + "\n" + \
                "        self.init_system_variables() #init/refresh data buffer for new fraemes" + "\n" + \
                "" + "\n" + \
                "        self.get_data(states_data) # data from UDP Read state stored in states_data_buffer.py" + "\n" + \
                "" + "\n" + \
                "        try:" + "\n" + \
                "            for frame in self.data_buffer_bytes:" + "\n" + \
                "                frame_data = self.identify_frames(frame) # decode ID in frame" + "\n" + \
                "                self.decoding_data_in_frame(frame_data) # decode data in frame and update variables in this class" + "\n" + \
                "        except:" + "\n" + \
                "            '''no frames in buffer'''" + "\n" + \
                "            pass" + "\n" + \
                "" + "\n" + \
                "        self.store_data(states_data) # store data in states_data_buffer.py" + "\n" + \
                "" + "\n" + \
                "        self.next_state = \"{}\"".format(self.next_state_name)





        self.convert_received_data_configuration() # get configuration

        create_class()
        create_init_function()
        create_init_identification_frame_numbers_function()
        create_init_system_variables_function()
        create_init_header_variables_function()
        create_init_received_variables_function()
        create_identify_frames_func()
        create_get_data_function()
        create_store_data_function()
        create_decoding_data_in_frame_function()
        create_run_state_function()

        file = open(self.convert_received_data_storage_folder + self.convert_received_data_file_name, "w")
        print(self.content_of_convert_received_data_file, file = file)
        self.content_of_convert_received_data_file = ""

    def main_code_function(self):
        def create_class():
            self.content_of_convert_send_data_file += \
                "from threading import Lock\n" + \
                "\n"

            self.content_of_convert_send_data_file += \
                "\n" + \
                "class {}():\n".format(self.create_class_name) + \
                "    \"\"\"\n" + \
                "    We define a state object which provides some utility functions for the\n" + \
                "    individual states within the state machine.\n" + \
                "    \"\"\"\n\n"
            self.content_of_convert_send_data_file += \
            "    \"\"\"Header function\"\"\"\n" + \
            "    from {}.Header import Header_data_code".format(self.import_folder_address) + \
            "\n\n" + \
            "    \"\"\"Data convert functions\"\"\"\n"

            for name in self.frame_name_list:
                if "Header" not in name:
                    string = "    from {0}.{1} import {1}_data_code\n".format(self.import_folder_address, name)
                    self.content_of_convert_send_data_file += string

            self.content_of_convert_send_data_file += "\n"


        def create_init_function():
            self.content_of_convert_send_data_file += \
                "    def __init__(self):\n" + \
                "        self.next_state = self.__class__.__name__\n" + \
                "        self.lock = Lock() # threading Lock mechanism\n" + \
                "        \"\"\"\n" + \
                "        self.lock.acquire() # lock before read/save data\n" + \
                "        self.lock.release() # unlock.\n" + \
                "        \"\"\"\n\n" + \
                "        self.init_identification_frame_numbers()\n" + \
                "        self.init_header_variables()\n" + \
                "        self.init_send_variables()\n" + \
                "        self.init_system_variables()" + "\n" + \
                "" + "\n"

        def create_init_identification_frame_numbers_function():
            self.content_of_convert_send_data_file += \
                "    def init_identification_frame_numbers(self):" + "\n" + \
                "        self.FRAMES_ID = {" + "\n"

            for name in self.FRAMES_ID:
                self.content_of_convert_send_data_file += \
                "                          \"{}\": {},\n".format(name, self.FRAMES_ID[name])

            self.content_of_convert_send_data_file += \
                "                         }" + "\n" + \
                "        self.FRAMES_DLC = {\n"

            for i in range(len(self.frame_name_list)):
                if "Header" not in self.frame_name_list[i]:

                    self.content_of_convert_send_data_file += \
                    "                           \"{}\": {},\n".format(self.frame_name_list[i], self.dlc_list[i])

            self.content_of_convert_send_data_file += \
                    "                          }" + "\n" + \
                    "" + "\n"

        def create_init_header_variables_function():
            self.content_of_convert_send_data_file += \
                    "    def init_header_variables(self):" + "\n"

            for i in range(len(self.frame_name_list)):
                if "Header" in self.frame_name_list[i]:
                    for ii in range(len(self.variables[i])):
                        self.content_of_convert_send_data_file += \
                        "        self.{} = {}\n".format(self.variables[i][ii], self.data_types[i][ii])

            self.content_of_convert_send_data_file += "\n"

        def create_init_received_variables_function():
            self.content_of_convert_send_data_file += \
                "    def init_send_variables(self):" + "\n"

            for i in range(len(self.frame_name_list)):
                if "Header" not in self.frame_name_list[i]:
                    self.content_of_convert_send_data_file += \
                    "        #{} variables\n".format(self.frame_name_list[i])
                    for ii in range(len(self.variables[i])):
                        self.content_of_convert_send_data_file += \
                        "        self.{} = {}\n".format(self.variables[i][ii], self.data_types[i][ii])

            self.content_of_convert_send_data_file += "\n"

        def create_init_system_variables_function():

            self.content_of_convert_send_data_file += \
                "    def init_system_variables(self):" + "\n" + \
                    "        self.messages = list()" + "\n" + \
                    "" + "\n"

            for frame in self.frame_name_list:
                if "Header" not in frame:
                    self.content_of_convert_send_data_file += \
                    "        self.{}SendOrd = False\n".format(frame)

            self.content_of_convert_send_data_file += "\n"

        def create_get_data():
            self.content_of_convert_send_data_file += \
                "    def get_data(self,  states_data, GUI_data):" + "\n" + \
                "        self.lock.acquire()  # lock before read/save data" + "\n"


            for i in range(len(self.frame_name_list)):
                if "Header" not in self.frame_name_list[i]:
                    self.content_of_convert_send_data_file += \
                    "        #{}\n".format(self.frame_name_list[i])
                    for ii in range(len(self.variables[i])):
                        self.content_of_convert_send_data_file += \
                        "        self.{0} = {1}.{0}\n".format(self.variables[i][ii], self.data_storage_class)

            self.content_of_convert_send_data_file += "\n        #send orders\n"

            for neme in self.frame_name_list:
                if "Header" not in neme:
                    self.content_of_convert_send_data_file += \
                        "        self.{0}SendOrd = {1}.{0}SendOrd\n".format(neme, self.data_storage_class)

            self.content_of_convert_send_data_file += \
                "\n        self.lock.release()  # unlock" + "\n"

        def create_store_data_function():
            self.content_of_convert_send_data_file += \
                "    def store_data(self, states_data, GUI_data):" + "\n" + \
                "        self.lock.acquire()  # lock before read/save data" + "\n" + \
                "        #states_data.{} = self\n".format(self.create_class_name.rstrip("ody").rstrip("B") ) + \
                "" + "\n" + "        \"\"\"system\"\"\"" + "\n"

            for neme in self.frame_name_list:
                if "Header" not in neme:
                    self.content_of_convert_send_data_file += \
                        "        states_data.{0}SendOrd = self.{0}SendOrd\n".format(neme)

            self.content_of_convert_send_data_file += "\n" + \
            "        self.lock.release()  # unlock" + "\n\n"

        def create_build_frames():
            self.content_of_convert_send_data_file += \
                "    def build_frames(self, ID):" + "\n" + \
                "        \'\'\'byte frame = Header + data\'\'\'" + "\n" +\
                "        self.ID = ID" + '\n\n'



            condition= "if"

            for name in self.frame_name_list:
                if "Header" not in name:
                    self.content_of_convert_send_data_file += \
                    "        {} self.ID == self.FRAMES_ID[\"{}\"]:\n".format(condition, name) + \
                    "            self.DLC = self.FRAMES_DLC[\'{}\']".format(name) + "\n" + \
                    "            frame_header = self.Header(endian=\'{}\')\n".format(self.endian) + \
                    "            frame_data = self.{}(endian=\'{}\')\n".format(name, self.endian)
                    condition = "elif"

            self.content_of_convert_send_data_file += \
            "\n        return frame_header + frame_data\n\n"

        def create_run_state():
            self.content_of_convert_send_data_file += \
                "    def run_state(self,  states_data, GUI_data):" + "\n" + \
                "        \'\'\'\n" + \
                "        Handle events that are delegated to this State.\n" + \
                "        \'\'\'\n" +\
                "        self.get_data(states_data, GUI_data)\n\n" + \
                "        self.messages = list() #clear list\n\n"

            self.content_of_convert_send_data_file += "        #Tranzition condition:\n"
            self.content_of_convert_send_data_file += "        if"
            for name in self.frame_name_list:
                if "Header" not in name:
                    self.content_of_convert_send_data_file += \
                        " self.{}SendOrd or".format(name)

            self.content_of_convert_send_data_file =  self.content_of_convert_send_data_file.rstrip(" or") + ":\n" + \
            "            self.next_state = \"{}\"\n".format(self.next_state_name) + \
            "        else:\n" + \
            "            self.next_state = \"{}\"\n\n".format(self.alternative_next_state_name)


            self.content_of_convert_send_data_file += "        #Prepare frames:\n"

            for name in self.frame_name_list:
                if "Header" not in name:
                    self.content_of_convert_send_data_file += \
                    "        if self.{}SendOrd == True:\n".format(name) + \
                    "            self.{}SendOrd = False\n".format(name) + \
                    "            self.store_data(states_data, GUI_data)\n" + \
                    "            self.messages.append(self.build_frames(self.FRAMES_ID[\"{}\"]))\n\n".format(name)

            self.content_of_convert_send_data_file += "        #Update data:\n" + \
            "        self.store_data(states_data, GUI_data)"










        self.convert_data_to_send_configuration() # get configuration

        create_class()
        create_init_function()
        create_init_identification_frame_numbers_function()
        create_init_header_variables_function()
        create_init_received_variables_function()
        create_init_system_variables_function()
        create_get_data()
        create_store_data_function()
        create_build_frames()
        create_run_state()

        self.prepare_data_to_send_files_storage_folder = "output_create/code_frame_files/" # to delete
        self.prepare_data_to_send_storage_folder = "output_create/" # to delete

        file = open(self.prepare_data_to_send_storage_folder + self.convert_send_data_file_name, "w")
        print(self.content_of_convert_send_data_file, file = file)
        self.content_of_convert_send_data_file = ""


if __name__ == "__main__":

    g = FrameHandlerFunctionsGenerator()

    '''check correction of input files'''
    g.first_input_check()
    g.frame_data_files_gen()
    #g.second_input_check()
    g.main_decode_function_gen()
    g.main_code_function()
