-- Drop the table if it exists to ensure a clean slate for new schema
-- In a real application, you would use migration tools (e.g., Flask-Migrate)
-- instead of dropping tables, especially in production.
DROP TABLE IF EXISTS app2_data;

-- Create a table for app1 with separate title and content columns
CREATE TABLE IF NOT EXISTS app2_data (
    id SERIAL PRIMARY KEY, -- Uniquely generated ID
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Insert some initial data (optional)
INSERT INTO app2_data (title, content) VALUES ('First Note Title', 'This is the content of my very first note.');
INSERT INTO app2_data (title, content) VALUES ('Another Important Note', 'Here is some more detailed information for the second note.');