from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,Regexp,EqualTo
from wtforms import ValidationError
from ..models import User

class RegistrationForm(Form)
    email=StringField('Email',validators=[Required(),Length(1,64),Email()])
    username=StringField('Username', validators=[Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
'Usernames must have only letters, '
'numbers, dots or underscores')])
    password=PasswordFiels('password', validators=[Required(), EqualTo('password2',message='Passwords must match')])
    password2=PasswordField('Confirm Password' validators=[Required()])
    submit=submitField('Register')

def validate_email(self,field):
    if User.query.filter_by(email=field.data).first()
        raise ValidationError('Email Already Registered')

def vallidate_username(self,field):
    if User.query.filter_by(Username=field.data).first()
        raise VallidationError('Username Already In Use')
