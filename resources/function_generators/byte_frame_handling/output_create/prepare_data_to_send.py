from threading import Lock

"""Header function"""
from resources.function_generators.byte_frame_handling.output_create.code_frame_files.Header import Header_data_code

"""Data convert functions"""
from resources.function_generators.byte_frame_handling.output_create.code_frame_files.TestFrameData import TestFrameData_data_code
from resources.function_generators.byte_frame_handling.output_create.code_frame_files.TestFrameData2 import TestFrameData2_data_code

class PrepareDataToSendBody():
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self):
        self.next_state = self.__class__.__name__
        self.lock = Lock() # threading Lock mechanism
        """
        self.lock.acquire() # lock before read/save data
        self.lock.release() # unlock.
        """

        self.init_identification_frame_numbers()
        self.init_header_variables()
        self.init_send_variables()
        self.init_system_variables()

    def init_identification_frame_numbers(self):
        self.FRAMES_ID = {
                          "TestFrameData": 100,
                          "TestFrameData2": 101,
                         }
        self.FRAMES_DLC = {
                           "TestFrameData": 14,
                           "TestFrameData2": 12,
                          }

    def init_header_variables(self):
        self.ID = int()
        self.DLC = int()

    def init_send_variables(self):
        #TestFrameData variables
        self.variable1 = int()
        self.variable2 = int()
        self.variable3 = float()
        self.variable4 = int()
        self.variable5 = int()
        #TestFrameData2 variables
        self.variable6 = int()
        self.variable7 = int()
        self.variable8 = float()

    def init_system_variables(self):
        self.messages = list()

        self.TestFrameDataSendOrd = False
        self.TestFrameData2SendOrd = False

    def get_data(self,  states_data, GUI_data):
        self.lock.acquire()  # lock before read/save data
        #TestFrameData
        self.variable1 = states_data.variable1
        self.variable2 = states_data.variable2
        self.variable3 = states_data.variable3
        self.variable4 = states_data.variable4
        self.variable5 = states_data.variable5
        #TestFrameData2
        self.variable6 = states_data.variable6
        self.variable7 = states_data.variable7
        self.variable8 = states_data.variable8

        #send orders
        self.TestFrameDataSendOrd = states_data.TestFrameDataSendOrd
        self.TestFrameData2SendOrd = states_data.TestFrameData2SendOrd

        self.lock.release()  # unlock
    def store_data(self, states_data):
        self.lock.acquire()  # lock before read/save data
        #states_data.PrepareDataToSend = self
        self.lock.release()  # unlock

        """system"""
        states_data.TestFrameDataSendOrd = self.TestFrameDataSendOrd
        states_data.TestFrameData2SendOrd = self.TestFrameData2SendOrd

    def build_frames(self, ID):
       '''byte frame = Header + data'''
