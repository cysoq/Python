from flask import Flask, render_template, flash 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create a Flask Instance
app = Flask(__name__, template_folder='template')

# Add Database
# OLD SQLite DB:
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# New MySQL DB
# Should be like so: `mysql://username:password@localhost/db_name` # where local host can eventually be a URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:4196Village@localhost/our_users'

# Secret Key!
app.config['SECRET_KEY'] = "secret key that no one should know" # need a secret key CSRF (Cross Site Request Forgery)



# Initialize The Database 
# Will also need to go into terminal, go into python3 shell, and do: >>> from hello import db (because this file is called hello)
# In that python terminal will then run: >>> db.create_all() to make the db
db = SQLAlchemy(app)
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Create A String 
    def __repr__(self):
        return '<Name %r>' % self.name

class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")



# FILTERS:
# safe - by default, flask will ignore html, can use safe so you can pass it in 
# capitalize - first  word will be cap
# lower - all lower
# upper - all upper
# title - capitalize each first letter
# trim - remove spaces at the end
# striptags - Wont ignore HTML tags, will remove them
# Many more filters shown in documentation 

# for web form, use WTF! (What the forms!) with $ pip install flask-wtf
# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()]) # What it will show, and the validator function (will make you fill out the form)
    submit = SubmitField("Submit")
    
    ## Fields:
	# BooleanField
	# DateField
	# DateTimeField
	# DecimalField
	# FileField
	# HiddenField
	# MultipleField
	# FieldList
	# FloatField
	# FormField
	# IntegerField
	# PasswordField
	# RadioField
	# SelectField
	# SelectMultipleField
	# SubmitField
	# StringField
	# TextAreaField

	## Validators:
	# DataRequired
	# Email
	# EqualTo
	# InputRequired
	# IPAddress
	# Length
	# MacAddress
	# NumberRange
	# Optional
	# Regexp
	# URL
	# UUID
	# AnyOf
	# NoneOf

@app.route('/user/add', methods=["GET", "POST"])
def add_user():
	name =  None
	form = UserForm()
	if form.validate_on_submit():
		# want a unique email
		user = Users.query.filter_by(email=form.email.data).first() # should be none
		if user is None: # that means its a new user that can be added
			user = Users(name=form.name.data, email=form.email.data) # make the user
			db.session.add(user) # add the user
			db.session.commit() # commit the user	
		
		name = form.name.data
		form.name.data = ""
		form.email.data = ""
		flash("User Added Sucessfully")
	our_users = Users.query.order_by(Users.date_added) # returns everything in the database
	return render_template("add_user.html", form=form, name=name, our_users=our_users)

# Create a route decorator 
@app.route('/') # / is the root route 

def index():
#     return "<h1>Hello World!<h1>" # Simple start
    first_name= "John"
    stuff= "This is bold text"
    
    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template("index.html", 
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)


# localhost:5000/user/John
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name) #pass in the variable name as user_name

# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

# Create Name Page
@app.route('/name', methods=['GET','POST'])
def name():
    name= None
    form= NamerForm()
    # Validate Form
    if form.validate_on_submit(): # Clears the name variable on submit
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully!") # dont need to put in render template, will need to update the html though
        
    return render_template("name.html", 
                           name=name, 
                           form=form)




'''
How to run:
in terminal:
$ export FLASK_ENV=development
$ export FLASK_APP=NAME.py
$ flask run
You can now copy that link into a browser
'''