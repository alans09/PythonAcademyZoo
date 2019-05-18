from flask_sqlalchemy import SQLAlchemy
import flask
import os


app = flask.Flask("ZOO")
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database//database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)