'''
here are the rules of state transition
'''


'''import all of states body classes'''
from resources.state_machine.states.s00_initialization import InitializationBody
from resources.state_machine.states.s01_close_program import CloseProgramBody
from resources.state_machine.states.s02_read_serial_configuration import ReadSerialConfigurationBody
from resources.state_machine.states.s03_serial_connect import SerialConnectBody
from resources.state_machine.states.s04_read_serial_data import ReadSerialDataBody
from resources.state_machine.states.s05_send_serial_data import SendSerialDataBody



class Initialization(InitializationBody):
    def on_event(self, event, states_data):
        '''import memory from States class'''
        self = states_data.Initialization

        '''control_word'''
        if event == 'device_locked':
            '''run your functions in this state'''
            self.run_state()
        else:
            states_data.CloseProgram.info = ">>> Info: device unlocked in {} state".format(self)
            return states_data.CloseProgram

        '''transition conditions'''
        if self.next_state == "ReadSerialConfiguration":
            return states_data.ReadSerialConfiguration
        else:
            states_data.CloseProgram.info = ">>> Info: transition error in {} state".format(self)
            return states_data.CloseProgram

class CloseProgram(CloseProgramBody):
    def on_event(self, event, states_data):
        '''import memory from States class'''
        self = states_data.CloseProgram
        '''run your functions in this state'''
        self.run_state()

class ReadSerialConfiguration(ReadSerialConfigurationBody):
    def on_event(self, event, states_data):
        '''import memory from States class'''
        self = states_data.ReadSerialConfiguration

        self.run_state(states_data)

        if self.next_state == "SerialConnect":
            return states_data.SerialConnect
        elif self.next_state == "ReadSerialConfiguration":
            return states_data.ReadSerialConfiguration
        else:
            states_data.CloseProgram.info = ">>> Info: transition error in {} state".format(self)
            return states_data.CloseProgram


class SerialConnect(SerialConnectBody):
    def on_event(self, event, states_data):
        '''import memory from States class'''
        self = states_data.SerialConnect
        self.run_state(states_data)

        if self.next_state == "SerialConnect":
            return states_data.SerialConnect
        elif self.next_state == "ReadSerialConfiguration":
            return states_data.ReadSerialData
        elif self.next_state == "ReadSerialData":
            return states_data.ReadSerialData
        elif self.next_state == "CloseProgram":
            return states_data.CloseProgram
        else:
            states_data.CloseProgram.info = ">>> Info: transition error in {} state".format(self)
            return states_data.CloseProgram

class ReadSerialData(ReadSerialDataBody):
    def on_event(self, event, states_data):
        '''import memory from States class'''
        self = states_data.ReadSerialData

        self.run_state(states_data)

        if self.next_state == "ReadSerialData":
            return states_data.ReadSerialData
        elif self.next_state == "SendSerialData":
            return states_data.SendSerialData
        elif self.next_state == "CloseProgram":
            return states_data.CloseProgram
        else:
            states_data.CloseProgram.info = ">>> Info: transition error in {} state".format(self)
            return states_data.CloseProgram

class SendSerialData(SendSerialDataBody):
    '''SEND DATA IS INDICATED BY BUTTONS EVENTS'''

    def on_event(self, event, states_data):
        '''import memory from States class'''
        self = states_data.SendSerialData

        self.run_state(states_data)

        if self.next_state == "ReadSerialData":
            return states_data.ReadSerialData
        elif self.next_state == "SendSerialData":
            return states_data.SendSerialData
        elif self.next_state == "CloseProgram":
            return states_data.CloseProgram
        else:
            states_data.CloseProgram.info = ">>> Info: transition error in {} state".format(self)
            return states_data.CloseProgram






