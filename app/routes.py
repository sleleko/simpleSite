from flask import render_template
from flask import flash
from flask import redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная')

@app.route('/about')
def about():
    return  render_template('about.html', title='Обо мне')

@app.route('/contacts')
def contactme():
    return render_template('contacts.html', title='Связаться со мной')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Вход под пользователем {username}, галка запомнить меня {remember_me}'.format(
            username=form.username.data, remember_me=form.remember_me.data
        ))
        return redirect('/index')
    return render_template('login.html', title="Вход", form=form)