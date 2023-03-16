#DROP TABLES

author_table_drop = "DROP TABLE IF EXISTS author;"
book_table_drop = "DROP TABLE IF EXISTS book;"

#CREATE TABLES

author_table_create = ("""
    CREATE TABLE IF NOT EXISTS authors (
      id INT PRIMARY KEY,
      book_id INT,
      first_name VARCHAR,
      last_name VARCHAR,
      country VARCHAR
    );
""")

book_table_create = ("""
    CREATE TABLE IF NOT EXISTS books (
        book_id INT PRIMARY KEY,
        title VARCHAR,
        publisher VARCHAR,
        cost INT
    );
""")

#INSERT RECORDS

author_table_insert = ("""
    INSERT INTO authors (id, book_id, first_name, last_name, country)
    VALUES (%s, %s, %s, %s, %s);
""")

book_table_insert = ("""
    INSERT INTO books (book_id, title, publisher, cost)
    VALUES (%s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

#FIND AUTHORS

author_select = ("""
    SELECT a.country, b.title
    FROM authors a
    INNER JOIN books b
    ON a.id = b.book_id
    WHERE a.first_name = %s AND a.last_name = %s AND b.publisher = %s;
""")

#QUERY LISTS

create_table_queries = [author_table_create, book_table_create]

drop_table_queries = [author_table_drop, book_table_drop]
