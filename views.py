from flask import render_template, url_for, current_app, redirect
from passlib.hash import pbkdf2_sha256 as hasher

#Home
def home_page():
    '''
    admin_name = os.getenv("ADMIN_NAME")
    admin_pw = os.getenv("ADMIN_PASSWORD")
    if hasher.verify(admin_name, admin_pw):
        return redirect(url_for("panel_page"))
    '''
    return render_template("home.html")


#User
def flights_page():
    db = current_app.config["db"]
    return render_template("flights.html", flights=db.flights)

def details_page(flight_id):
    db = current_app.config["db"]
    flight = db.get_flight(flight_id)
    return render_template("details.html", flight=flight)

def user_reservations_page():
    return render_template("user_reservations.html")


#Admin
def panel_home_page():
    return render_template("panels/home-panel.html")

def panel_menu_page(menu):
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