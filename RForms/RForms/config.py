from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from models import db
from models import Form
from models import Field
from models import Answer
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.attributes import flag_modified
from templates import*


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://semusr:12345@localhost/radiusforms'
db = SQLAlchemy(app)
