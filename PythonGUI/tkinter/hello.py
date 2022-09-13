# Will specifically use the module Tkinter 
from tkinter import *

# In tkinter, everything is a widget 

root = Tk() # This is a root widget that must exist 

myLabel = Label(root, text ="Hello World!") # Creates a label Widget

# Pack is one of several ways to put text, think of it as putting it in the first available spot
myLabel.pack() # Shoved on the screen 

# Need an event loop for all GUIs, ends when that loop end
root.mainloop()
