from . import db
from flask_login import UserMixin


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data =


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))