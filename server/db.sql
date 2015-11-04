CREATE TABLE cards (
	id int(11) AUTO_INCREMENT,
	q text NOT NULL default '',
	a text NOT NULL default '',
	cat varchar(255) NOT NULL default '',
	sort int(11) NOT NULL default 0,
	INDEX(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

