from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Slider")

# sliders are refereed to as Scale(), default up and down
vertical = Scale(root,from_=0, to=200)
vertical.pack()

root.geometry("400x400") # Designate size of window

def slide(var):
    global myLabel
    myLabel = Label(text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400") # Can resize the window!, to touchy though if passed in from th slider
    return

horizontal = Scale(root,from_=0, to=200, orient=HORIZONTAL) # command=slide to make to auto update
horizontal.pack()

myLabel = Label(text=horizontal.get()).pack()

my_btn = Button(root, text="click", command=slide).pack()

root.mainloop()