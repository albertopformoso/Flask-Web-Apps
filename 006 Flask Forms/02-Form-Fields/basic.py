from flask import (Flask, render_template, 
                   session, redirect, 
                   url_for)
from dotenv import load_dotenv, find_dotenv
import os

from forms import InfoForm

# ---- .env check ---- 
if len(find_dotenv()) == 0:
        raise RuntimeError("Can't find your .env file")

load_dotenv(find_dotenv())
# --------------------

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/', methods=['GET', 'POST'])
def index():
    breed = False

    form = InfoForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))
    
    return render_template('index.html', 
                            form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)
    
