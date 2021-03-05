from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    mylist = [f'Element {i}' for i in range(1, 6)]

    user_logged_in = True

    return render_template('03_basic.html', mylist=mylist,
                            user_logged_in=user_logged_in)

if __name__ == '__main__':
    app.run(debug=True)