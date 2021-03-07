from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class InfoForm(FlaskForm):
    breed = StringField(label='What breed are you?')
    submit = SubmitField(label='Submit')