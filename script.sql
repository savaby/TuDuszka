CREATE TABLE TODO (
    id integer primary key autoincrement,
    title string,
    type_id int not null,
    todo_text string,
    create_date date not null,
    end_date date
);

create table types (
    id integer primary key autoincrement,
    name string(20)
);

insert into types(name) values('urgent');
insert into types(name) values('daily');
insert into types(name) values('simple');