from flask.ext.login import Logimanager

login_manager=LoginManager()
login_manager.login_view='auth.login'

def create app(config_name):

login_manager.init_app(app)
