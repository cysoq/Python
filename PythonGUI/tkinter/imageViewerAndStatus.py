from ast import Lambda
import re
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn To Code at Codemy.com")

##########################################################################################
# Make my Image viewer
##########################################################################################
myImg1 = ImageTk.PhotoImage(Image.open("Pic/Blue.png"))
myImg2 = ImageTk.PhotoImage(Image.open("Pic/Green.png"))
myImg3 = ImageTk.PhotoImage(Image.open("Pic/Orange.png"))
myImg4 = ImageTk.PhotoImage(Image.open("Pic/Purple.png"))
myImg5 = ImageTk.PhotoImage(Image.open("Pic/Red.png"))

imageList = [myImg1,myImg2,myImg3,myImg4,myImg5]

ListNum = 0

myLabel = Label(image=imageList[ListNum])
myLabel.grid(row=0, column=0, columnspan=3)

# Add my initial status
# Gives it a border and makes it sunken, also anchor it east or left
status = Label(root, text="Image 1 of " + str(len(imageList)), bd=1, relief=SUNKEN, anchor=E) 
status.grid(row=2, column=0, columnspan=3, sticky=W+E) # sticky tells it to stretch, in this case West and East


def forward():
    global ListNum
    global myLabel
    ListNum = ListNum + 1
    if ListNum >= len(imageList):
        ListNum = 0
    
    myLabel.grid_forget()
    myLabel = Label(image=imageList[ListNum])
    myLabel.grid(row=0, column=0, columnspan=3)
    
    # update status
    global status
    
    status.grid_forget()
    status = Label(root, text="Image " + str(ListNum+1) + " of " + str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
    # If we dont want it to loop back at the end can, instead use this if statement 
    # WILL DISABLE THE BUTTON AT THE END
    #    if ListNum >= len(imageList):
    #       buttonForward = Button(root, text=">>", state=DISABLED)
    #       return
    
def back():
    global ListNum
    global myLabel
    ListNum = ListNum - 1
    if ListNum < 0:
        ListNum = len(imageList) -1
    
    myLabel.grid_forget()
    myLabel = Label(image=imageList[ListNum])
    myLabel.grid(row=0, column=0, columnspan=3)
    
    # update status
    global status
    
    status.grid_forget()
    status = Label(root, text="Image " + str(ListNum+1) + " of " + str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

buttonBack =  Button(root, text="<<", command=back)
buttonExit = Button(root, text="Exit Program", command=root.quit)
buttonForward = Button(root, text=">>", command=forward)

buttonBack.grid(row=1, column=0)
buttonExit.grid(row=1, column=1)
buttonForward.grid(row=1, column=2)

##########################################################################################
# Add Status Bar
##########################################################################################


root.mainloop()