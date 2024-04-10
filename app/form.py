from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,FileField,HiddenField,PasswordField

class Creating_Steg(FlaskForm):
    file=FileField("File")
    message=StringField("Message")
    submit=SubmitField("Submit")

class Getting_Message(FlaskForm):
    file=FileField("File")
    key=StringField("Key")
    Submit2=SubmitField("Submit")