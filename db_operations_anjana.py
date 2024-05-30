import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root project directory
db_file = "C:\\Users\\AnjanaD\\Documents\\datafun-05-sql-project\\project.db"

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

def select_records():
    """Function to select all records in the authors table"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("select_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Records read successfully.")
    except sqlite3.Error as e:
        print("Error reading records:", e)


def filter_records():
    """Function to filter movies data based on conditions"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("filter_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            results = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]
            print(" | ".join(column_names))
            print("-" * (len(" | ".join(column_names)) + 10))
            for row in results:
                 print(" | ".join(map(str, row)))  
    except sqlite3.Error as e:
        print("Error filtering book data:", e)

def sort_records() :
    """Function to filter movies data based on conditions"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sort_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            results = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]
            print(" | ".join(column_names))
            print("-" * (len(" | ".join(column_names)) + 10))
            for row in results:
                 print(" | ".join(map(str, row)))  
    except sqlite3.Error as e:
        print("Error filtering book data:", e)


 


def main():
    insert_data_from_csv()
    select_records()
    filter_records()
    sort_records()
   

if __name__ == "__main__":
    main()
