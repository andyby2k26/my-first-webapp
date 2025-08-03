-- Create a table for app1
CREATE TABLE IF NOT EXISTS app1_data (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Insert some initial data (optional)
INSERT INTO app1_data (name) VALUES ('Initial entry for App 1');
INSERT INTO app1_data (name) VALUES ('Another entry for App 1');