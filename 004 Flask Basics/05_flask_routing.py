from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')  # 127.0.0.1:5000
def index():
    return f'<h1>Go to /puppy_name/name and see the result!</h1>'

@app.route('/puppy_name/<name>')
def puppylatin(name):
    pupname = ''

    if name[-1] == 'y':
        pupname = name[:-1] + 'iful'
    else:
        pupname = name + 'y'
    
    return f"<h1> Hi {name}! Your puppy latin name is: {pupname.capitalize()}</h1>"


if __name__ == '__main__':
    app.run(debug=True)