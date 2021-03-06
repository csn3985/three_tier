CREATE DATABASE courses;
USE courses;
CREATE TABLE courses (ID INT(30), NAME VARCHAR(20), RATING INT(20), NUMRATINGS INT(20), COMMENTS VARCHAR(10000));
INSERT INTO courses VALUES(1, 'CS150', 2, 4, 'comment1: This was a good class');
INSERT INTO courses VALUES(2, 'CS250', 3, 5, 'This was a terrible class');
INSERT INTO courses VALUES(3, 'CS350', 5, 3, 'The professor was informative');
INSERT INTO courses VALUES(4, 'M150', 5, 3, 'The professor never showed up');
INSERT INTO courses VALUES(5, 'M151', 5, 3, 'I liked the final project');
INSERT INTO courses VALUES(6, 'M200', 5, 3, 'I dropped this course');
