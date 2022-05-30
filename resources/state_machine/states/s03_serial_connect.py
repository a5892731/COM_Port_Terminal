class SerialConnectBody(object):

    def __init__(self,):
        """
        We define a state object which provides some utility functions for the
        individual states within the state machine.
        """
        self.next_state = "ReadSerialData"

    def run_state(self, states_data):
        '''serial_port > system > com.py'''

        errorType = None
        try:
            states_data.com.serial_connection()
        except errorType:
            print(states_data.com.serial_parameters.dicionary["port"])
            states_data.CloseProgram.info = "Connection Error"
            self.next_state = "CloseProgram"

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



