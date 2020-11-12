from classes import Flight, Pilot, Airport, Plane, Reservation
import urllib.parse as urlparse
import os

'''url = urlparse.urlparse(os.getenv('DATABASE_URL'))'''


class Database:
    def __init__(self):
        f1 = Flight(1, 2020, "SGA", "AMH", "Sabiha Gökçen", "Boeing 727", 160, 160)
        f2 = Flight(2, 2020, "AMH", "SGA", "Ahmet Uslu", "Boeing 737", 180, 75)
        self.flights = [f1, f2]


    def get_flight(self, id):
        for flight in self.flights:
            if flight.id == id:
                return flight