from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("check")
root.geometry("400x400")

var = IntVar()

c = Checkbutton(root, text="Check this", variable=var, onvalue=2, offvalue=1) # Can set on and off value, though 1/0 is default
c.deselect() # This is to make sure it is not selected just in case
c.pack()

def show():
    
    myLabel = Label(root, text=var.get()).pack()

myButton = Button(root, text="show selection", command=show).pack()
root.mainloop()