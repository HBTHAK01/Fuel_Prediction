CREATE DATABASE Fuel_Database;

CREATE TABLE Fuel_Database.Usercredentials (
username varchar(50) NOT NULL,
password varchar(150) NOT NULL,
PRIMARY KEY (username)
);

CREATE TABLE Fuel_Database.Clientinformation (
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
gallons int  NOT NULL,
deliverydate varchar(10) NOT NULL
);