-- Set a default to an entity in a database table if no value is specified and all id values should be unique.
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256), UNIQUE(id));
