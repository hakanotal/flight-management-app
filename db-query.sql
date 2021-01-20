-- ACCOUNTS
"INSERT INTO accounts(mail, name, password, is_admin) VALUES (%s,%s,%s,%s)"
"SELECT * FROM accounts WHERE mail = %s"
"SELECT * FROM accounts WHERE mail = %s AND password = %s"
"SELECT * FROM accounts"
"DELETE FROM accounts WHERE mail = %s"
"UPDATE accounts SET name = %s WHERE mail = %s"
"UPDATE accounts SET password = %s WHERE mail = %s"

-- RESERVATIONS
"SELECT f.flight_id, f.date, f.fk_fromairport_id, f.fk_toairport_id, r.reservation_id, r.count, r.fk_user_id FROM flights f JOIN reservations r ON (f.flight_id = r.fk_flight_id);"
"SELECT f.flight_id, f.date, f.fk_fromairport_id, f.fk_toairport_id, r.reservation_id, r.count, r.fk_user_id FROM flights f JOIN reservations r ON (f.flight_id = r.fk_flight_id) WHERE r.fk_user_id = %s"
"INSERT INTO reservations(count, fk_user_id, fk_flight_id) VALUES (%s, %s, %s)"
"UPDATE flights SET passenger_count = passenger_count + %s WHERE flight_id = %s"
"SELECT * FROM reservations WHERE reservation_id = %s"
"DELETE FROM reservations WHERE reservation_id = %s"
"UPDATE flights SET passenger_count = passenger_count - %s WHERE flight_id = %s"

-- FLIGHTS
"SELECT f.flight_id, f.date, f.fk_fromairport_id, f.fk_toairport_id, f.passenger_count, pi.name, pl.name, pl.brand, pl.capacity FROM flights f INNER JOIN pilots pi ON (pi.pilot_id = f.fk_pilot_id) INNER JOIN planes pl ON (pl.plane_id = f.fk_plane_id);"
"SELECT f.flight_id, f.date, f.fk_fromairport_id, f.fk_toairport_id, f.passenger_count, pi.name, pl.name, pl.brand, pl.capacity FROM flights f INNER JOIN pilots pi ON (pi.pilot_id = f.fk_pilot_id) INNER JOIN planes pl ON (pl.plane_id = f.fk_plane_id) WHERE flight_id = %s"
"INSERT INTO flights(date, fk_pilot_id, fk_fromairport_id, fk_toairport_id, fk_plane_id, passenger_count) VALUES (%s,%s,%s,%s,%s,%s)"
"DELETE FROM flights WHERE flight_id = %s"
"SELECT f.flight_id, f.date, f.fk_fromairport_id, f.fk_toairport_id, f.passenger_count, pi.name, pl.name, pl.brand, pl.capacity FROM flights f INNER JOIN pilots pi ON (pi.pilot_id = f.fk_pilot_id) INNER JOIN planes pl ON (pl.plane_id = f.fk_plane_id) WHERE f.fk_fromairport_id = %s AND f.fk_toairport_id = %s"
"SELECT f.flight_id, f.date, f.fk_fromairport_id, f.fk_toairport_id, f.passenger_count, pi.name, pl.name, pl.brand, pl.capacity FROM flights f INNER JOIN pilots pi ON (pi.pilot_id = f.fk_pilot_id) INNER JOIN planes pl ON (pl.plane_id = f.fk_plane_id) WHERE f.date = %s AND f.fk_fromairport_id = %s AND f.fk_toairport_id = %s"

-- PILOTS
"SELECT * FROM pilots WHERE pilot_id = %s"
"SELECT * FROM pilots"
"INSERT INTO pilots(name, age) VALUES (%s,%s)"
"DELETE FROM pilots WHERE pilot_id = %s"

-- PLANES
"SELECT * FROM planes WHERE plane_id = %s"
"SELECT * FROM planes"
"INSERT INTO planes(name, brand, capacity) VALUES (%s,%s,%s)"
"DELETE FROM planes WHERE plane_id = %s"

-- AIRPORTS
"SELECT * FROM airports"
"INSERT INTO airports(abbreviation, name, city) VALUES (%s,%s,%s)"
"DELETE FROM airports WHERE abbreviation = %s"
