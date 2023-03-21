USE master
GO

IF DB_ID('develop') IS NOT NULL
BEGIN
    ALTER DATABASE develop SET SINGLE_USER WITH ROLLBACK IMMEDIATE
    DROP DATABASE develop
END

CREATE DATABASE develop;
GO

USE develop;
GO

CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    email VARCHAR(100),
    created_at DATETIME DEFAULT GETDATE()
);

DECLARE @counter INT = 1;
WHILE @counter <= 1000
BEGIN
    INSERT INTO users (id, name, age, email) VALUES (
        @counter,
        'User ' + CAST(@counter AS VARCHAR),
        ABS(CHECKSUM(NEWID())) % 80 + 18, 
        'user' + CAST(@counter AS VARCHAR) + '@example.com'
    );
    SET @counter += 1;
END
