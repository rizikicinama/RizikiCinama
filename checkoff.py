from datetime import datetime

class CheckOff:
    """
    Represents a check-off for a habit, which records the date a habit was completed.

    Attributes:
        db (Database): The database connection instance.
        habit_id (int): The ID of the habit associated with this check-off.
        check_date (str): The date the habit was completed.
    """

    def __init__(self, db, habit_id=None, check_date=None):
        """
        Initializes a new CheckOff instance.

        Args:
            db (Database): The database connection instance.
            habit_id (int, optional): The ID of the habit associated with this check-off.
            check_date (str, optional): The date the habit was completed.
        """
        self.db = db
        self.habit_id = habit_id
        self.check_date = check_date
        
    def save(self):
        """
        Saves the check-off to the database by inserting a new record.

        Raises:
            DatabaseError: If there is an issue with the database operation.
        """
        query = 'INSERT INTO check_off (habit_id, check_date) VALUES (?, ?)'
        self.db.execute_query(query, (self.habit_id, self.check_date))

    @staticmethod
    def get_all(db):
        """
        Retrieves all check-offs from the database.

        Args:
            db (Database): The database connection instance.

        Returns:
            list: A list of all check-offs in the database.
        """
        query = 'SELECT * FROM check_off'
        return db.fetch_all(query)
    
    @staticmethod
    def get_checkdates_for_habit(db, habit_id):
        """
        Retrieves all check-off dates for a specific habit, ordered by date.

        Args:
            db (Database): The database connection instance.
            habit_id (int): The ID of the habit.

        Returns:
            list: A list of date objects representing the check-off dates.

        Raises:
            ValueError: If a date string in the database cannot be parsed.
        """
        data_list = db.fetch_all('SELECT check_date FROM check_off WHERE habit_id = ? ORDER BY check_date', (habit_id,))
        date_objects = []
        for date_str in data_list:
            try:
                datetime_obj = datetime.strptime(date_str[0], '%Y-%m-%d %H:%M:%S')
                date_objects.append(datetime_obj.date())
            except ValueError:
                print(f"Invalid date format: {date_str}")
        return date_objects

    @staticmethod
    def get_by_habit(db, habit_id):
        """
        Retrieves all check-offs for a specific habit.

        Args:
            db (Database): The database connection instance.
            habit_id (int): The ID of the habit.

        Returns:
            list: A list of check-offs for the specified habit.
        """
        query = 'SELECT * FROM check_off WHERE habit_id = ?'
        return db.fetch_all(query, (habit_id,))

    @staticmethod
    def update(db, checkoff_id, habit_id, check_date):
        """
        Updates a check-off record in the database.

        Args:
            db (Database): The database connection instance.
            checkoff_id (int): The ID of the check-off to update.
            habit_id (int): The ID of the habit associated with this check-off.
            check_date (str): The new check-off date.

        Raises:
            DatabaseError: If there is an issue with the database operation.
        """
        query = 'UPDATE check_off SET habit_id = ?, check_date = ? WHERE id = ?'
        db.execute_query(query, (habit_id, check_date, checkoff_id))

    @staticmethod
    def delete(db, checkoff_id):
        """
        Deletes a check-off record from the database.

        Args:
            db (Database): The database connection instance.
            checkoff_id (int): The ID of the check-off to delete.

        Raises:
            DatabaseError: If there is an issue with the database operation.
        """
        query = 'DELETE FROM check_off WHERE id = ?'
        db.execute_query(query, (checkoff_id,))
