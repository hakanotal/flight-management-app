from flask import Flask
from database import Database
import views


def create_app():
    app = Flask(__name__)
    db = Database()

    app.config.from_object("settings")
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

    return app


if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host='127.0.0.1', port=port)