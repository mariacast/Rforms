from flask import Flask
from settings import db
from flask_sqlalchemy import SQLAlchemy
import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://semusr:12345@localhost/radiusforms'
db = SQLAlchemy(app)

class Form(db.Model):
    __tablename__ = 'form'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    create = db.Column(db.DateTime, default=datetime.datetime.now)
    estatus = db.Column(db.String(1))
    detail = db.Column(db.Text)
    fields = db.relationship('Field')


class Field(db.Model):
    __tablename__ = 'field'
    id = db.Column(db.Integer, primary_key=True)
    form_id = db.Column(db.Integer,db.ForeignKey('form.id'))
    name = db.Column(db.String(50))
    tipe = db.Column(db.String(50))
    label = db.Column(db.String(100))
    detail = db.Column(db.Text)
    answers = db.relationship('Answer')

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial = db.Column(db.Integer())
    field_id = db.Column(db.Integer,db.ForeignKey('field.id'))
    data = db.Column(db.Text)
