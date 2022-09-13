# Will specifically use the module Tkinter 
from tkinter import *
from tkmacosx import Button # This will fix the button issue where on macs bg does not do anything 


# In tkinter, everything is a widget 

root = Tk() # This is a root widget that must exist 

# A function for the button to trigger
def myClick():
    myLabel = Label(root, text="Look! I clicked a Button")
    myLabel.pack()

myButton = Button(root, text="Click Me!", padx=50, pady=50, command=myClick, fg="Green", bg='Black', highlightbackground='Grey') # Create the button, can define state such as: state="disabled"
#padx/y will determine the button, fg changes the text, bg changes the button color, highlightbackground makes a ring around the text
# Can use hex color codes: #number
myButton.pack() # throw it on the screen 

# Need an event loop for all GUIs, ends when that loop end
root.mainloop()