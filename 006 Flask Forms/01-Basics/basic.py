from flask import Flask, render_template
from dotenv import load_dotenv, find_dotenv
import os

from my_form import InfoForm



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
        breed = form.breed.data
        form.breed.data = ''

    return render_template('index.html', 
                            form=form,
                            breed=breed)

if __name__ == '__main__':
    app.run(debug=True)
    
