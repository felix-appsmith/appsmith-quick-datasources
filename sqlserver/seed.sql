USE master;

CREATE TABLE users (
id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
username VARCHAR(50) NOT NULL,
email VARCHAR(100) NOT NULL,
age INT,
bio TEXT,
avatar VARBINARY(MAX),
is_active BIT,
created_at DATETIME2 DEFAULT CURRENT_TIMESTAMP,
data NVARCHAR(MAX),
salary DECIMAL(10, 2)
);

DECLARE @counter INT = 1;

WHILE @counter <= 1000
BEGIN
    INSERT INTO master.dbo.users (username, email, age, bio, avatar, is_active, created_at, data, salary)
    VALUES (
        CONCAT('user', @counter),
        CONCAT('user', @counter, '@example.com'),
        ROUND(RAND() * 50 + 20, 0),
        CONCAT('I am a ',
            CASE WHEN RAND() < 0.5 THEN 'software developer' ELSE 'teacher' END,
            ' from ',
            CASE WHEN RAND() < 0.5 THEN 'New York' ELSE 'Los Angeles' END
        ),
        NULL,
        CAST(RAND() * 2 AS BIT),
        GETDATE(),
        '{ "key1": "value1", "key2": "value2" }',
        ROUND(RAND() * 50000 + 5000, 2)
    );
    SET @counter += 1;
END;





