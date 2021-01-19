from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256 as hasher

class User(UserMixin):
    def __init__(self, mail, name, password, admin=False):
        self.id = mail
        self.name = name
        self.mail = mail
        self.password = hasher.hash(password)
        self.is_admin = admin

    def get_id(self):
        return self.mail
        

class Flight:
    def __init__(self, id, date, from_airport, to_airport, passengers, pi_name, pl_name, pl_brand, pl_cap):
        self.id = id
        self.date = date
        self.from_airport = from_airport
        self.to_airport = to_airport
        self.passengers = passengers
        self.pi_name = pi_name
        self.pl_name = pl_name
        self.pl_brand = pl_brand
        self.pl_cap = pl_cap


class Pilot:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class Airport:
    def __init__(self, abbr, name, city):
        self.name = name
        self.city = city
        self.abbr = abbr


class Plane:
    def __init__(self, id, name, brand, capacity):
        self.id = id
        self.name = name
        self.brand = brand
        self.capacity = capacity


class Reservation:
    def __init__(self, f_id, f_date, f_from, f_to, id, count, user):
        self.id = id
        self.user = user
        self.count = count
        self.f_id = f_id
        self.f_date = f_date
        self.f_from = f_from
        self.f_to = f_to