from tkinter import *
'''------------------------------------------------------------------------------------------------------------------'''
def window_variables_init(self):
    def gui_mechanism_variables():
        self.window_width = 0
        self.window_height = 0
        self.tab_name = ""

    def support_variables():
        self.int_var_type = IntVar()
        self.string_var_type = StringVar()

    def serial_variables():
        self.receive_string = ""
        self.com_receive_label = None
        self.send_string = StringVar()
        self.com_data_send_button = False

    #----------------------------------------------------------------------
    gui_mechanism_variables()
    serial_variables()

'''------------------------------------------------------------------------------------------------------------------'''
def set_variable_default_values(self):
    def gui_mechanism_variables():
        self.window_width = self.window.winfo_screenwidth()
        self.window_height = self.window.winfo_screenheight() - 30
        self.tab_name = "Terminal"
    def serial_variables():
        self.receive_string = ""

    #----------------------------------------------------------------------
    gui_mechanism_variables()
    serial_variables()


def import_variables_to_gui(self, state_machine_variables):
    '''this function is prepared to import data to gui from state machine'''

    def terminal(state_machine_variables):
        self.receive_string = state_machine_variables.ReadSerialData.data
        self.com_receive_label.config(text=self.receive_string)   # error in another labels active
        self.com_data_send_button = state_machine_variables.SendSerialData.com_data_send_button # reset button

    #----------------------------------------------------------------------
    if self.tab_name == "Terminal":
        terminal(state_machine_variables)

def export_variables_from_gui(self, state_machine_variables):
    '''this function is prepared to export data from gui to state machine'''
    def terminal(state_machine_variables):
        state_machine_variables.SendSerialData.com_data_send_button = self.com_data_send_button # button click
        state_machine_variables.SendSerialData.data = self.send_string.get()

        #----------------------------------------------------------------------
    if self.tab_name == "Terminal":
        terminal(state_machine_variables)