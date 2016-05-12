from flask.ext.login import UserMixin


class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(64),unique=True,index=True)
    username=db.Column(db.String(64),unique-True,Index=True)
    password_hash=db.Column(db.String(128))
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

from import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


