from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from . import auth
from .forms import SignUpForm, LoginForm
from .. import db
from ..models import User
from ..email import mail_message


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        
        mail_message("Welcome to Pitch", "email/welcome", user.email, user=user)
        
        return redirect(url_for('auth.login'))
    title = "New Account"
    return render_template('auth/signup.html', signupform=form, title=title)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login = LoginForm()
    if login.validate_on_submit():
        user = User.query.filter_by(username=login.username.data).first()
        if user is not None and user.verify_password(login.password.data):
            login_user(user, login.rememberMe.data)
            return redirect(url_for('main.index'))

        flash('Invalid username or password')

    title = 'Login'

    return render_template('auth/login.html', loginform=login, title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
