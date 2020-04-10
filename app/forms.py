from flask_wtf import FlaskForm
#from wtforms import StringField, TextField, FileField, file_required, RadioFields
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired 

from wtforms import StringField 
from wtforms.fields import TextField, SelectField, RadioField,TextAreaField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import InputRequired, Email

class UploadForm(FlaskForm):
    
    firstname = TextField('First Name', validators=[InputRequired()])
    lastname = TextField('Last Name', validators=[InputRequired()])
    gender = SelectField('Gender', choices=[("None", "Select Gender"), ("Male", "Male"), ("Female", "Female")], validators=[InputRequired()])
    email = TextField('Email', validators = [InputRequired()])
    location =  TextField('Location', validators = [InputRequired()])
    biography = TextAreaField('Biography', validators=[InputRequired()])
    profilePic = FileField('Profile Picture', validators=[FileRequired(),FileAllowed(['jpg','png'], 'Images only!')])
    
    