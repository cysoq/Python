# Will specifically use the module Tkinter 
from tkinter import *
from tkmacosx import Button # This will fix the button issue where on macs bg does not do anything 


# In tkinter, everything is a widget 

root = Tk() # This is a root widget that must exist 

# Make a text box
e = Entry(root, width=50, bg="blue", fg="white", borderwidth=5)
e.pack()
e.get() # Returns the string typed in the entry  
e.insert(0, "Enter you name") # Will make default text in the text box

# A function for the button to trigger, In this case will return what is in the Entry
def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

myButton = Button(root, text="Enter Your Name!", padx=50, pady=50, command=myClick, fg="Green", bg='Black', highlightbackground='Grey') # Create the button, can define state such as: state="disabled"
#padx/y will determine the button, fg changes the text, bg changes the button color, highlightbackground makes a ring around the text
# Can use hex color codes: #number
myButton.pack() # throw it on the screen 

# Need an event loop for all GUIs, ends when that loop end
root.mainloop()