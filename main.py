from flask import Flask, current_app
from flask_login import LoginManager
from database import Database
import views, requests


lm = LoginManager()

@lm.user_loader
def load_user(user_id):
    db = current_app.config["db"]
    return db.find_user(user_id)


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    #Login manager
    lm.init_app(app)
    lm.login_view = "home_page"

    #Database initialization
    db = Database()
    app.config["db"] = db

    # VIEWS
    app.add_url_rule("/", view_func=views.home_page)

    app.add_url_rule("/flights", view_func=views.flights_page)
    app.add_url_rule("/flights/<int:flight_id>", view_func=views.details_page)
    app.add_url_rule("/reservations", view_func=views.reservations_page)

    app.add_url_rule("/panel", view_func=views.panel_home_page)
    app.add_url_rule("/panel/<menu>", view_func=views.panel_menu_page)

    # REQUESTS
    app.add_url_rule("/login", view_func=requests.login_request, methods = ['POST'])
    app.add_url_rule("/signup", view_func=requests.signup_request, methods = ['POST'])
    app.add_url_rule("/logout", view_func=requests.logout_request, methods = ['POST'])

    app.add_url_rule("/add_reservation", view_func=requests.add_reservation_request, methods = ['POST'])
    app.add_url_rule("/new_reservation/<int:flight_id>", view_func=requests.new_reservation_request, methods = ['POST'])
    app.add_url_rule("/delete_reservation/<int:reservation_id>", view_func=requests.delete_reservation_request, methods = ['POST'])
    
    app.add_url_rule("/add_flight", view_func=requests.add_flight_request, methods = ['POST'])
    app.add_url_rule("/delete_flight/<int:flight_id>", view_func=requests.delete_flight_request, methods = ['POST'])
    app.add_url_rule("/search_flights", view_func=requests.search_flights_request, methods = ['POST'])

    app.add_url_rule("/add_airport", view_func=requests.add_airport_request, methods = ['POST'])
    app.add_url_rule("/delete_airport/<airport_id>", view_func=requests.delete_airport_request, methods = ['POST'])

    app.add_url_rule("/add_pilot", view_func=requests.add_pilot_request, methods = ['POST'])
    app.add_url_rule("/delete_pilot/<int:pilot_id>", view_func=requests.delete_pilot_request, methods = ['POST'])

    app.add_url_rule("/add_plane", view_func=requests.add_plane_request, methods = ['POST'])
    app.add_url_rule("/delete_plane/<int:plane_id>", view_func=requests.delete_plane_request, methods = ['POST'])

    app.add_url_rule("/add_user", view_func=requests.add_user_request, methods = ['POST'])
    app.add_url_rule("/delete_user/<user_id>", view_func=requests.delete_user_request, methods = ['POST'])

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='127.0.0.1')