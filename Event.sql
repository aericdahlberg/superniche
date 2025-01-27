create table event (
	id SERIAL PRIMARY KEY,
	event_name VARCHAR(100),
	event_logo bytea,
	tagline VARCHAR(100), 
	abstract TEXT
	event_date date, 
	
);

' new table creation... insert into event (event_name, event_logo, tagline, datetime_start, datetime_end, abstract) values ('Crypto Meet', null, 'Unleash the power of crypto', '2024-01-12 18:10:15', '2024-07-17 13:41:27', 'Come connect and learn more about crypto');

