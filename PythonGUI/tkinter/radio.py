# Used for forms

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn To Code at Codemy.com")

# Need to declare the variable 
r = IntVar()
r.set(0) # Remember that tkiner variables need to be set and get

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()
    
# Loop method
MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese" ),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)
    

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

# Can do the same thing with a button 

myLabel = Label(root, text=r.get())
myLabel.pack()
root.mainloop()