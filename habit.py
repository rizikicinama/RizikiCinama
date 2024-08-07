from datetime import datetime, timedelta

class Habit:
    """
    A class to manage habits in the habit tracker application.

    Attributes:
        db (Database): The database instance to interact with.
        name (str): The name of the habit.
        description (str): A brief description of the habit.
        frequency_id (int): The ID of the frequency associated with the habit.
        startdate (date): The start date of the habit.
        enddate (date): The end date of the habit.
        dateadded (date): The date when the habit was added.
    """

    def __init__(self, db, name=None, description=None, frequency_id=None, startdate=None, enddate=None):
        """
        Initializes the Habit instance.

        Args:
            db (Database): The database instance to interact with.
            name (str, optional): The name of the habit. Defaults to None.
            description (str, optional): A brief description of the habit. Defaults to None.
            frequency_id (int, optional): The ID of the frequency associated with the habit. Defaults to None.
            startdate (date, optional): The start date of the habit. Defaults to None.
            enddate (date, optional): The end date of the habit. Defaults to None.
        """
        self.db = db
        self.name = name
        self.description = description
        self.frequency_id = frequency_id
        self.startdate = startdate
        self.enddate = enddate
        self.dateadded = datetime.now().date()

    def save(self):
        """
        Saves a new habit to the database.
        """
        query = '''INSERT INTO habit (name, description, frequency_id, startdate, enddate, dateadded) 
                   VALUES (?, ?, ?, ?, ?, ?)'''
        self.db.execute_query(query, (self.name, self.description, self.frequency_id, self.startdate, self.enddate, self.dateadded))

    @staticmethod
    def get_all(db):
        """
        Retrieves all habits from the database.

        Args:
            db (Database): The database instance to interact with.

        Returns:
            list: A list of tuples containing all habits.
        """
        query = 'SELECT * FROM habit'
        return db.fetch_all(query)

    @staticmethod
    def update(db, habit_id, name, description, frequency_id, startdate, enddate):
        """
        Updates an existing habit in the database.

        Args:
            db (Database): The database instance to interact with.
            habit_id (int): The ID of the habit to update.
            name (str): The new name of the habit.
            description (str): The new description of the habit.
            frequency_id (int): The new frequency ID of the habit.
            startdate (date): The new start date of the habit.
            enddate (date): The new end date of the habit.
        """
        query = '''UPDATE habit SET name = ?, description = ?, frequency_id = ?, startdate = ?, enddate = ? WHERE id = ?'''
        db.execute_query(query, (name, description, frequency_id, startdate, enddate, habit_id))

    @staticmethod
    def delete(db, habit_id):
        """
        Deletes a habit from the database, along with its check-off entries.

        Args:
            db (Database): The database instance to interact with.
            habit_id (int): The ID of the habit to delete.
        """
        query = 'DELETE FROM habit WHERE id = ?'
        db.execute_query(query, (habit_id,))
        
        # Also delete associated check-off entries
        query = 'DELETE FROM check_off WHERE habit_id = ?'
        db.execute_query(query, (habit_id,))
