from flask import (Flask, render_template, 
                   session, redirect, 
                   url_for, flash)
from dotenv import load_dotenv, find_dotenv
import os

from forms import SimpleForm

# ---- .env check ---- 
if len(find_dotenv()) == 0:
        raise RuntimeError("Can't find your .env file")

load_dotenv(find_dotenv())
# --------------------

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = SimpleForm()

    if form.validate_on_submit():
        flash('You just clicked the button!')

        return redirect(url_for('index'))
    
    return render_template('index.html', 
                            form=form)


if __name__ == '__main__':
    app.run(debug=True)
    
