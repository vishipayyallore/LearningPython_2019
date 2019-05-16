PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE persons (id int, name text);
INSERT INTO persons VALUES(101,'Manish');
INSERT INTO persons VALUES(102,'Ranesh');
COMMIT;
