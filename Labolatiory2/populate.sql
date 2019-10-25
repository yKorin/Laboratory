INSERT INTO Users (login, password, email, lastname, firstname, created)
VALUES('Jon1','1234qwer','Jonbla1@gmail.com', 'Jon', 'Kon', NOW());
INSERT INTO Users (login, password, email, lastname, firstname, created)
VALUES('Bob345','123qwert','bobwilsom@gmail.com', 'Bob', 'Wilsom', NOW());
INSERT INTO Users (login, password, email, lastname, firstname, created)
VALUES('Nick324','1234qwer','nicktramp@gmail.com', 'Nick', 'Tramp', NOW());

INSERT INTO Reposytoty (name, description, created, countofprojects, user_id)
VALUES ('Population of reptile','Research population reptile', NOW(), 1, 3);
INSERT INTO Reposytoty (name, description, created, countofprojects, user_id)
VALUES ('Parsing fecebook','Methods for parsing page of fecebook', NOW(), 3, 4);
INSERT INTO Reposytoty (name, description, created, countofprojects, user_id)
VALUES ('Data maining','Algoritms for maining', NOW(), 2, 4);

INSERT INTO Project (name, description, created, CountOfFiles, reposytoty_ID)
VALUES ('Population','Research population reptile in Africa', NOW(), 4, 1);
INSERT INTO Project (name, description, created, CountOfFiles, reposytoty_ID)
VALUES ('Parsing news line','Method parsing news line of fecebook', NOW(), 3, 2);
INSERT INTO Project (name, description, created, CountOfFiles, reposytoty_ID)
VALUES ('Parsing single page','Method parsing single page of fecebook', NOW(), 5, 2);

INSERT INTO Files (name, File_text, Expansion, versions, created, rating, project_ID)
VALUES ('main','import ...', '.py', '1.0.0.1', NOW(), 0.32, 1);
INSERT INTO Files (name, file_text, Expansion, versions, created, rating, project_ID)
VALUES ('poplate','import pandas ...', '.py', '1.0.0.2', NOW(), 0.39, 1);
INSERT INTO Files (name, file_text, Expansion, versions, created, rating, project_ID)
VALUES ('main','import xml...', '.py', '1.0.1', NOW(), 0.02, 2);

select * from users;
select * from reposytoty;
select * from project;
select * from files;
