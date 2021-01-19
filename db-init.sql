DROP TABLE IF EXISTS admins CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS accounts CASCADE;
DROP TABLE IF EXISTS reservations CASCADE;
DROP TABLE IF EXISTS pilots CASCADE;
DROP TABLE IF EXISTS airports CASCADE;
DROP TABLE IF EXISTS abbreviations CASCADE;
DROP TABLE IF EXISTS planes CASCADE;
DROP TABLE IF EXISTS flights CASCADE;


CREATE TABLE accounts(
	mail VARCHAR(30) PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	password VARCHAR(30) NOT NULL,
	is_admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE admins(
	admin_id SERIAL PRIMARY KEY,
	mail VARCHAR(30) UNIQUE NOT NULL,
		FOREIGN KEY(mail) REFERENCES accounts(mail)
);

CREATE TABLE users(
	user_id SERIAL PRIMARY KEY,
	mail VARCHAR(30) UNIQUE NOT NULL,
		FOREIGN KEY(mail) REFERENCES accounts(mail)
);

CREATE TABLE pilots(
	pilot_id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	age INTEGER
);

CREATE TABLE abbreviations(
	abbreviation VARCHAR(30) PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	city VARCHAR(30) NOT NULL
);

CREATE TABLE airports(
	airport_id SERIAL PRIMARY KEY,
	abbreviation VARCHAR(30) UNIQUE NOT NULL,
		FOREIGN KEY(abbreviation) REFERENCES abbreviations(abbreviation)
);

CREATE TABLE planes(
	plane_id SERIAL PRIMARY KEY,
	name VARCHAR(30) UNIQUE NOT NULL,
	brand VARCHAR(30) NOT NULL,
	capacity INTEGER NOT NULL
);

CREATE TABLE flights(
	flight_id SERIAL PRIMARY KEY,
	date DATE NOT NULL,
	fk_pilot_id INTEGER NOT NULL,
		FOREIGN KEY(fk_pilot_id) REFERENCES pilots(pilot_id),
	fk_fromAirport_id INTEGER NOT NULL,
		FOREIGN KEY(fk_fromAirport_id) REFERENCES airports(airport_id),
	fk_toAirport_id INTEGER NOT NULL,
		FOREIGN KEY(fk_toAirport_id) REFERENCES airports(airport_id),
	fk_plane_id INTEGER NOT NULL,
		FOREIGN KEY(fk_plane_id) REFERENCES planes(plane_id),
	passenger_count INTEGER DEFAULT 0
);

CREATE TABLE reservations(
	reservation_id SERIAL PRIMARY KEY,
	count INTEGER NOT NULL,
	fk_user_id INTEGER NOT NULL,
		FOREIGN KEY(fk_user_id) REFERENCES users(user_id),
	fk_flight_id INTEGER NOT NULL,
		FOREIGN KEY(fk_flight_id) REFERENCES flights(flight_id)
);
