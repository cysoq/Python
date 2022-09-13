from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn To Code at Codemy.com")

# Still not displaying the image right, but it gets the closest
root.iconbitmap("/Users/noahsoqui/Documents/GitHub/Cysoq/Python/PythonGUI/Pic/ps_apple_logo.icns")

# First define image, put them in something, display the thing
myImg = ImageTk.PhotoImage(Image.open("Pic/test.png"))
my_label = Label(image=myImg)
my_label.pack()


# Another button to quit the program
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.pack()

root.mainloop()