from flask import render_template
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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Вход", form=form)