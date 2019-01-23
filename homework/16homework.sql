CREATE TABLE friends (
    id INTEGER,
    name TEXT,
    location TEXT
);

INSERT INTO friends (id, name, location)
VALUES (1, 'Justin', 'Seoul')
(2, 'Simon', 'New York')
(3, 'Chang', 'Las Vegas')
(4, 'John', 'Sydney');

ALTER TABLE friends
ADD COLUMN married INTEGER;

UPDATE friends
SET married = 1
WHERE id = 1, id = 4;

UPDATE friends
SET married = 0
WHERE id = 2, id = 3;

DELETE FROM friends
WHERE married = 0;