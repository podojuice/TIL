CREATE TABLE bands (
id INTEGER,
name TEXT,
debut INTEGER
);

INSERT INTO bands (id, name, debut)
VALUES 
(1, 'Queen', 1973),
(2, 'Coldplay', 1998),
(3, 'MCR', 2001);

SELECT id, name FROM bands;

SELECT name FROM bands WHERE debut < 2000;