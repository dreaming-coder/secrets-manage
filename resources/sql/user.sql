create table if not exists user(
    id integer primary key autoincrement ,
    phone char(11) unique not null ,
    email text unique not null ,
    name text not null ,
    password text not null ,
    create_time text not null,
    last_login_time text
);