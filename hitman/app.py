from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_oauthlib.client import OAuth
from .util.config import config

app = Flask(__name__)

uri = '{driver}{user}:{password}@{path}'.format(**config.storage._asdict())
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = config.crypto.key
app.config['SERVER_NAME'] = config.http.name

# create Database
db = SQLAlchemy(app)
oauth = OAuth(app)

from .api.auth import auth_app
app.register_blueprint(auth_app, url_prefix = '/auth')

from .api.slack import slack_app
app.register_blueprint(slack_app, url_prefix = '/slack')

