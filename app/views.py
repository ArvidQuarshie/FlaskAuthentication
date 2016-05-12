from flask import render_template,redirect,request,url_for ,flash
from flask.ext.login import login_user
from . import auth
from ..models import User
from .forms import LoginForm

@auth.route('/login',methods=['GET','POST'])
def login():
    form=loginForm()
    if form.validate_on_submit():
    user=User.query.filter_by(email=form.email.data).first()
