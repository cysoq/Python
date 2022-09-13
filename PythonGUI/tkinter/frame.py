from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn To Code at Codemy.com")

# A frame is a box to keep things orginized 

frame = LabelFrame(root, text="This is my frame...", padx=5, pady=5) # padding is inside the frame
frame.pack(padx=100, pady=100) # padding is on the outside of the Frame

b = Button(frame, text="Dont click here") # Can grid inside a frame
b2 = Button(frame, text="Dont click here")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

# A frame with no name might look cleaner
# frame2 = LabelFrame(root, padx=5, pady=5) # padding is inside the frame
# frame2.pack(padx=100, pady=100) # padding is on the outside of the Frame

root.mainloop()