from flask_wtf import FlaskForm 
from wtforms import TextField, PasswordField, StringField, SelectField, TextAreaField, validators
from wtforms.fields.html5 import EmailField 
from flask_wtf.file import FileField, FileAllowed, FileRequired
from datetime import date
from wtforms.fields.html5 import DateField
from wtforms.fields.html5 import DateTimeField
from wtforms.validators import InputRequired

class RegistrationForm(FlaskForm):
    firstname = TextField('First Name', validators= [InputRequired()])
    lastname = TextField('Last Name', validators= [InputRequired()])
    username = StringField('Username', validators= [InputRequired()])
    dob = DateField('Date of Birth', default= date.today)
    profile_img = FileField('Profile Picture', validators= [FileRequired(), FileAllowed(['jpg','png'], 'Images Only!')])
    password = PasswordField('Password', validators= [InputRequired()])
    
class LoginForm(FlaskForm):
    username = StringField(validators= [InputRequired()])
    password = PasswordField('Password', validators= [InputRequired()])
    

class Dashboard(FlaskForm):
    selectionOS = SelectField("Select your operating system below", choices = [('Windows','Windows'),('MacOs','MacOs')])
    search = StringField("Search")
    
class ContactForm(FlaskForm):
    email = EmailField('Email', validators= [InputRequired()])
    subject = TextField('Subject', validators = [InputRequired()])
    message = TextAreaField('Message', validators = [InputRequired()])
