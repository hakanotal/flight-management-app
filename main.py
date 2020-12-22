from flask import Flask
from flask_login import LoginManager
from database import Database
import views, requests
from account import find_user


lm = LoginManager()

@lm.user_loader
def load_user(user_id):
    return find_user(user_id)


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    #Login manager
    lm.init_app(app)
    lm.login_view = "home_page"

    #Database initialization
    db = Database()
    app.config["db"] = db

    #Home page
    app.add_url_rule("/", view_func=views.home_page)
    #User pages
    app.add_url_rule("/flights", view_func=views.flights_page)
    app.add_url_rule("/flights/<int:flight_id>", view_func=views.details_page)
    app.add_url_rule("/myreservations", view_func=views.user_reservations_page)
    #Admin pages
    app.add_url_rule("/panel", view_func=views.panel_home_page)
    app.add_url_rule("/panel/<menu>", view_func=views.panel_menu_page)

    #Home Requests
    app.add_url_rule("/login", view_func=requests.login_request, methods = ['POST'])
    app.add_url_rule("/signup", view_func=requests.signup_request, methods = ['POST'])
    app.add_url_rule("/logout", view_func=requests.logout_request, methods = ['POST'])

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='127.0.0.1')