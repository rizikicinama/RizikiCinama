import sqlite3
from datetime import datetime, timedelta

class Database:
    """
    A utility class for interacting with an SQLite database for habit tracking.

    Attributes:
        connection (sqlite3.Connection): The SQLite database connection.
    """

    def __init__(self, db_name='test_habits.db'):
        """
        Initializes the Database instance and creates tables if they do not exist.

        Args:
            db_name (str): The name of the database file. Defaults to 'test_habits.db'.
        """
        self.connection = sqlite3.connect(db_name)
        self.create_tables()
        
    def create_tables(self):
        """
        Creates the necessary tables for the habit tracker application if they do not exist.
        """
        with self.connection:
            # Create the 'frequency' table
            self.connection.execute('''CREATE TABLE IF NOT EXISTS frequency (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL UNIQUE
                                      )''')
            # Create the 'habit' table
            self.connection.execute('''CREATE TABLE IF NOT EXISTS habit (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        description TEXT,
                                        frequency_id INTEGER,
                                        startdate DATE,
                                        enddate DATE,
                                        dateadded DATE NOT NULL,
                                        FOREIGN KEY (frequency_id) REFERENCES frequency (id)
                                      )''')
            # Create the 'check_off' table
            self.connection.execute('''CREATE TABLE IF NOT EXISTS check_off (
                                        id INTEGER PRIMARY KEY,
                                        habit_id INTEGER,
                                        check_date DATE NOT NULL,
                                        FOREIGN KEY (habit_id) REFERENCES habit (id)
                                      )''')
            
    def execute_query(self, query, params=()):
        """
        Executes a query that modifies the database (INSERT, UPDATE, DELETE).

        Args:
            query (str): The SQL query to execute.
            params (tuple): The parameters to substitute into the query.

        Returns:
            sqlite3.Cursor: The cursor after executing the query.
        """
        with self.connection:
            cursor = self.connection.execute(query, params)
            self.connection.commit()
        return cursor

    def fetch_all(self, query, params=()):
        """
        Executes a query that retrieves multiple rows from the database (SELECT).

        Args:
            query (str): The SQL query to execute.
            params (tuple): The parameters to substitute into the query.

        Returns:
            list: A list of tuples containing the rows retrieved.
        """
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def fetch_one(self, query, params=()):
        """
        Executes a query that retrieves a single row from the database (SELECT).

        Args:
            query (str): The SQL query to execute.
            params (tuple): The parameters to substitute into the query.

        Returns:
            tuple: A tuple containing the row retrieved, or None if no row was found.
        """
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()
