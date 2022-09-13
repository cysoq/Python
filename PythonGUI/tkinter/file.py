from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Open Files Dialog Box")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/Users/noahsoqui", title="Select file,", filetypes=(("png files","*.png"),("All files", "*.*"),))# Will return the location, and then can open it
    myLabel = Label(root, text=root.filename).pack() # Displays the location
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    myLabel = Label(root,image=my_image).pack()
    
bybtn = Button(root, text="Open File", command=open).pack()
root.mainloop()
