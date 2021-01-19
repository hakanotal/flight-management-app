from flask import render_template, url_for, current_app, redirect, request, session
from flask_login import login_user, logout_user, current_user, login_required
from passlib.hash import pbkdf2_sha256 as hasher


# LOGIN
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

# SIGN UP
def signup_request():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    db = current_app.config["db"]
    db.add_user(email, name, password)
    return redirect(url_for("home_page"))

# LOG OUT
@login_required
def logout_request():
    logout_user()
    current_app.logger.info('User logging out...')
    return redirect(url_for("home_page"))


# RESERVATION
@login_required
def new_reservation_request(flight_id): 
    count = request.form['count']
    user_id = current_user.id

    db = current_app.config["db"]
    db.new_reservation(count, user_id, flight_id)
    return redirect(url_for("reservations_page"))

@login_required
def add_reservation_request(): 
    user = request.form['user']
    flight = request.form['flight']
    count = request.form['count']

    db = current_app.config["db"]
    db.new_reservation(count, user, flight)
    return redirect(request.referrer)

@login_required
def delete_reservation_request(reservation_id):
    db = current_app.config["db"]
    db.delete_reservation(reservation_id)
    return redirect(request.referrer)


# FLIGHT
@login_required
def add_flight_request(): 
    date = request.form['date']
    from_ = request.form['from'].upper()
    to = request.form['to'].upper()
    pilot = request.form['pilot']
    plane = request.form['plane']

    db = current_app.config["db"]
    db.new_flight(date, pilot, from_, to, plane)
    return redirect(request.referrer)

@login_required
def delete_flight_request(flight_id):
    db = current_app.config["db"]
    db.delete_flight(flight_id)
    return redirect(request.referrer)

@login_required
def search_flights_request():
    date = request.form['date']
    from_ = request.form['from']
    to = request.form['to']
    
    current_app.logger.info('DATE: %s', date)

    db = current_app.config["db"]
    return render_template("pages/flights.html", flights=db.search_flights(date, from_, to), airports=db.get_airports())

# AIRPORT
@login_required
def add_airport_request(): 
    abb = request.form['abb'].upper()
    name = request.form['name'].upper()
    city = request.form['city'].upper()

    db = current_app.config["db"]
    db.new_airport(abb, name, city)
    return redirect(request.referrer)

@login_required
def delete_airport_request(airport_id):
    db = current_app.config["db"]
    db.delete_airport(airport_id)
    return redirect(request.referrer)


# PILOT
@login_required
def add_pilot_request(): 
    name = request.form['name']
    age = request.form['age']

    db = current_app.config["db"]
    db.new_pilot(name, age)
    return redirect(request.referrer)

@login_required
def delete_pilot_request(pilot_id):
    db = current_app.config["db"]
    db.delete_pilot(pilot_id)
    return redirect(request.referrer)


# PLANE
@login_required
def add_plane_request(): 
    name = request.form['name'].upper()
    brand = request.form['brand'].upper()
    cap = request.form['cap']

    db = current_app.config["db"]
    db.new_plane(name, brand, cap)
    return redirect(request.referrer)

@login_required
def delete_plane_request(plane_id):
    db = current_app.config["db"]
    db.delete_plane(plane_id)
    return redirect(request.referrer)


# USER
@login_required
def add_user_request(): 
    mail = request.form['mail']
    name = request.form['name']
    password = request.form['password']
    admin = (request.form['admin'].upper() == "TRUE")

    db = current_app.config["db"]
    db.add_user(mail, name, password, admin)
    return redirect(request.referrer)

@login_required
def delete_user_request(user_id):
    db = current_app.config["db"]
    db.delete_user(user_id)
    return redirect(request.referrer)

@login_required
def update_user_request(user_id):
    name = request.form.get('name')
    password = request.form.get('password')

    db = current_app.config["db"]
    db.update_user(user_id, name, password)
    return redirect(request.referrer)

