class Flight:
    def __init__(self, id, date, pilot, from_airport, to_airport, plane_type, capacity, passengers=0):
        self.id = id
        self.date = date
        self.from_airport = from_airport
        self.to_airport = to_airport
        self.pilot = pilot
        self.plane = plane_type
        self.capacity = capacity
        self.passengers = passengers


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
    def __init__(self, id, user, flight, count):
        self.id = id
        self.user = user
        self.flight = flight
        self.count = count