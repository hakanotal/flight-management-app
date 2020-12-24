from data_types import Flight, Pilot, Airport, Plane, Reservation
from flask import current_app
from account import User
import psycopg2


class Database:
    def __init__(self):
        # Connect to your postgres DB
        self.conn = psycopg2.connect(
            host = 'ec2-54-217-236-206.eu-west-1.compute.amazonaws.com',
            database = 'df318pdncl0ave',
            user = 'cuorkiryfslzay',
            password = 'c09f7fbd08121fa82131d015a5fbd4e3b0e470a2e8f35afdcae5e93200a4bb29'
        )
        self.conn.commit()


    def get_flights(self):
        flights = []
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM flights")
        rows = cur.fetchall()
        cur.close()
        for r in rows:
            pilot = self.get_pilot_name(r[2])
            plane = self.get_plane_name(r[5])
            flights.append(Flight(r[0], r[1], pilot, r[3], r[4], plane, r[6]))
        return flights

    def get_flight(self, id):
        for flight in self.get_flights:
            if flight.id == id:
                return flight

    def get_pilot_name(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM pilots WHERE pilot_id = %s", id)
        r = cur.fetchone()
        cur.close()
        return r[1]

    def get_pilots(self):
        pilots = []
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM pilots")
        rows = cur.fetchall()
        cur.close()
        for r in rows:
            pilots.append(Pilot(r[0], r[1], r[2]))
        return pilots


    def get_plane_name(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM planes WHERE plane_id = %s", id)
        r = cur.fetchone()
        cur.close()
        return r[1].join(r[2])

    def get_planes(self):
        planes = []
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM planes")
        rows = cur.fetchall()
        cur.close()
        for r in rows:
            planes.append(Plane(r[0], r[1], r[2], r[3]))
        return planes

    def get_airports(self):
        airports = []
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM airports")
        rows = cur.fetchall()
        cur.close()
        for r in rows:
            airports.append(Airport(r[0], r[1], r[2]))
        return airports

    def get_reservations(self):
        reservations = []
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM reservations")
        rows = cur.fetchall()
        cur.close()
        for r in rows:
            reservations.append(Reservation(r[0], r[1], r[2], r[3]))
        return reservations


    def add_user(self, mail, name, password): 
        cur = self.conn.cursor()
        cur.execute("INSERT INTO accounts(mail, name, password) VALUES (%s, %s, %s)", (mail, name, password)) 
        cur.close()
        self.conn.commit()
        

    def check_user(self, mail, password):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM accounts WHERE mail = %s AND password = %s", (mail, password))
        r = cur.fetchone()
        cur.close()
        return User(r[0], r[1], r[2], r[3])
        
    def get_users(self):
        users = []
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM accounts")
        rows = cur.fetchall()
        cur.close()
        for r in rows:
            users.append(User(r[0], r[1], r[2], r[3]))
        return users