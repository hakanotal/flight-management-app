from flask import render_template, url_for, current_app, redirect, abort
from flask_login import login_required, current_user, logout_user


#Home Page
def home_page():
    if current_user:
        logout_user()
    return render_template("pages/home.html")


#User Pages
@login_required
def flights_page():
    db = current_app.config["db"]
    return render_template("pages/flights.html", flights=db.get_flights(), airports=db.get_airports())

@login_required
def details_page(flight_id):
    db = current_app.config["db"]
    flight = db.get_flight(flight_id)
    return render_template("pages/details.html", flight=flight)

@login_required
def reservations_page():
    db = current_app.config["db"]
    return render_template("pages/reservations.html", reservations=db.get_reservations_of_user(current_user.id))

@login_required
def settings_page():
    return render_template("pages/settings.html", user=current_user)

#Admin Pages
@login_required
def panel_home_page():
    current_app.logger.info('DEBUG: %s', current_user.id)
    if current_user.is_admin is False:
        abort(401)

    return render_template("panels/home-panel.html")

@login_required
def panel_menu_page(menu):
    if current_user.is_admin is False:
        abort(401)

    db = current_app.config["db"]

    if(menu == "flights"):
        return render_template("panels/flights-panel.html", menu=menu, flights=db.get_flights())
    elif(menu == "pilots"):
        return render_template("panels/pilots-panel.html", menu=menu, pilots=db.get_pilots())
    elif(menu == "planes"):
        return render_template("panels/planes-panel.html", menu=menu, planes=db.get_planes())
    elif(menu == "airports"):
        return render_template("panels/airports-panel.html", menu=menu, airports=db.get_airports())
    elif(menu == "reservations"):
        return render_template("panels/reservations-panel.html", menu=menu, reservations=db.get_reservations())
    elif(menu == "users"):
        return render_template("panels/users-panel.html", menu=menu, users=db.get_users())
    else:    
        return redirect(url_for("panel_home_page"))