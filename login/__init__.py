import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
gestor = LoginManager()

app.config['SECRET_KEY'] = 'clavesecreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir,'login.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

gestor.init_app(app)
gestor.login_view = 'login'