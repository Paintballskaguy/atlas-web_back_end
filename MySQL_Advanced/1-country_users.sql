-- creates the table users if it doesn't exist


CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
    country CHAR(2) NOT NULL DEFAULT 'US',
    CHECK (country IN ('US', 'CO', 'TN'))
); 