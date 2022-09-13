# Need a pip installed mysql connector to make a database with python 
    # pip install mysql-connector-python
    
# for it to work with flask will also need to:
    # pip install cryptography 
    # pip install pymysql

# Will also need to import the database to whatever flask py is using in this case "hello"
    # from hello import db
    # db.create_all()
    
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd='4196Village')

my_cursor = mydb.cursor() # automated program to interface with the database

# SHOULD UNCOMMENT THIS IF NEED TO MAKE A NEW DATABASE
# my_cursor.execute("Create Database our_users") # how to make it 

# Print to terminal evidence that it was created
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

