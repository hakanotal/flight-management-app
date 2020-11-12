from classes import Flight, Pilot, Airport, Plane, Reservation
import psycopg2
import urllib.parse as urlparse
import os

url = urlparse.urlparse(os.getenv('DB_URL'))


class Database:
    def __init__(self):
        f1 = Flight(1, 2020, "SGA", "AMH", "Sabiha Gökçen", "Boeing 727", 160, 160)
        f2 = Flight(2, 2020, "AMH", "SGA", "Ahmet Uslu", "Boeing 737", 180, 75)
        self.flights = [f1, f2]

        self.con = psycopg2.connect(
            dbname=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
        self.cur = self.con.cursor()

    def get_flight(self, id):
        for flight in self.flights:
            if flight.id == id:
                return flight