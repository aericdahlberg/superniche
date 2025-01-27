create table Pricing_Grid (
	id SERIAL PRIMARY KEY,
	pricing_type VARCHAR(50),
    expiration_date date default null,
    available_date date default null,
    ticket_price int not null
);

insert into Pricing_Grid (pricing_type, expiration_date, available_date, ticket_price) values ('early bird', null, null, 10);
insert into Pricing_Grid (pricing_type, expiration_date, available_date, ticket_price) values ('standard', null, null, 20);
insert into Pricing_Grid (pricing_type, expiration_date, available_date, ticket_price) values ('discount', null, null, 30);