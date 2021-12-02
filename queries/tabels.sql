/*
 *CREATE TABLE user(
 *    ID int NOT NULL,
 *    username varchar(255) NOT NULL,
 *    PRIMARY KEY(ID)
 *);
 */

CREATE TABLE score(
    scoreID int NOT NULL,
    ID int,
    score int,
    PRIMARY KEY(scoreID),
    FOREIGN KEY (ID)  REFERENCES user(ID)
);

CREATE TABLE tries(
    triesID int NOT NULL,
    ID int,
    num_fails int,
    num_successes int,
    PRIMARY KEY(triesID),
    FOREIGN KEY (ID)  REFERENCES user(ID)
);
