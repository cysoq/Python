# Will specifically use the module Tkinter 
from tkinter import *

# In tkinter, everything is a widget 

root = Tk() # This is a root widget that must exist 

myLabel1 = Label(root, text ="Hello World!") # Creates a label Widget
myLabel2 = Label(root, text ="My Name is Noah!") # Creates a label Widget

# Will use the grid system, visual grids on the screen to understand placement 
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1) # Notice they are relative to each other 

# Need an event loop for all GUIs, ends when that loop end
root.mainloop()
