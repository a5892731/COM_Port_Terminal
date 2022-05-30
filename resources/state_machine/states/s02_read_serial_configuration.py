from time import sleep

class ReadSerialConfigurationBody(object):

    def __init__(self,):
        """
        We define a state object which provides some utility functions for the
        individual states within the state machine.
        """
        self.next_state = "SerialConnect"

    def run_state(self, states_data):
        '''serial_port > system > com.py'''

        states_data.com.read_configuration(data_file = "resources/serial_port/data_files/PORT_COM.txt")


    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.__class__.__name__



