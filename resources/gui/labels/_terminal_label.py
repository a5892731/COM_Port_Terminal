from resources.gui.widgets.checkbox import checkbox
from resources.gui.widgets.button import button
from resources.gui.widgets.labelframe import labelframe
from resources.gui.widgets.label import label
from resources.gui.widgets.entry import entry
from resources.gui.functions.import_image import import_image
from resources.gui.widgets.label_image import label_image

from tkinter import LEFT

def terminal_label(self):

    def configure_central_label(window_width, window_height):
        '''configure main label'''
        self.main_label.columnconfigure(0, minsize=int(window_width))
        label(label=self.main_label, column=0, row=0, text="COM Terminal", columnspan=1)
        self.main_label.rowconfigure(1, minsize=int(window_height * 1/4 ))
        self.main_label.rowconfigure(2, minsize=int(window_height * 3/4 ))

    def configure_upper_label(window_width):
        upper_label = labelframe(label= self.main_label, column = 0, row = 1, text = "Serial Transmission:")
        columns = 10

        for column_nr in range(columns):
            upper_label.columnconfigure(column_nr, minsize=int(window_width / columns))

        label(label=upper_label, column=0, row=1, text="Znaki do wysłania", columnspan = 1)
        entry(label=upper_label, text=self.send_string, column=0, row=2, width=60, columnspan=6)
        button(label=upper_label, text= "Wyślij", command=send_serial, column=7, row=2, width=12)

    def configure_lower_label(window_width):
        lower_label = labelframe(label= self.main_label, column = 0, row = 2, text = "Serial Receive:")

        self.com_receive_label = label(label=lower_label, column=0, row=0, text=self.receive_string, justify=LEFT)



    '''----------------------------------------------BUTTONS----------------------------------------------------->>>>'''
    def send_serial():
        self.com_data_send_button = True
        print("send_serial")



    '''----------------------------------------------BUTTONS-----------------------------------------------------<<<<'''



    '''--------------------------------------------------------------------------------------------------------------'''
    window_width = 1048
    window_height = 554
    configure_central_label(window_width, window_height)
    configure_upper_label(window_width, )
    configure_lower_label(window_width, )




