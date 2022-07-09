from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    return render_template("login.html", text="Logowanie pomyślne")


@auth.route('/logout')
def logut():
    return render_template("logout.html")


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        firstname = request.form.get('FirstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        print(request.form)
        if len(email) < 4:
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
            flash('Account created', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign-up.html")
