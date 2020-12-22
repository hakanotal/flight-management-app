from flask import render_template, url_for, current_app, redirect, request, session
from flask_login import login_user, logout_user, current_user, login_required
from passlib.hash import pbkdf2_sha256 as hasher
from random import randint


#Home
def login_request():
    email = request.form['email']
    password = request.form['password']

    db = current_app.config["db"]
    user = db.check_user(email, password)

    #Valid
    if user is not None:
        #Admin
        if user.is_admin is True:
            login_user(user)
            current_app.logger.info('Admin logging: %s - %s ', email, password)
            return redirect(url_for("panel_home_page"))
        #User
        else:
            login_user(user)
            current_app.logger.info('User logging: %s - %s ', email, password)
            return redirect(url_for("flights_page"))

    #Invalid
    else:
        current_app.logger.info('Invalid attempt: %s - %s ', email, password)
        return redirect(url_for("home_page"))

def signup_request():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    db = current_app.config["db"]
    db.add_user(email, name, password)
    return redirect(url_for("home_page"))

@login_required
def logout_request():
    logout_user()
    current_app.logger.info('User logging out...')
    return redirect(url_for("home_page"))