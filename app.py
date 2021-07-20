from flask import Flask, g, request, url_for, redirect, jsonify
from flask.templating import render_template
from db import get_db
import datetime

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'connection'):
        g.connection.close()


@app.route('/')
def home():
    db = get_db()
    cur = db.execute('select todo.id, todo.title, todo.create_date, todo.todo_text, types.name, todo.end_date from todo join types on todo.type_id = types.id order by todo.create_date desc')
    todos = cur.fetchall()
    return render_template('index.html', todos=todos)

@app.route('/view/<int:id>')
def view(id):
    db = get_db()
    cur = db.execute('select todo.id, todo.title, todo.create_date, todo.end_date, todo.todo_text, types.name from todo join types on todo.type_id = types.id where todo.id = ?', [id])
    todo = cur.fetchone()
    return render_template('view.html', todo=todo )

@app.route('/add', methods=["POST", "GET"])
def add():
    db = get_db()
    cur = db.execute('select * from types order by id')
    types = cur.fetchall()
    if request.method == "POST":
        title = request.form['todo-title']
        text = request.form['todo-text']
        type_id = request.form['todo-type']
        create_date = datetime.date.today()
        db.execute('insert into todo(title, type_id, todo_text, create_date) values(?,?,?,?)', [title, type_id, text, create_date])
        db.commit()
        return redirect('/')
    return render_template('add.html', types=types)
    
@app.route('/done', methods=['POST'])
def done():
    db = get_db()
    id = request.form['thisId']
    end_date = datetime.date.today()
    db.execute('update todo set end_date = ? where id = ?', [end_date, id])
    db.commit()
    return redirect(request.referrer)


@app.route('/delete', methods=['POST'])
def delete():
    db = get_db()
    id = request.form['thisId']
    end_date = datetime.date.today()
    db.execute('delete from todo where todo.id = ?', [id])
    db.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)