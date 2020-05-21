from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, SelectField, IntegerField, SelectMultipleField, BooleanField
from wtforms.validators import DataRequired, Length, InputRequired, Email
from wtforms.widgets import TextArea
from wtforms.fields.html5 import EmailField
#this is thhe form that handles the parameters for mood quiz request
class messageForm(FlaskForm):
    email = EmailField('Email Address', validators =[DataRequired(), Email()])
    name = StringField("Name", validators=[DataRequired()])
    message = StringField('message',validators=[DataRequired()],widget=TextArea())
    submit = SubmitField('Submit')

