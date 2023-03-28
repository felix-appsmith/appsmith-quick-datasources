

CREATE TABLE users (
id SERIAL PRIMARY KEY,
username VARCHAR(50) NOT NULL,
email VARCHAR(100) NOT NULL,
age INT,
bio TEXT,
avatar BYTEA,
is_active BOOLEAN,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
data JSONB,
salary NUMERIC(10, 2)
);

DO $$
DECLARE counter INT := 1;
BEGIN
  WHILE counter <= 1000 LOOP
    INSERT INTO public.users (username, email, age, bio, avatar, is_active, created_at, data, salary)
    VALUES (
        CONCAT('user', counter),
        CONCAT('user', counter, '@example.com'),
        CAST(RANDOM() * 50 + 20 AS NUMERIC),
        CONCAT('I am a ',
            CASE WHEN RANDOM() < 0.5 THEN 'software developer' ELSE 'teacher' END,
            ' from ',
            CASE WHEN RANDOM() < 0.5 THEN 'New York' ELSE 'Los Angeles' END
        ),
        NULL,
        CASE WHEN RANDOM() < 0.5 THEN TRUE ELSE FALSE END,
        CURRENT_TIMESTAMP,
        '{ "key1": "value1", "key2": "value2" }'::JSONB,
        CAST(RANDOM() * 50000 + 5000 AS NUMERIC(10, 2))
    );
    counter := counter + 1;
  END LOOP;
END $$;
