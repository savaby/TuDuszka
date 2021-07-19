from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/view/<int:todo>')
def view(todo):
    pass

@app.route('/add')
def add(id=None):
    pass



if __name__ == '__main__':
    app.run(debug=True)