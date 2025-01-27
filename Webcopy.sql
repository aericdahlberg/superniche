create table WebCopy (
	id SERIAL PRIMARY KEY,
	header_names VARCHAR(100),
    homepage_copy text,
    call_to_action VARCHAR(50),
    early_registration_copy VARCHAR(50),
    sponsorship_copy VARCHAR(50), 
    contact_us_copy VARCHAR(50),
    about_organizer_copy VARCHAR(50),
    discount_info text
);

