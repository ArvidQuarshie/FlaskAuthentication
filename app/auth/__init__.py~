#creating an authentication blueprint

from flask import Blueprint
auth=Blueprint('auth',__name__)
from . import views

#flask login initialization

from flask.ext.login import LoginManager

login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.loginview='auth.login'

def create_app(config_name):
#..
login_manager.init_app(app)
#..


