drop table Agenda;
create table Agenda (
	session_id BIGSERIAL PRIMARY KEY,
	session_time time NOT NULL,
	title varchar(100),
	abstract VARCHAR(150),
	session_track Varchar(150)
);
insert into Agenda (session_time, title, abstract, session_track) values ('8:31 AM', 'Man Push Cart', 'Drama', 'Blockchain');
insert into Agenda (session_time, title, abstract, session_track) values ('6:25 PM', 'Max Payne', 'Action|Crime|Drama|Thriller', 'Web Development');
insert into Agenda (session_time, title, abstract, session_track) values ('4:20 PM', '7 Plus Seven', 'Documentary', 'Digital Marketing');
insert into Agenda (session_time, title, abstract, session_track) values ('7:42 PM', '29 Palms', 'Comedy|Drama|Thriller', 'Mobile App Development');
insert into Agenda (session_time, title, abstract, session_track) values ('8:27 AM', 'Best Foot Forward', 'Comedy|Musical', 'Mobile App Development');
insert into Agenda (session_time, title, abstract, session_track) values ('5:08 PM', 'Torment (Hets)', 'Drama', 'Blockchain');
insert into Agenda (session_time, title, abstract, session_track) values ('7:53 AM', 'Asterix & Obelix vs. Caesar (Astérix et Obélix contre César)', 'Adventure|Children|Comedy|Fantasy', 'Internet of Things');
insert into Agenda (session_time, title, abstract, session_track) values ('9:20 AM', 'White Sound, The (Das weiße Rauschen)', 'Drama', 'Cybersecurity');
insert into Agenda (session_time, title, abstract, session_track) values ('4:47 PM', 'Wuthering Heights', 'Drama|Romance', 'Web Development');
insert into Agenda (session_time, title, abstract, session_track) values ('12:10 PM', 'Legend of Hell House, The', 'Horror|Thriller', 'Artificial Intelligence');