import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://semusr:12345@localhost/radiusforms'
db = SQLAlchemy(app)                           
