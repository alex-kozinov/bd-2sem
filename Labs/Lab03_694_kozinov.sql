1.
SELECT min(range) as "minimal distance", max(range) as "maximal distance"
FROM aircrafts
2.
SELECT a.model, max(a.range) as "longest distance", count(s.seat_no) as "Number of seats"
FROM aircrafts a 
INNER JOIN seats s ON (a.aircraft_code = s.aircraft_code)
GROUP BY a.model
3.
SELECT passenger_name, count(ticket_no) as "Number of tickets"
FROM tickets
GROUP BY passenger_name
ORDER BY count(ticket_no) DESC
LIMIT 10
4.
SELECT  tick.passenger_name, 
	count(tick.ticket_no) as "Number of flights",
	round(cast(AVG(book.total_amount) as decimal), 2) as "average cost"
FROM bookings book
INNER JOIN tickets tick ON (book.book_ref = tick.book_ref)
GROUP BY passenger_name
HAVING count(tick.ticket_no) >= (SELECT count(t.ticket_no)
				 FROM tickets t
				 GROUP BY t.passenger_name
				 ORDER BY count(t.ticket_no) DESC
				 OFFSET 10 Rows
				 LIMIT 1)
ORDER BY count(tick.ticket_no) DESC
LIMIT 10
5.
SELECT count(f.flight_no)
FROM flights f, airports a
WHERE a.airport_code = f.departure_airport
AND a.city='Москва'
AND f.arrival_airport='LED'
6.
SELECT f.flight_no, ai.city, f.scheduled_departure,
       count(bp.seat_no) FILTER (WHERE tf.fare_conditions='Economy') as "Econumy seats",
       count(bp.seat_no) FILTER (WHERE tf.fare_conditions='Comfort') as "Comfort seats", 
       count(bp.seat_no) FILTER (WHERE tf.fare_conditions='Business') as "Business seats"
FROM flights f, ticket_flights tf, boarding_passes bp, airports ai
WHERE f.flight_id = tf.flight_id
AND tf.flight_id = bp.flight_id
AND f.arrival_airport=ai.airport_code
AND f.departure_airport = 'DME'
AND f.scheduled_departure BETWEEN bookings.now() AND bookings.now() + '3 hour'
GROUP BY f.flight_no, ai.city, f.scheduled_departure
7.
SELECT ti.passenger_name, round(cast(AVG(tf.amount) as decimal), 2) as "avg cost"
FROM  flights fl, ticket_flights tf, tickets ti
WHERE fl.flight_id = tf.flight_id
AND ti.ticket_no = tf.ticket_no
AND ti.passenger_name IN (
	SELECT passenger_name
	FROM tickets ti, ticket_flights tf
	WHERE ti.ticket_no = tf.ticket_no
	AND tf.flight_id = 2943
	AND tf.fare_conditions = 'Business'
	)
GROUP BY ti.passenger_name
HAVING AVG(tf.amount) < 20000
ORDER BY AVG(tf.amount) DESC
8.
SELECT ti.ticket_no, tf.flight_id, fl.scheduled_departure, sum(tf.amount) OVER (ORDER BY fl.scheduled_departure)
FROM tickets ti, ticket_flights tf, flights fl
WHERE ti.ticket_no = tf.ticket_no
AND tf.flight_id = fl.flight_id
AND ti.passenger_name = 'YULIYA MOROZOVA';