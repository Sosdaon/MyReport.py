# 5
from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = ['Щоденник', 'Журнал реєстрації', "Паспорт пам'ятки"]


@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='Назва сторінки', menu=menu)


@app.route('/profile/<user_name>')
def profile(user_name):
    return f'Користувач: {user_name}'


if __name__ == '__main__':
    app.run(debug=True)
