from dis import show_code
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Drop Down")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get()).pack()
    
# Drop Down Boxes
clicked = StringVar()
clicked.set("monday")

# Will not have a default value unless set
drop = OptionMenu(root, clicked, "monday","tuesday","wednesday","thursday", "friday", "saturday", "sunday").pack()
# Can also pass in a list, but will have to put a star in front of the list name, Ex: *list

myButton = Button(root, text="show selection", command=show).pack()

root.mainloop()