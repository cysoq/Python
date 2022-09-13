from tkinter import *
from PIL import ImageTk, Image
import sqlite3

# Can learn more with https://www.youtube.com/watch?v=byHcYRpMgI4

root = Tk()
root.title("Database")

# Databases, SQLite3 comes with python! not very powerful, but easy to learn mySQL after 
# Create a database or connect to one
# conn = sqlite3.connect('address_book.db')

# # Create a cursor, which is used to do commands       Will need to do this inside each function
# c = conn.cursor()

# Will need to create a table and designate a columns, commented out because we dont need to create it every time

# c.execute(
# '''CREATE TABLE addresses(
# first_name text,
# last_name text,
# Res_Address text,
# city text,
# US_State text,
# zipcode integer
# ) ''')

# Add columns within the TableName()
# Five data types: Text=string, integers=ints, real=floats, null=does not exist, blob=image/video/etc

def update():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create a cursor, which is used to do commands
    c = conn.cursor()
    
    global f_name_edit
    global l_name_edit
    global addr_edit
    global city_edit
    global state_edit
    global zip_edit
    
    record_id = del_box.get()
    
    c.execute(
    '''UPDATE addresses SET
    first_name = :first,
    last_name = :last,
    Res_Address = :address,
    city = :city,
    US_State = :state,
    zipcode = :zip    
    
    where oid = :oid''',
    {'first': f_name_edit.get(),
     'last': l_name_edit.get(),
     'address': addr_edit.get(),
     'city': city_edit.get(),
     'state': state_edit.get(),
     'zip': zip_edit.get(),
     'oid': record_id
    })
    
    conn.commit()
    conn.close()
    
    editor.destroy()

# Create Edit
def edit():
    global editor
    editor = Tk()
    editor.title("Update a record")
    
    global f_name_edit
    global l_name_edit
    global addr_edit
    global city_edit
    global state_edit
    global zip_edit
    
    # Create Text Boxes
    f_name_edit = Entry(editor, width=30)
    f_name_edit.grid(row=0, column=1, padx=20)

    l_name_edit = Entry(editor, width=30)
    l_name_edit.grid(row=1, column=1, padx=20)

    addr_edit = Entry(editor, width=30)
    addr_edit.grid(row=2, column=1, padx=20)

    city_edit = Entry(editor, width=30)
    city_edit.grid(row=3, column=1, padx=20)

    state_edit = Entry(editor, width=30)
    state_edit.grid(row=4, column=1, padx=20)

    zip_edit = Entry(editor, width=30)
    zip_edit.grid(row=5, column=1, padx=20)

    # Create Text Box Labels
    f_name_Label = Label(editor, text= "First Name")
    f_name_Label.grid(row=0, column=0, padx=20)

    l_name_Label = Label(editor, text= "Last Name")
    l_name_Label.grid(row=1, column=0, padx=20)

    addr_Label = Label(editor, text= "Address")
    addr_Label.grid(row=2, column=0, padx=20)

    city_Label = Label(editor, text= "City")
    city_Label.grid(row=3, column=0, padx=20)

    state_Label = Label(editor, text= "State")
    state_Label.grid(row=4, column=0, padx=20)

    zip_Label = Label(editor, text= "Zip Code")
    zip_Label.grid(row=5, column=0, padx=20)
    
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create a cursor, which is used to do commands
    c = conn.cursor()

    record_id = del_box.get()

    c.execute("SELECT * FROM addresses WHERE oid= " + str(record_id))
    records = c.fetchall()
    
    for record in records:
        f_name_edit.insert(0, record[0])
        l_name_edit.insert(0, record[1])
        addr_edit.insert(0, record[2])
        city_edit.insert(0, record[3])
        state_edit.insert(0, record[4])
        zip_edit.insert(0, record[5])
        
    # Create Save Button 
    Save = Button(editor, text="Save", command=update)
    Save.grid(row=6, column =0, columnspan=2, pady=10, padx=10, ipadx =160) #ipax will strech it 
    
    conn.commit()
    conn.close()

    
    
# Create Function to Delete A Record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create a cursor, which is used to do commands
    c = conn.cursor()
    
    # Delete a record 
    c.execute("DELETE from addresses WHERE oid=" + del_box.get())
    conn.commit()
    conn.close()
    
    del_box.delete(0, END)


# Create submit funtion For database
def submit():
    
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create a cursor, which is used to do commands
    c = conn.cursor()
    
    c.execute("INSERT INTO addresses VALUES(:first_name, :last_name, :Res_Address, :city, :US_State, :zipcode)",
              {
                    'first_name': f_name.get(),
                    'last_name': l_name.get(),
                    'Res_Address': addr.get(),
                    'city': city.get(),
                    'US_State': state.get(),
                    'zipcode': zip.get()
              })
    
    conn.commit()
    conn.close()
    
    f_name.delete(0, END)
    l_name.delete(0, END)
    addr.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zip.delete(0, END)
    
# Create query
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create a cursor, which is used to do commands
    c = conn.cursor()
    
    #Query the database, oid is the primary key so you can select certain records
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall() # can also do fetchmany or fetchone
    print_records =""
    for record in records:
        print_records += str(record) +  "\n"
        
    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)
    
    conn.commit()
    conn.close()
    
# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

addr = Entry(root, width=30)
addr.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zip = Entry(root, width=30)
zip.grid(row=5, column=1, padx=20)

# Create Text Box Labels
f_name_Label = Label(root, text= "First Name")
f_name_Label.grid(row=0, column=0, padx=20)

l_name_Label = Label(root, text= "Last Name")
l_name_Label.grid(row=1, column=0, padx=20)

addr_Label = Label(root, text= "Address")
addr_Label.grid(row=2, column=0, padx=20)

city_Label = Label(root, text= "City")
city_Label.grid(row=3, column=0, padx=20)

state_Label = Label(root, text= "State")
state_Label.grid(row=4, column=0, padx=20)

zip_Label = Label(root, text= "Zip Code")
zip_Label.grid(row=5, column=0, padx=20)

# Create Submit Button 
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column =0, columnspan=2, pady=10, padx=10, ipadx =100) #ipax will strech it 

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=132)

# Create Delete Button 
del_box = Entry(root, width= 30)
del_box.grid(row=9, column =1)
sel_label = Label(root, text="Select ID", width= 30)
sel_label.grid(row=9, column =0)
del_btn = Button(root, text="Delete", command=delete)
del_btn.grid(row=10, column =0, columnspan=2, pady=10, padx=10, ipadx =156) #ipax will strech it 

# Create an Update button 
del_btn = Button(root, text="Edit Record", command=edit)
del_btn.grid(row=11, column =0, columnspan=2, pady=10, padx=10, ipadx =141) #ipax will strech it 


# To commit changes to the database, and close the connection 
# conn.commit()
# conn.close()


root.mainloop()