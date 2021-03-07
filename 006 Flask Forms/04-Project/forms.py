from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField)
from wtforms.validators import DataRequired

class SimpleForm(FlaskForm):
    breed = StringField(label='What breed are you?')
    submit = SubmitField(label='Submit')