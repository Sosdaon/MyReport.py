# 9
import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
from FDataBase import FDataBase

DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'fdgdfgdfggf786hfg6hfg6h7f'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path,'flsite,db')))

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

@app.route('/')
def index():
    db = get_db()
    dbase = FDataBase(db)
    print(url_for('index'))
    return render_template('index.html', menu=dbase.getMenu(), title='Головна')

@app.route('/add_post', methods=['POST', 'GET'])
def addPost():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['post'])
            if not res:
                flash('Виникла, помилка публікування статті', category='error')
            else:
                flash('Стаття успішно опублікована', category='success')
        else:
            flash('Назва статті має бути не менш ніж чотири символи.', category='error')
    return render_template('add_post.html', menu=dbase.getMenu(), title='Публікація')

@app.route('/post/<int:id_post>')
def showPost(id_post):
    db = get_db()
    dbase = FDataBase(db)
    title, post = dbase.getPost(id_post)
    if not title:
        abort(404)

    return render_template('post.html', menu=dbase.getMenu(), title=title, post=post)

@app.route('/about_us')
def about_us():
    db = get_db()
    dbase = FDataBase(db)
    print(url_for('about_us'))
    return render_template('about.html', menu=dbase.getMenu(), title='Про нас')

@app.errorhandler(404)
def pageNotFound(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('page404.html', menu=dbase.getMenu(), title='Не знайдено'), 404

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        if len(request.form['user_name']) > 2:
            flash('Ваше повідомлення відправлено. Ми вдосконалюємося.', category='success')
        else:
            flash('На жаль, виникла помилка відправлення', category='error')

    return render_template('contact.html', menu=dbase.getMenu(), title='Повідомити')

if __name__ == '__main__':
    app.run(debug=True)