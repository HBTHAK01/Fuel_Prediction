CREATE DATABASE Fuel_Database;

CREATE TABLE Fuel_Database.Usercredentials (
id INT NOT NULL AUTO_INCREMENT,
username varchar(50) NOT NULL unique,
password varchar(150) NOT NULL,
PRIMARY KEY (id)
);

CREATE TABLE Fuel_Database.Clientinformation (
userid varchar(50) NOT NULL unique,
name varchar(50) NOT NULL,
email varchar(50) NOT NULL,
address1 varchar(100) NOT NULL,
address2 varchar(100),
city varchar(100) NOT NULL,
state varchar(2) NOT NULL,
zipcode varchar(9) NOT NULL,
PRIMARY KEY (email)
);

CREATE TABLE Fuel_Database.Fuelquote (
userid varchar(50) NOT NULL,
gallons float NOT NULL,
deliveryaddress varchar(150) NOT NULL,
deliverydate varchar(10) NOT NULL,
pergallon float NOT NULL,
total float NOT NULL
);
