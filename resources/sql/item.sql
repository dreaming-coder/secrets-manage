create table if not exists item(
    id integer primary key autoincrement ,
    user_id integer not null,
    title text not null ,
    account text not null ,
    password text not null ,
    notes text,
    create_time text not null ,
    update_time text not null
);