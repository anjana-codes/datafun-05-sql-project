-- Start by deleting any tables if the exist already
-- We want to be able to re-run this script as needed.
-- DROP tables in reverse order of creation 
-- DROP dependent tables (with foreign keys) first

DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS directors;



-- Create the directors table 
-- Note that the directors table has no foreign keys, so it is a standalone table

CREATE TABLE Directors (
    DirectorID INT AUTO_INCREMENT PRIMARY KEY,
    Name Text NOT NULL,
    Birth Year INT,
    Nationality TEXT,
    NotableMovies TEXT
);

-- Create the movies table
-- Note that the movies table has a foreign key to the directors table
-- This means that the movies table is dependent on the directors table
-- Be sure to create the standalone directors table BEFORE creating the movies table.

CREATE TABLE Movies (
    MovieID INT AUTO_INCREMENT PRIMARY KEY,
    Title TEXT NOT NULL,
    Year INT,
    Director Text,
    Genre VARCHAR(50),
    Rating DECIMAL(3, 1),
    DirectorID INT,
    FOREIGN KEY (DirectorID) REFERENCES Directors(DirectorID)

);

