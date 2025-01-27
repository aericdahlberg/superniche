create table Attendees (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(50),
    surname VARCHAR(50),
    job_title VARCHAR(50),
    company_name VARCHAR(50),
	company_type VARCHAR(50),
    ticket_type VARCHAR(50),
	ticket_price int,
    date_registered date,
    email_address VARCHAR(150)
);

insert into Attendees (first_name, surname, job_title, company_name, company_type, ticket_type, ticket_price, date_registered, email_address) values ('Ranice', 'Burras', 'Financial Advisor', 'Gigashots', 'GPACU', 'discount', 20, '2/16/2024', 'rburras0@youtube.com');
insert into Attendees (first_name, surname, job_title, company_name, company_type, ticket_type, ticket_price, date_registered, email_address) values ('Martina', 'Conibere', 'Mechanical Systems Engineer', 'Zoovu', 'CEZ', 'early bird', 30, '11/10/2024', 'mconibere1@domainmarket.com');
insert into Attendees (first_name, surname, job_title, company_name, company_type, ticket_type, ticket_price, date_registered, email_address) values ('Gayla', 'Debell', 'Senior Quality Engineer', 'Jabberbean', 'DLX', 'early bird', 30, '8/11/2024', 'gdebell2@aol.com');
insert into Attendees (first_name, surname, job_title, company_name, company_type, ticket_type, ticket_price, date_registered, email_address) values ('Dolly', 'Clyde', 'Help Desk Operator', 'Feedfire', 'TRCH', 'standard', 20, '5/22/2023', 'dclyde3@spiegel.de');
insert into Attendees (first_name, surname, job_title, company_name, company_type, ticket_type, ticket_price, date_registered, email_address) values ('Hervey', 'Skyme', 'Quality Control Specialist', 'Dabjam', 'GSH', 'early bird', 10, '10/3/2024', 'hskyme4@bbb.org');
insert into Attendees (first_name, surname, job_title, company_name, company_type, ticket_type, ticket_price, date_registered, email_address) values ('Cedric', 'Hardson', 'Data Coordinator', 'Dabvine', 'STX', 'standard', 20, '2/3/2024', 'chardson5@example.com');
insert into Attendees (first_name, surname, job_title, company_name, company_type, ticket_type, ticket_price, date_registered, email_address) values ('Weston', 'Bernardelli', 'Social Worker', 'Topicstorm', 'GSL^B', 'early bird', 20, '3/21/2024', 'wbernardelli6@webs.com');
insert into Attendees (first_name, surname, job_title, company_name, company_type, ticket_type, ticket_price, date_registered, email_address) values ('Flin', 'Websdale', 'Project Manager', 'Voomm', 'AEB', 'standard', 10, '12/28/2023', 'fwebsdale7@google.pl');
insert into Attendees (first_name, surname, job_title, company_name, company_type, ticket_type, ticket_price, date_registered, email_address) values ('Sammie', 'Worsam', 'Senior Cost Accountant', 'Ntag', 'IRET', 'standard', 10, '2/14/2023', 'sworsam8@ezinearticles.com');
insert into Attendees (first_name, surname, job_title, company_name, company_type, ticket_type, ticket_price, date_registered, email_address) values ('Arnie', 'Haggerwood', 'Nuclear Power Engineer', 'Skibox', 'ROP', 'standard', 20, '4/13/2024', 'ahaggerwood9@businesswire.com');