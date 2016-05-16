from flask.ext.login import UserMixin

class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(64),unique=True,index=True)
    username=db.Column(db.String(64),unoque=True,index=True)
    password_hash=db.Column(db.String)(128))
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))



#####
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    #...
    password_hash = db.Column(db.String(128))
    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")
    @password.setter
    def password(self):
        self.password_hash=generate_password_hash(password)
    def verify_password(self,password):
        self.password_hash=generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

#User Loader call back function
#login manager provides a level of security

from . import login_manager

@login_manager.user_loader

def load_user(user_id):
    return User.query.get(int(user_id))
        

#User Account Confirmation

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from . import db

class User(UserMixin,db.Model):
    #..
    confirmed=db.Column(db.Boolean,default=False)

def generate_confirmation_token(self,expiration=3600)
    s=Serializer(current_app.config['SECRET_KEY'],expiration)
    return s.dumps({'confirm':self.id})

def confirm(self,token):
    s=Serializer(current_app.config['SECRET_KEY'])
    try:
    

    





