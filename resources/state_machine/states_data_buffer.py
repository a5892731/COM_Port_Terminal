'''import all your states here'''
'''    machine 1'''
from resources.state_machine.machine1.my_states import ReadInitialization
'''    machine 2'''
from resources.state_machine.machine2.my_states import ProgramInitialization
'''    machine 3'''
from resources.state_machine.machine3.my_states import SendInitialization

class StatesDataBuffer():
    def __init__(self):
        '''information variables'''
        self.current_state = None
        self.info = "info"


        '''init all your states here
        this class stores memory of States'''
        '''    machine 1'''
        self.ReadInitialization = ReadInitialization()

        '''    machine 2'''
        self.ProgramInitialization = ProgramInitialization()

        '''    machine 3'''
        self.SendInitialization = SendInitialization()

        '''Header'''
        self.ID = int()
        self.DLC = int()
        self.reserved0 = int()
        self.reserved1 = int()
        self.reserved2 = int()

        """Data"""
        self.variable1 = int()
        self.variable2 = float()
        self.variable3 = float()
        self.variable4 = int()
        self.variable5 = int()