import os
import sys


basedir = os.path.abspath(os.path.dirname(__file__))
#basedir = sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'venv/Lib/python3.7/site-packages'))


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'FS$GK$Grg45339'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False