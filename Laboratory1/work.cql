

insert into dbislabwork.user(NicName,Email,lastname,firstname,birthday,Created,Job) 
values('joseph','emailjoseph.com','last','first','1985-10-16','2000-10-16',
	[{Position:'team lead',Company:'google',Started:'2000-10-16',Finished:'2000-10-16'}]
);

insert into dbislabwork.user(NicName,Email,lastname,firstname,birthday,Created,Job) 
values('dima','emaildima.com','last','first','1985-10-16','2000-10-16',
	[{Position:'team lead',Company:'google',Started:'2000-10-16',Finished:'2000-10-16'}]
);

insert into dbislabwork.user(NicName,Email,lastname,firstname,birthday,Created,Job) 
values('andriy','emailandriy.com','last','first','1985-10-16','2000-10-16',
	[{Position:'team lead',Company:'google',Started:'2000-10-16',Finished:'2000-10-16'}]
);
select * from dbislabwork.user;

insert into dbislabwork.reposytoty(Id,Name,firstname,Description,Created,CountOfProjects,email) 
values(1,'github','asd','asd','2000-10-16',4,'emailjoseph.com');

insert into dbislabwork.reposytoty(Id,Name,firstname,Description,Created,CountOfProjects,email) 
values(2,'github','asd','asd','2000-10-16',4,'emailjoseph.com');

insert into dbislabwork.reposytoty(Id,Name,firstname,Description,Created,CountOfProjects,email) 
values(3,'github','asd','asd','2000-10-16',4,'emailjoseph.com');

select * from dbislabwork.reposytoty;

insert into dbislabwork.project(Id,Name,firstname,Description,Created,CountOfFiles,repositoryId) 
values(1,'github','asd','asd','2000-10-16',4,1);

insert into dbislabwork.project(Id,Name,firstname,Description,Created,CountOfFiles,repositoryId) 
values(2,'github','asd','asd','2000-10-16',4,1);

insert into dbislabwork.project(Id,Name,firstname,Description,Created,CountOfFiles,repositoryId) 
values(3,'github','asd','asd','2000-10-16',4,1);

select * from dbislabwork.project;


insert into dbislabwork.file(Id,Name,file,Version,Created,Rating,projectId) 
values(1,'github','asd','asd','2000-10-16',4,1);

insert into dbislabwork.file(Id,Name,file,Version,Created,Rating,projectId) 
values(2,'github','asd','asd','2000-10-16',4,1);

insert into dbislabwork.file(Id,Name,file,Version,Created,Rating,projectId) 
values(3,'github','asd','asd','2000-10-16',4,1);

select * from dbislabwork.file;



update dbislabwork.user
set NicName = 'dsa' where email = 'emaildima.com';

select NicName from dbislabwork.user;

update dbislabwork.user
set Job = [{Position:'junior',Company:'google',Started:'2000-10-16',Finished:'2000-10-16'}] + Job 
where email = 'emaildima.com';

select Job from dbislabwork.user;

update dbislabwork.user
set firstName = 'dsa' where email = 'emaildima.com';

select firstName from dbislabwork.user;


update dbislabwork.reposytoty
set Name = 'dsa' where Id = 1;

select Name from dbislabwork.reposytoty where Id = 1;

update dbislabwork.reposytoty
set email = 'email' 
where Id = 1;

select email from dbislabwork.reposytoty;

update dbislabwork.reposytoty
set CountOfProjects = 7 where Id = 1;

select CountOfProjects from dbislabwork.reposytoty where Id = 1;

update dbislabwork.project
set Name = 'dsa' where Id = 1;

select Name from dbislabwork.project where Id = 1;

update dbislabwork.project
set CountOfFiles = 4 
where Id = 1;

select CountOfFiles from dbislabwork.project;

update dbislabwork.project
set Description = 'sa' where Id = 1;

select Description from dbislabwork.project where Id = 1;

update dbislabwork.file
set Name = 'dsa' where Id = 1;

select Name from dbislabwork.file where Id = 1;

update dbislabwork.file
set file = 'sad' 
where Id = 1;

select file from dbislabwork.file;

update dbislabwork.file
set Rating = 45 where Id = 1;

select Rating from dbislabwork.file where Id = 1;


create index if not exists on dbislabwork.reposytoty(email);
select * from dbislabwork.reposytoty where email = 'emailjoseph.com';

create index if not exists on dbislabwork.project(repositoryId);
select * from dbislabwork.project where repositoryId = 1;

create index if not exists on dbislabwork.file(projectId);
select * from dbislabwork.file where projectId = 1;

select CountOfFiles,Name from dbislabwork.project where repositoryId = 1;

delete NicName from dbislabwork.user where email = 'emaildima.com';
delete lastname from dbislabwork.user where email = 'emaildima.com';
delete firstname from dbislabwork.user where email = 'emaildima.com';

delete Name from dbislabwork.reposytoty where Id = 1;
delete firstname from dbislabwork.reposytoty where Id = 1;
delete Description from dbislabwork.reposytoty where Id = 1;

delete firstname from dbislabwork.project where Id = 1;
delete Description from dbislabwork.project where Id = 1;
delete Created from dbislabwork.project where Id = 1;

delete Created from dbislabwork.file where Id = 1;
delete Version from dbislabwork.file where Id = 1;
delete Rating from dbislabwork.file where Id = 1;

