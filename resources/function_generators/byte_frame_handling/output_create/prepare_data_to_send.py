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
        self.init_send_variables()
        self.init_system_variables()

    def init_identification_frame_numbers(self):
        self.FRAMES_ID = {
                          "TestFrameData": 100,
                          "TestFrameData2": 101,
                         }
        self.FRAMES_DLC = {
                           "TestFrameData": 14,
                           "TestFrameData2": 5,
                          }


