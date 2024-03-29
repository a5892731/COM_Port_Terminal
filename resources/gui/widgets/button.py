from tkinter import Button, ACTIVE, DISABLED

'''
https://www.tutorialspoint.com/python/tk_button.htm
'''

def button(label, text, command,  column = 0, row = 0, width= 12, columnspan = 1, state = ACTIVE,
           font=("Arial", 12, "bold"), sticky="WENS"):
    button = Button(label, font=font, text=text, width=width, state=state, command=command)
    button.grid(column=column, row=row, columnspan=columnspan, sticky=sticky)
    return button