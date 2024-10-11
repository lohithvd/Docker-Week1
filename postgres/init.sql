
CREATE USER "myuser" WITH ENCRYPTED PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE mydb TO "myuser";



\connect mydb;

CREATE TABLE my_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);
GRANT ALL PRIVILEGES ON TABLE my_table TO "myuser";

INSERT INTO my_table (name) VALUES ('Item 1'), ('Item 2'), ('Item 3');
