from flask import Flask
import os
import models
from settings import app, db


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug = True, port= 8080)
