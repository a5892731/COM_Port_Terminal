from threading import Lock

"""Header function"""
from resources.function_generators.byte_frame_handling.output_decode.Header import Header_data_decode

"""Data convert functions"""
from resources.function_generators.byte_frame_handling.output_decode.TestFrameData import TestFrameData_data_decode
from resources.function_generators.byte_frame_handling.output_decode.TestFrameData2 import TestFrameData2_data_decode

class ConvertReceivedDataBody():
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


