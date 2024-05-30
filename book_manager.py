import sqlite3
import pandas as pd 
import pathlib
import csv

# Define the database file in the current root project directory
db_file = "C:\\Users\\AnjanaD\\Documents\\datafun-05-sql-project\\project.db"

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = "C:\\Users\\AnjanaD\\Documents\\datafun-05-sql-project\\create_tables.sql"
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)


def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        directors_data_path = pathlib.Path("data", "directors.csv")
        movies_data_path = pathlib.Path("data", "movies.csv")
        directors_df = pd.read_csv(directors_data_path)
        movies_df = pd.read_csv(movies_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            directors_df.to_sql("Directors", conn, if_exists="replace", index=False)
            movies_df.to_sql("Movies", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

def main():
    create_database()
    create_tables()
    insert_data_from_csv()

if __name__ == "__main__":
    main()