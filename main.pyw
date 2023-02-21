# author: a5892731
# date: 11.05.2022
# last update: 21.02.2023
# version: 1.4
#
# description:
# This is a simple template for programs with Graphic User Interface

'''
imports
-tkinter: pip install tk
-PIL: pip install pillow
'''

from tkinter import Tk
from threading import Thread

from resources.state_machine.machine1.read_machine_loader import ReadUDPmachine


class ProgramRun:
    from resources.gui._gui_variables import window_variables_init, set_variable_default_values
    from resources.gui._main_window import build_main_window, update_window

    '''>>> imports used in other files connected to this class'''
    from resources.gui.windows._left_menu_label import _left_menu_bar, exit_program
    from resources.gui.windows._home_label import _home_label
    from resources.gui.windows._settings_label import _settings_label

    '''<<< imports used in other files connected to this class'''
    def __init__(self,):
        self.window = Tk()
        self.window_variables_init()
        self.set_variable_default_values()
        self.build_main_window()

        self.main_loop()

    def main_loop(self):

        device = ReadUDPmachine()

        while True:
            '''create threads'''
            threads = []
            self.update_window()


            thread = Thread(
                target=device.on_event(self, 'device_locked',)
            )
            threads.append(thread)



            '''start threads'''
            for thread in threads:
                thread.start()

            '''wait for all threads to end'''
            for thread in threads:
                thread.join()

            try:
                self.window.winfo_exists()  # if there is no window then exit program
            except:
                exit()




'''---------------------------------------START APP------------------------------------------------------------------'''
app = ProgramRun()