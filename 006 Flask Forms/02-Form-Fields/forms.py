from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, 
                     DateTimeField, RadioField, SelectField, 
                     TextField, TextAreaField)
from wtforms.validators import DataRequired

class InfoForm(FlaskForm):
    breed = StringField(
        label='What breed are you?',
        validators=[
            DataRequired(message='Please fill this field')
        ]
    )
    neutered = BooleanField(label='Have you been neutered?')

    mood = RadioField(
        label='Please choose your mood:',
        choices=[
            ('mood_one', 'Happy'),
            ('mood_two', 'Excited')
        ]
    )

    food_choice = SelectField(
        label=u'Pick your favorite food:',
        choices=[
            ('chi', 'Chicken'),
            ('bf', 'Beef'),
            ('fish', 'Fish')
        ]
    )

    feedback = TextAreaField()
    submit = SubmitField(label='Submit')