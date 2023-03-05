from threading import Lock

from resources.functions.convert_variable_to_bytes import convert_variable_to_bytes

class PrepareDataToSendBody(object):
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self):
        """
        We define a state object which provides some utility functions for the
        individual states within the state machine.
        """
        self.next_state = self.__class__.__name__
        self.lock = Lock() # threading Lock mechanism
        '''
        self.lock.acquire() # lock before read/save data
        self.lock.release() # unlock
        '''
        self.init_identification_frame_numbers()
        self.init_send_variables()
        self.init_system_variables()

    def init_identification_frame_numbers(self):
        self.FRAMES_ID = {
                         "TurbidityFrame": 100,
                         "LightsFrame": 101,
                         "ThrusterFrame": 102,
                         "HumidityFrame": 103,
                         "TemperatureFrame": 104,
                         "AnalogsFrame": 105,
                         "TurbiditySettings": 106,
                         "LightsSettings": 107,
                         "ThrusterSettings": 108,
                         }

        self.FRAMES_DLC = {
                         "TurbidityFrame": 22,
                         "LightsFrame": 5,
                         "ThrusterFrame": 17,
                         "HumidityFrame": 8,
                         "TemperatureFrame": 8,
                         "AnalogsFrame": 32,
                         "TurbiditySettings": 4,
                         "LightsSettings": 5,
                         "ThrusterSettings": 5,
                         }
    def init_system_variables(self):
        self.TurbiditySettingsSendOrd = False
        self.LightsSettingsSendOrd = False
        self.ThrusterSettingsSendOrd = False

        self.message = b''
        self.data = {}

    def init_send_variables(self):
        '''Turbidity'''
        self.TurbidityGainA  = False #bool on byte
        self.TurbidityGainB = False #bool on byte
        '''Lights'''
        self.LightTurrnOn= False #bool on byte
        self.LightsPwmPulseWidth = 0 #int
        self.LightsPwmPulseStepTime = 0 #int
        '''Thruster'''
        self.ThrusterTurrnOn= False #bool on byte
        self.ThrusterPwmPulseWidth = 0 #int
        self.ThrusterPwmPulseStepTime = 0 #int

    def get_system_data(self, states_data):
        self.lock.acquire() # lock before read/save data
        '''Turbidity'''
        self.TurbidityGainA = states_data.TurbidityGainA
        self.TurbidityGainB = states_data.TurbidityGainB
        '''Lights'''
        self.LightTurrnOn = states_data.LightTurrnOn
        self.LightsPwmPulseWidth = states_data.LightsPwmPulseWidth
        self.LightsPwmPulseStepTime = states_data.LightsPwmPulseStepTime
        '''Thruster'''
        self.ThrusterTurrnOn = states_data.ThrusterTurrnOn
        self.ThrusterPwmPulseWidth = states_data.ThrusterPwmPulseWidth
        self.ThrusterPwmPulseStepTime = states_data.ThrusterPwmPulseStepTime
        """system"""

        #self.TurbiditySettingsSendOrd = states_data.TurbiditySettingsSendOrd
        self.TurbiditySettingsSendOrd = states_data.TurbiditySystemState.TurbiditySettingsSendOrd
        self.LightsSettingsSendOrd = states_data.LightsSettingsSendOrd
        self.ThrusterSettingsSendOrd = states_data.ThrusterSettingsSendOrd
        ''''''
        self.lock.release()  # unlock

    def build_frames(self, ID):
        '''byte frame = Header + data [TurbiditySettings, or LightsSettings or ... , etc.]'''

        def Header(id, dlc, endian="little"):
            '''
            struct Header
            {
            private:
                int32_t ID {};
                int8_t DLC {};
                int8_t reserved0 {};
                int8_t reserved1 {};
                int8_t reserved2 {};
            };
            '''
            ID = convert_variable_to_bytes(value=id, type="int32_t", endian=endian)
            DLC = convert_variable_to_bytes(value=dlc, type="unsigned char", endian=endian)
            reserved0 = convert_variable_to_bytes(value=0, type="unsigned char")
            reserved1 = convert_variable_to_bytes(value=0, type="unsigned char")
            reserved2 = convert_variable_to_bytes(value=0, type="unsigned char")

            header = ID + DLC + reserved0 + reserved1 + reserved2
            return header

        def TurbiditySettingsData(endian="little"):
            '''
            enum Id: TurbiditySettings {
            int8_t TurbidityGainA {};
            int8_t TurbidityGainB {};
            int8_t reserved {};
            int8_t reserved {};
            };
            '''

            TurbidityGainA = convert_variable_to_bytes(value=self.TurbidityGainA, type="unsigned char")
            TurbidityGainB = convert_variable_to_bytes(value=self.TurbidityGainB, type="unsigned char")
            reserved0 = convert_variable_to_bytes(value=0, type="unsigned char")
            reserved1 = convert_variable_to_bytes(value=0, type="unsigned char")

            TurbiditySettingsData = TurbidityGainA + TurbidityGainB + reserved0 + reserved1

            #self.data = [self.FRAMES_ID["TurbiditySettings"], self.FRAMES_DLC["TurbiditySettings"],
            #             self.TurbidityGainA, self.TurbidityGainB, 0, 0]


            self.data = {"ID":self.FRAMES_ID["TurbiditySettings"], "DLC":self.FRAMES_DLC["TurbiditySettings"],
                         "TurbidityGainA":self.TurbidityGainA, "TurbidityGainB":self.TurbidityGainB,
                         "reserved0":0, "reserved1":0}


            return TurbiditySettingsData

        def LightsSettingsData(endian="little"):
            '''
            enum Id: LightsSettings
            {
                int8_t LightTurrnOn {};
                int32_t LightsPwmPulseWidth {};
                int32_t LightsPwmPulseStepTime {};
            };
            '''
            LightTurrnOn = convert_variable_to_bytes(value=self.LightTurrnOn, type="unsigned char", endian=endian)
            LightsPwmPulseWidth = convert_variable_to_bytes(value=self.LightsPwmPulseWidth, type="int32", endian=endian)
            LightsPwmPulseStepTime = convert_variable_to_bytes(value=self.LightsPwmPulseStepTime, type="int32", endian=endian)

            LightsSettingsData = LightTurrnOn + LightsPwmPulseWidth + LightsPwmPulseStepTime

            #self.data = [self.FRAMES_ID["LightsSettings"], self.FRAMES_DLC["LightsSettings"],
            #             self.LightTurrnOn, self.LightsPwmPulseWidth, self.LightsPwmPulseStepTime]

            self.data = {"ID":self.FRAMES_ID["LightsSettings"], "DLC":self.FRAMES_DLC["LightsSettings"],
                         "LightTurnOn":self.LightTurrnOn, "LightsPwmPulseWidth":self.LightsPwmPulseWidth,
                         "LightsPwmPulseStepTime":self.LightsPwmPulseStepTime}


            return LightsSettingsData

        def ThrusterSettingsData(endian="little"):
            '''
            enum Id: ThrusterSettings {
            int8_t ThrusterTurrnOn {};
            int32_t ThrusterPwmPulseWidth {};
            int32_t ThrusterPwmPulseStepTime {};
            };
            '''
            ThrusterTurrnOn = convert_variable_to_bytes(value=self.ThrusterTurrnOn, type="unsigned char",
                                                        endian=endian)
            ThrusterPwmPulseWidth = convert_variable_to_bytes(value=self.ThrusterPwmPulseWidth, type="int32",
                                                              endian=endian)
            ThrusterPwmPulseStepTime = convert_variable_to_bytes(value=self.ThrusterPwmPulseStepTime, type="int32",
                                                                 endian=endian)

            ThrusterSettingsData = ThrusterTurrnOn + ThrusterPwmPulseWidth + ThrusterPwmPulseStepTime

            #self.data = [self.FRAMES_ID["ThrusterSettings"], self.FRAMES_DLC["ThrusterSettings"],
            #             self.ThrusterTurrnOn, self.ThrusterPwmPulseWidth, self.ThrusterPwmPulseStepTime]

            self.data = {"ID":self.FRAMES_ID["ThrusterSettings"], "DLC":self.FRAMES_DLC["ThrusterSettings"],
                         "ThrusterTurnOn":self.ThrusterTurrnOn, "ThrusterPwmPulseWidth":self.ThrusterPwmPulseWidth,
                         "ThrusterPwmPulseStepTime":self.ThrusterPwmPulseStepTime}


            return ThrusterSettingsData

        if ID == self.FRAMES_ID["TurbiditySettings"]:
            frame_header = Header(self.FRAMES_ID["TurbiditySettings"], self.FRAMES_DLC["TurbiditySettings"],)
            frame_data = TurbiditySettingsData()

        elif ID == self.FRAMES_ID["LightsSettings"]:
            frame_header = Header(self.FRAMES_ID["LightsSettings"], self.FRAMES_DLC["LightsSettings"], )
            frame_data = LightsSettingsData()

        elif ID == self.FRAMES_ID["ThrusterSettings"]:
            frame_header = Header(self.FRAMES_ID["ThrusterSettings"], self.FRAMES_DLC["ThrusterSettings"], )
            frame_data = ThrusterSettingsData()


        #end_of_frame = b'\xff' # prevent from losing bytes with zero value on the end of frame
        #return frame_header + frame_data + end_of_frame
        return frame_header + frame_data

    def update_system_data(self, states_data):
        '''delete order after execution'''
        self.lock.acquire() # lock before read/save data
        """system"""
        states_data.TurbiditySettingsSendOrd = self.TurbiditySettingsSendOrd
        states_data.LightsSettingsSendOrd = self.LightsSettingsSendOrd
        states_data.ThrusterSettingsSendOrd = self.ThrusterSettingsSendOrd
        ''''''
        self.lock.release()  # unlock



    def run_state(self, states_data):
        """
        Handle events that are delegated to this State.
        """
        self.get_system_data(states_data)

        #print()
        #print("TurbiditySettingsSendOrd {}".format(self.TurbiditySettingsSendOrd))
        #print("LightsSettingsSendOrd {}".format(self.LightsSettingsSendOrd))
        #print("ThrusterSettingsSendOrd {}".format(self.ThrusterSettingsSendOrd))

        if self.TurbiditySettingsSendOrd == True:
            self.TurbiditySettingsSendOrd = False
            self.update_system_data(states_data)
            self.message = self.build_frames(self.FRAMES_ID["TurbiditySettings"])
            self.next_state = "SendData"

        elif self.LightsSettingsSendOrd == True:
            self.LightsSettingsSendOrd = False
            self.update_system_data(states_data)
            self.message = self.build_frames(self.FRAMES_ID["LightsSettings"])
            self.next_state = "SendData"

        elif self.ThrusterSettingsSendOrd == True:
            self.ThrusterSettingsSendOrd = False
            self.update_system_data(states_data)
            self.message = self.build_frames(self.FRAMES_ID["ThrusterSettings"])
            self.next_state = "SendData"

        else:
            self.next_state = "StoreSendData"