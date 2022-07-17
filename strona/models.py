from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import datetime

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notatka = db.Column(db.String(10000))
    data = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __str__(self):
        self.notka = self.notatka[0:10]
        self.printable_date = self.data
        return f'{self.id},{self.notka}...,{self.printable_date.strftime("%Y-%m-%d, %H:%M:%S")}'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    notes = db.relationship('Note')
