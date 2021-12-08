CREATE DATABASE highlow;

USE highlow;

CREATE TABLE user(
    username varchar(255) NOT NULL,
    score int,
    PRIMARY KEY(username)
);
