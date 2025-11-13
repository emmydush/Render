-- SQL script for setting up the database and user for pgAdmin
-- This assumes you're using the default PostgreSQL installation

-- Connect to PostgreSQL as superuser (usually postgres) and run these commands:

-- Create database if it doesn't exist
SELECT 'CREATE DATABASE myapp'
WHERE NOT EXISTS (
    SELECT FROM pg_database
    WHERE datname = 'myapp'
)\gexec

-- Connect to the myapp database
\c myapp

-- Create the users table if it doesn't exist
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data (optional)
INSERT INTO users (name, email) VALUES 
    ('Alice Smith', 'alice@example.com'),
    ('Bob Johnson', 'bob@example.com'),
    ('Carol Williams', 'carol@example.com')
ON CONFLICT (email) DO NOTHING;

-- Create a dedicated user for the application (optional but recommended)
-- Uncomment the following lines if you want to create a dedicated user:
-- CREATE USER myapp_user WITH PASSWORD 'Jesuslove@12';
-- GRANT ALL PRIVILEGES ON TABLE users TO myapp_user;
-- GRANT USAGE, SELECT ON SEQUENCE users_id_seq TO myapp_user;

-- Grant necessary permissions
GRANT ALL PRIVILEGES ON TABLE users TO postgres;
GRANT USAGE, SELECT ON SEQUENCE users_id_seq TO postgres;

-- Verify the setup
SELECT * FROM users;