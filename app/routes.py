from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegisterForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/home')
# @login_required
def home():
    return render_template('index.html', title='Главная')


@app.route('/contacts')
def contactme():
    return render_template('contacts.html', title='Связаться со мной')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or user.check_password(form.password.data):
            flash('Вход под пользователем {username}, галка запомнить меня {remember_me}'.format(
                username=form.username.data, remember_me=form.remember_me.data))
            return redirect(url_for('login'))
        # action login user
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(url_for('home'))

    return render_template('login.html', title="Вход", form=form)


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Пользователь успешно зарегистрирован!")
        return redirect(url_for('login'))
    return render_template('register.html', title='Регистрация нового пользователя', form=form)


@app.route('/users/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    content = [
        {'user': user, 'content': 'test content'}
    ]
    return render_template('user.html', user=user, content=content)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


'''
@app.route('/portfolio', methods=['GET', 'POST'])
def example():
    return "Example return content for anonymous user"
'''


@app.route('/portfolio')
@login_required
def portfolio():
    return render_template('portfolio.html')