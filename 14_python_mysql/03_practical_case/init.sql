create database py_sql charset utf8;
use py_sql;

create table orders(
   order_date date,
   order_id varchar(255),
   money int,
   province varchar(10)
);