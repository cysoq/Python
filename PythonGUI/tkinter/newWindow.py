from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("First Window")

def open():
    # To make a new window
    top = Toplevel() # what tkinter calls a new window
    top.title("Second Window")
    global my_img # Needs to be global for it to work
    my_img = ImageTk.PhotoImage(Image.open("Pic/red.png"))
    my_label = Label(top,image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open)
btn.pack()

mainloop()