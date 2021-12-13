# 8
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'

menu = [{'name': 'Щоденник', 'url': 'diary'},
        {'name': 'Журнал реєстрації', 'url': 'registration_book'},
        {'name': "Паспорт пам'ятки", 'url': 'passport'},
        {'name': 'Повідомити про проблему', 'url': 'contact'}]


@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', title='Головна', menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='Про нас', menu=menu)


@app.route('/profile/<user_name>')
def profile(user_name):
    if 'userLogged' not in session or session['userLogged'] != user_name:
        abort(401)

    return f'Користувач: {user_name}'

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['user_name']) > 2:
            flash('Ваше повідомлення відправлено. Ми вдосконалюємося.', category='success')
        else:
            flash('На жаль, виникла помилка відправлення', category='error')

    return render_template('contact.html', title='Повідомити', menu=menu)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', user_name=session['userLogged']))
    elif request.method == 'POST' and request.form['user_name'] == 'Радченко Степан' and request.form['psw'] == '1928':
        session['userLogged'] = request.form['user_name']
        return redirect(url_for('profile', user_name=session['userLogged']))

    return render_template('login.html', title='Авторизація', menu=menu)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title='Не знайдено'), 404


if __name__ == '__main__':
    app.run(debug=True)
