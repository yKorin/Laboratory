create keyspace if not exists DBISLabwork
with replication = {
					'class':'SimpleStrategy'
					,'replication_factor':2
					};



Use DBISLabwork;
CREATE TYPE IF NOT EXISTS DBISLabwork.PositionUser ( 
	Position Text,
	Company text, 
	Started timestamp, 
	Finished timestamp
);

CREATE TABLE IF NOT EXISTS DBISLabwork.User ( 
	NicName text,
	Email Text,
	lastname text, 
	firstname text,
	birthday timestamp, 
	Created timestamp,
	Job list<FROZEN <PositionUser>>,
	PRIMARY KEY (Email)
);

CREATE TABLE IF NOT EXISTS DBISLabwork.Reposytoty ( 
	Id int,
	Name text, 
	firstname text,
	Description text, 
	Created timestamp,
	CountOfProjects int,
	email text,
	PRIMARY KEY (Id)
);

CREATE TABLE IF NOT EXISTS DBISLabwork.Project ( 
	Id int,
	Name text, 
	firstname text,
	Description text, 
	Created timestamp,
	CountOfFiles int,
	repositoryId int,
	PRIMARY KEY (Id)
);

CREATE TABLE IF NOT EXISTS DBISLabwork.File ( 
	Id int,
	Name text, 
	file text,
	Version text, 
	Created timestamp,
	Rating int,
	projectId int,
	PRIMARY KEY (Id)
);