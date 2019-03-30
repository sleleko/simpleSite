from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, Unique=True)
    email = db.Column(db.String(120), index=True, Unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User> {username}'.format(username=self.username)