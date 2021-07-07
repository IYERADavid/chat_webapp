import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskext.autoversion import Autoversion
from datetime import timedelta

app = Flask(__name__)
# TODO add a function to retrieve environment variables
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.autoversion = True
Autoversion(app)
app.permanent_session_lifetime = timedelta(days=30)
db = SQLAlchemy(app)
