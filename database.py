from data_types import User, Flight, Pilot, Airport, Plane, Reservation
from flask import current_app
import psycopg2


class Database:
    def __init__(self):
        # Connection to postgres DB
        self.conn = psycopg2.connect(
            host = 'ec2-54-217-236-206.eu-west-1.compute.amazonaws.com',
            database = 'df318pdncl0ave',
            user = 'cuorkiryfslzay',
            password = 'c09f7fbd08121fa82131d015a5fbd4e3b0e470a2e8f35afdcae5e93200a4bb29'
        )
        self.conn.commit()


    # FLIGHT
    def get_flights(self):
        flights = []
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM flights")
        rows = cur.fetchall()
        cur.close()
        for r in rows:
            pilot = self.get_pilot(r[2])
            plane = self.get_plane(r[5])
            flights.append(Flight(r[0], r[1], pilot[1], r[3], r[4], plane[1], plane[3], r[6]))
        return flights

    def get_flight(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM flights WHERE flight_id = %s", (id,))
        r = cur.fetchone()
        cur.close()
        pilot = self.get_pilot(r[2])
        plane = self.get_plane(r[5])
        flight = Flight(r[0], r[1], pilot[1], r[3], r[4], plane[1], plane[3], r[6])
        return flight
    
    def new_flight(self, date, pilot, from_airport, to_airport, plane_type):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO flights(date, fk_pilot_id, fk_fromairport_id, fk_toairport_id, fk_plane_id, passenger_count) VALUES (%s,%s,%s,%s,%s,%s)", (date, pilot, from_airport, to_airport, plane_type, 0))
        cur.close()
        self.conn.commit()
    
    def delete_flight(self, id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM flights WHERE flight_id = %s", (id,))
        cur.close()
        self.conn.commit()

    def search_flights(self, date, from_, to):
        flights = []
        cur = self.conn.cursor()
        if not date:
            cur.execute("SELECT * FROM flights WHERE fk_fromairport_id = %s AND fk_toairport_id = %s", (from_, to))
        else:
            cur.execute("SELECT * FROM flights WHERE date = %s AND fk_fromairport_id = %s AND fk_toairport_id = %s", (date, from_, to))
        rows = cur.fetchall()
        cur.close()
        for r in rows:
            pilot = self.get_pilot(r[2])
            plane = self.get_plane(r[5])
            flights.append(Flight(r[0], r[1], pilot[1], r[3], r[4], plane[1], plane[3], r[6]))
        return flights


    # PILOT
    def get_pilot(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM pilots WHERE pilot_id = %s", (id,))
        r = cur.fetchone()
        cur.close()
        return r

    def get_pilots(self):
        pilots = []
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM pilots")
        rows = cur.fetchall()
        cur.close()
        for r in rows:
            pilots.append(Pilot(r[0], r[1], r[2]))
        return pilots

    def new_pilot(self, name, age):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO pilots(name, age) VALUES (%s,%s)", (name, age))
        cur.close()
        self.conn.commit()
    
    def delete_pilot(self, id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM pilots WHERE pilot_id = %s", (id,))
        cur.close()
        self.conn.commit()


    # PLANE
    def get_plane(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM planes WHERE plane_id = %s", (id,))
        r = cur.fetchone()
        cur.close()
        return r

    def get_planes(self):
        planes = []
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM planes")
        rows = cur.fetchall()
        cur.close()
        for r in rows:
            planes.append(Plane(r[0], r[1], r[2], r[3]))
        return planes

    def new_plane(self, name, brand, cap):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO planes(name, brand, capacity) VALUES (%s,%s,%s)", (name, brand, cap))
        cur.close()
        self.conn.commit()
    
    def delete_plane(self, id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM planes WHERE plane_id = %s", (id,))
        cur.close()
        self.conn.commit()


    # AIRPORT
    def get_airports(self):
        airports = []
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM airports")
        rows = cur.fetchall()
        cur.close()
        for r in rows:
            airports.append(Airport(r[0], r[1], r[2]))
        return airports

    def new_airport(self, abb, name, city):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO airports(abbreviation, name, city) VALUES (%s,%s,%s)", (abb, name, city))
        cur.close()
        self.conn.commit()
    
    def delete_airport(self, id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM airports WHERE abbreviation = %s", (id,))
        cur.close()
        self.conn.commit()


    # RESERVATION
    def get_reservations(self):
        reservations = []
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM reservations")
        rows = cur.fetchall()
        cur.close()
        for r in rows:
            reservations.append(Reservation(r[0], r[1], r[2], r[3]))
        return reservations
    
    def get_reservations_of_user(self, id):
        reservations = []
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM reservations WHERE fk_user_id = %s", (id,))
        rows = cur.fetchall()
        cur.close()
        for r in rows:
            reservations.append(Reservation(r[0], r[1], r[3], self.get_flight(r[3])))
        return reservations
    
    def new_reservation(self, count, user, flight):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO reservations(count, fk_user_id, fk_flight_id) VALUES (%s, %s, %s)", (count, user, flight))
        cur.execute("UPDATE flights SET passenger_count = passenger_count + %s WHERE flight_id = %s", (count, flight))
        cur.close()
        self.conn.commit()
    
    def delete_reservation(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM reservations WHERE reservation_id = %s", (id,))
        r = cur.fetchone()
        cur.execute("DELETE FROM reservations WHERE reservation_id = %s", (id,))
        cur.execute("UPDATE flights SET passenger_count = passenger_count - %s WHERE flight_id = %s", (r[1], r[3]))
        cur.close()
        self.conn.commit()


    # USER
    def add_user(self, mail, name, password, admin=False): 
        cur = self.conn.cursor()
        cur.execute("INSERT INTO accounts(mail, name, password, is_admin) VALUES (%s,%s,%s,%s)", (mail, name, password, admin)) 
        cur.close()
        self.conn.commit()
        
    def find_user(self, mail):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM accounts WHERE mail = %s", (mail,))
        r = cur.fetchone()
        cur.close()
        if r:
            return User(r[0], r[1], r[2], r[3])
        return None

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
    
    def delete_user(self, id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM accounts WHERE mail = %s", (id,))
        cur.close()
        self.conn.commit()