from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная')

@app.route('/about')
def about():
    return  render_template('about.html', title='Обо мне')