from flask import Flask

app = Flask(__name__)

@app.route('/')  # 127.0.0.1:5000
def index():
    return '<h1>Hello World!</h1>'

@app.route('/information')  # 127.0.0.1:5000/information
def info():
    return '<h1>Info page</h1>'

@app.route('/puppy/<name>')
def puppy(name):
    return f"<h1>100th letter <em>{name[100]}</em></h1>"


if __name__ == '__main__':
    app.run(debug=True)