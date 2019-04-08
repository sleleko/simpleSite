from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная')


@app.route('/about')
def about():
    return render_template('about.html', title='Обо мне')


@app.route('/contacts')
def contactme():
    return render_template('contacts.html', title='Связаться со мной')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or user.check_password(form.password.data):
            flash('Вход под пользователем {username}, галка запомнить меня {remember_me}'.format(
                username=form.username.data, remember_me=form.remember_me.data))
            return redirect(url_for('login'))
        # action login user
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', title="Вход", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/example', methods=['GET', 'POST'])
def example():
    return "Example return content for anonymous user"


@app.route('/example2')
@login_required
def example2():
    return "Example return content for auth users only"