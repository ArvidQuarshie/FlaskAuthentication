#blueprint attachment

def create_app(config.name):
#...
from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint,url_prefix='/auth')
return app
