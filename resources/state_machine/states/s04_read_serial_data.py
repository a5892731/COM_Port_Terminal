class ReadSerialDataBody(object):

    def __init__(self,):
        """
        We define a state object which provides some utility functions for the
        individual states within the state machine.
        """
        self.next_state = "SendSerialData"
        self.data = ""
        self.frame = ""
        self.frames_buffer = []
        self.buffer_size = 17

    def run_state(self, states_data):
        self.frame = states_data.com.read_data()

        if self.frame != "":
            self.frames_buffer.append(self.frame)

        if len(self.frames_buffer) > self.buffer_size:
            self.frames_buffer.pop(0)

        self.data = ""
        for frame in self.frames_buffer:
            self.data += frame + "\n"
        self.data.rstrip("\n") # delete last \n item)


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



