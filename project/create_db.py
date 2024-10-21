import sqlite3
import os

# Creates db.sqlite3, a test database for SQL injection

db = \
"""
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE Users (id varchar(9) PRIMARY KEY, name varchar(50), password TEXT, admin BOOL);
INSERT INTO Users VALUES('123','Hank','StrongPass321',0);
INSERT INTO Users VALUES('eX','Extra','987saX', 0);
INSERT INTO Users VALUES('Texas','Alabama','Steak99', 1);
INSERT INTO Users VALUES('S','Superman','p23', 0);
INSERT INTO Users VALUES('Uni1','Universal','globalPASS', 1);

CREATE TABLE Clients (name varchar(50), client TEXT);
INSERT INTO Clients VALUES('Texas','Hank');
INSERT INTO Clients VALUES('eX','Milly Moo');
INSERT INTO Clients VALUES('S','Wonderland');

COMMIT;
"""

if os.path.exists('db.sqlite3'):
	print('db.sqlite3 already exists')
else:
	conn = sqlite3.connect('db.sqlite3')
	conn.cursor().executescript(db)
	conn.commit()
