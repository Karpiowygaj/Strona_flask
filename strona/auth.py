from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, login_user, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in sucessfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", text="Logowanie pomyślne")


@auth.route('/logout')
@login_required
def logut():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        firstname = request.form.get('FirstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater then 4 characters', category='error')
        elif len(firstname) < 2:
            flash('First name must be greater then 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords must math', category='error')
        elif len(password1) < 7:
            flash('Password is to weak', category='error')
        else:
            # add user to database
            new_user = User(email=email, firstname=firstname,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign-up.html")
