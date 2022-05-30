class SendSerialDataBody(object):

    def __init__(self,):
        """
        We define a state object which provides some utility functions for the
        individual states within the state machine.
        """
        self.next_state = "ReadSerialData"
        self.data = ""
        self.frame = ""
        self.com_data_send_button = False


    def run_state(self, states_data):
        if self.com_data_send_button == True:
            self.com_data_send_button = False
            print(self.data)
            states_data.com.send_data(self.data)


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



