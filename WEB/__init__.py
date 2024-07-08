# framework initialization
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import timedelta
from config import Config,DevelopmentConfig,ProductionConfig
import os
from flask_login import LoginManager,login_user,logout_user,current_user

app = Flask(__name__)

# AZUDONI VICTORY CHUWKUNEKU WORK








# app configurations
env= os.getenv('FLASK_ENV','development')
if env=='development':
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)


# db initialization
db = SQLAlchemy(app)
migrate = Migrate(app = app, db = db)
from .model import LoginDataBase,Balance,Current,Utility,Savings,Dollar

# AZUDONI VICTORY CHUWKUNEKU WORK


# routes links
from flask import Blueprint
from .auth import auth
from .view import view
from .admin import admin
app.register_blueprint(auth,url_prifix = '/')
app.register_blueprint(view,url_prifix = '/')
app.register_blueprint(admin,url_prifix = '/')



LoginManager = LoginManager()
LoginManager.login_view = 'auth.login'
LoginManager.init_app(app)

@LoginManager.user_loader
def load_user(id):
    return LoginDataBase.query.get(int(id))