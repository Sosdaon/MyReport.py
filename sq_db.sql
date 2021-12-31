CREATE TABLE IF NOT EXISTS mainmenu (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
url text NOT NULL
);

CREATE TABLE IF NOT EXISTS posts (
id integer PRIMARY KEY AUTOINCREMENT,
passport_number text NOT NULL,
title text NOT NULL,
text text NOT NULL,
institution_name text NOT NULL,
department_name text NOT NULL,
time integer NOT NULL
);
