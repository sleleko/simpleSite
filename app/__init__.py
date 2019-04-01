from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
# Don't forget change it!!
app.config['SECRET_KEY'] = 'mysupersecret'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models





