# author: a5892731
# date: 03.03.2021
# last update: 30.05.2022
# version: 2.0
#
# description:
# This is a COM port terminal with Tkinter gui and stare machine in program loop.

'''
imports

-tkinter: pip install tk
-PIL: pip install pillow
-struct:

------------------------
#>>> Sources:
https://pyserial.readthedocs.io/en/latest/pyserial_api.html#serial.STOPBITS_ONE
https://docs.python.org/3/library/io.html#io.TextIOWrapper
------------------------
#>>> Libs:
import serial
------------
import io
import os
import time
'''

from tkinter import Tk
from time import time

from resources.state_machine.state_loader import StateLoader


class ProgramRun:
    from resources.gui._gui_variables import window_variables_init, set_variable_default_values, \
                                             import_variables_to_gui, export_variables_from_gui
    from resources.gui._main_window import build_main_window, update_window

    '''>>> imports used in other files connected to this class'''
    from resources.gui.labels._left_menu_label import left_menu_bar, exit_program, view_terminal_label
    from resources.gui.labels._terminal_label import terminal_label




    '''<<< imports used in other files connected to this class'''
    def __init__(self,):
        self.window = Tk()
        self.window_variables_init()
        self.set_variable_default_values()
        self.build_main_window()

        self.main_loop()

    def main_loop(self):
        device = StateLoader()

        while True:
            #start_time = time()
            self.update_window()

            device.on_event(self, 'device_locked',)  # call the state machine events

            #loop_time = time() - start_time
            #print(">>> main loop time = {}".format(loop_time))





'''---------------------------------------START APP------------------------------------------------------------------'''
app = ProgramRun()