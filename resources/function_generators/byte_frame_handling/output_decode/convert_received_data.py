from threading import Lock


class ConvertReceivedDataBody():
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    """Header function"""
    from resources.function_generators.byte_frame_handling.output_decode.decode_frame_files.Header import Header_data_decode

    """Data convert functions"""
    from resources.function_generators.byte_frame_handling.output_decode.decode_frame_files.TestFrameData import TestFrameData_data_decode
    from resources.function_generators.byte_frame_handling.output_decode.decode_frame_files.TestFrameData2 import TestFrameData2_data_decode

    def __init__(self):
        self.next_state = self.__class__.__name__
        self.lock = Lock() # threading Lock mechanism
        """
        self.lock.acquire() # lock before read/save data
        self.lock.release() # unlock.
        """

        self.init_identification_frame_numbers()
        self.init_header_variables()
        self.init_received_variables()

    def init_identification_frame_numbers(self):
        self.FRAMES_ID = {
                          "TestFrameData": 100,
                          "TestFrameData2": 101,
                         }
        self.FRAMES_DLC = {
                           "TestFrameData": 14,
                           "TestFrameData2": 12,
                          }

    def init_system_variables(self):
        self.data_buffer_bytes = None

    def init_header_variables(self):
        self.ID = int()
        self.DLC = int()

    def init_received_variables(self):
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

    def identify_frames(self, frame):
        self.Header_data_decode(frame)
        return frame[2:]

    def get_data(self, states_data):
        self.lock.acquire() # lock before read/save data
        self.data_buffer_bytes = states_data.UdpRead.data_buffer
        self.lock.release() # unlock

    def store_data(self, states_data):
        self.lock.acquire()  # lock before read/save data
        #states_data.ConvertReceivedData = self
        self.lock.release()  # unlock

    def decoding_data_in_frame(self, frame_data):
        if self.ID == self.FRAMES_ID["TestFrameData"]:
            self.TestFrameData_data_decode(frame_data)
        elif self.ID == self.FRAMES_ID["TestFrameData2"]:
            self.TestFrameData2_data_decode(frame_data)
        else:
            print(">>> error: unknown frame ID")

    def run_state(self,  states_data, GUI_data):
        """
        Handle events that are delegated to this State.
        """
        self.init_system_variables() #init/refresh data buffer for new fraemes

        self.get_data(states_data) # data from UDP Read state stored in states_data_buffer.py

        try:
            for frame in self.data_buffer_bytes:
                frame_data = self.identify_frames(frame) # decode ID in frame
                self.decoding_data_in_frame(frame_data) # decode data in frame and update variables in this class
        except:
            '''no frames in buffer'''
            pass

        self.store_data(states_data) # store data in states_data_buffer.py

        self.next_state = "StoreData"
