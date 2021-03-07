from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# __file__ --> /basic.py
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -----------------------------------------------------
# --------------- Table Creation ----------------------
# -----------------------------------------------------
class Puppy(db.Model):

    # Manual table name choice
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Puppy {self.name} is {self.age} year/s old'


if __name__ == '__main__':
    app.run(debug=True)