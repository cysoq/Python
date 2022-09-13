from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Learn To Code at Codemy.com")

# All message boxes: showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.showinfo("This is my Popup!", "Hello World!") # Header, then text, Simply shows text
    # Can now print out the response and make a if/else statement based on it. Most of them are 0 or 1, meaning true or false
    print(response)

Button(root, text="Popup", command=popup).pack()

root.mainloop()