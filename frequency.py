class Frequency:
    """
    A class to manage the frequency of habits in the habit tracker application.

    Attributes:
        db (Database): The database instance to interact with.
        name (str): The name of the frequency.
    """

    def __init__(self, db, name=None):
        """
        Initializes the Frequency instance.

        Args:
            db (Database): The database instance to interact with.
            name (str, optional): The name of the frequency. Defaults to None.
        """
        self.db = db
        self.name = name

    def save(self):
        """
        Saves a new frequency to the database.
        """
        query = 'INSERT INTO frequency (name) VALUES (?)'
        self.db.execute_query(query, (self.name,))

    @staticmethod
    def get_all(db):
        """
        Retrieves all frequencies from the database.

        Args:
            db (Database): The database instance to interact with.

        Returns:
            list: A list of tuples containing all frequencies.
        """
        query = 'SELECT * FROM frequency'
        return db.fetch_all(query)

    @staticmethod
    def update(db, frequency_id, name):
        """
        Updates the name of an existing frequency in the database.

        Args:
            db (Database): The database instance to interact with.
            frequency_id (int): The ID of the frequency to update.
            name (str): The new name of the frequency.
        """
        query = 'UPDATE frequency SET name = ? WHERE id = ?'
        db.execute_query(query, (name, frequency_id))

    @staticmethod
    def delete(db, frequency_id):
        """
        Deletes a frequency from the database.

        Args:
            db (Database): The database instance to interact with.
            frequency_id (int): The ID of the frequency to delete.
        """
        query = 'DELETE FROM frequency WHERE id = ?'
        db.execute_query(query, (frequency_id,))
