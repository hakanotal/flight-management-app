from flask import render_template, url_for, current_app, redirect
from passlib.hash import pbkdf2_sha256 as hasher


def home_page():
    '''
    admin_name = os.getenv("ADMIN_NAME")
    admin_pw = os.getenv("ADMIN_PASSWORD")
    if hasher.verify(admin_name, admin_pw):
        return redirect(url_for("panel_page"))
    '''
    return render_template("home.html")

def details_page(flight_id):
    db = current_app.config["db"]
    flight = db.get_flight(flight_id)
    return render_template("details.html", flight=flight)

def flights_page():
    db = current_app.config["db"]
    return render_template("flights.html", flights=db.flights)


def user_reservations_page():
    return render_template("user_reservations.html")


def panel_page():
    return render_template("panel.html")