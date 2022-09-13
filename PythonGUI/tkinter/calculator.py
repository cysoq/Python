# Will specifically use the module Tkinter 
import math
from tkinter import *
# In tkinter, everything is a widget 

root = Tk() # This is a root widget that must exist 
root.title("Simple Calculator") # how to name the GUI

# Make a text box
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10) #columnspan makes it cover several columns 

def button_click(number):
    current = e.get()
    e.delete(0, END) # Need those parameters 
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_number)
    e.delete(0, END)

def button_mult():
    first_number = e.get()
    global f_num
    global math
    math = "mult"
    f_num = int(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_number)
    e.delete(0, END)


def button_eq():
    second_number = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, f_num + int(second_number))
    elif math == "sub":
        e.insert(0, f_num - int(second_number))
    elif math == "mult":
        e.insert(0, f_num * int(second_number))
    elif math == "div":
        if int(second_number) == 0:
            e.insert(0, "Error")
            return
        e.insert(0, f_num / int(second_number))

# Define buttons 

# Will need to use Lambda to pass in parameters 
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
buttonAdd = Button(root, text="+", padx=40, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=101, pady=20, command=button_eq)
button_clear = Button(root, text="clear", padx=91, pady=20, command=button_clear)

buttonSubtract = Button(root, text="-", padx=41, pady=20, command=button_sub)
buttonMultiply = Button(root, text="*", padx=40, pady=20, command=button_mult)
buttonDivide = Button(root, text="/", padx=40, pady=20, command=button_div)

# Put buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
buttonAdd.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

buttonSubtract.grid(row=6, column=0)
buttonMultiply.grid(row=6, column=1)
buttonDivide.grid(row=6, column=2)

# Need an event loop for all GUIs, ends when that loop end
root.mainloop()