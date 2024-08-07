import fire
from dbutil import Database
from habit import Habit
from frequency import Frequency
from checkoff import CheckOff
from habitanalysis import HabitAnalysis

class ManageDB:
    """
    A class to manage the database operations for the Habit Tracker application.
    
    Attributes:
        db (Database): The database instance to interact with.
    """

    def __init__(self, db_name='test_habits.db'):
        """
        Initializes the ManageDB instance with a database connection.
        
        Args:
            db_name (str): The name of the database file.
        """
        self.db = Database(db_name)
    
    # Frequency Management

    def add_frequency(self, name):
        """
        Adds a new frequency to the database.
        
        Args:
            name (str): The name of the frequency.
        """
        frequency = Frequency(self.db, name)
        frequency.save()
        print(f"Added frequency: {name}")
    
    def update_frequency(self, frequency_id, name):
        """
        Updates an existing frequency in the database.
        
        Args:
            frequency_id (int): The ID of the frequency to update.
            name (str): The new name of the frequency.
        """
        Frequency.update(self.db, frequency_id, name)
        print(f"Updated frequency {frequency_id} to {name}")
    
    def delete_frequency(self, frequency_id):
        """
        Deletes a frequency from the database.
        
        Args:
            frequency_id (int): The ID of the frequency to delete.
        """
        Frequency.delete(self.db, frequency_id)
        print(f"Deleted frequency {frequency_id}")
    
    def list_frequencies(self):
        """
        Lists all frequencies in the database.
        """
        frequencies = Frequency.get_all(self.db)
        for freq in frequencies:
            print(freq)

    # Habit Management

    def add_habit(self, name, description, frequency_id, startdate=None, enddate=None):
        """
        Adds a new habit to the database.
        
        Args:
            name (str): The name of the habit.
            description (str): The description of the habit.
            frequency_id (int): The ID of the frequency associated with the habit.
            startdate (str): The start date of the habit (optional).
            enddate (str): The end date of the habit (optional).
        """
        habit = Habit(self.db, name, description, frequency_id, startdate, enddate)
        habit.save()
        print(f"Added habit: {name}")
    
    def update_habit(self, habit_id, name, description, frequency_id, startdate=None, enddate=None):
        """
        Updates an existing habit in the database.
        
        Args:
            habit_id (int): The ID of the habit to update.
            name (str): The new name of the habit.
            description (str): The new description of the habit.
            frequency_id (int): The new frequency ID associated with the habit.
            startdate (str): The new start date of the habit (optional).
            enddate (str): The new end date of the habit (optional).
        """
        Habit.update(self.db, habit_id, name, description, frequency_id, startdate, enddate)
        print(f"Updated habit {habit_id}")
    
    def delete_habit(self, habit_id):
        """
        Deletes a habit from the database.
        
        Args:
            habit_id (int): The ID of the habit to delete.
        """
        Habit.delete(self.db, habit_id)
        print(f"Deleted habit {habit_id}")
    
    def list_habits(self):
        """
        Lists all habits in the database.
        """
        habits = Habit.get_all(self.db)
        for habit in habits:
            print(habit)

    # CheckOff Management

    def add_checkoff(self, habit_id, check_date):
        """
        Adds a new checkoff to the database.
        
        Args:
            habit_id (int): The ID of the habit.
            check_date (str): The date of the checkoff.
        """
        checkoff = CheckOff(self.db, habit_id, check_date)
        checkoff.save()
        print(f"Added checkoff for habit {habit_id} on {check_date}")
    
    def update_checkoff(self, checkoff_id, habit_id, check_date):
        """
        Updates an existing checkoff in the database.
        
        Args:
            checkoff_id (int): The ID of the checkoff to update.
            habit_id (int): The ID of the habit.
            check_date (str): The new date of the checkoff.
        """
        CheckOff.update(self.db, checkoff_id, habit_id, check_date)
        print(f"Updated checkoff {checkoff_id}")
    
    def delete_checkoff(self, checkoff_id):
        """
        Deletes a checkoff from the database.
        
        Args:
            checkoff_id (int): The ID of the checkoff to delete.
        """
        CheckOff.delete(self.db, checkoff_id)
        print(f"Deleted checkoff {checkoff_id}")
    
    def list_checkoffs(self):
        """
        Lists all checkoffs in the database.
        """
        checkoffs = CheckOff.get_all(self.db)
        for checkoff in checkoffs:
            print(checkoff)

    def list_checkoffs_by_habit(self, habit_id):
        """
        Lists all checkoffs for a specific habit.
        
        Args:
            habit_id (int): The ID of the habit.
        """
        checkoffs = CheckOff.get_by_habit(self.db, habit_id)
        for checkoff in checkoffs:
            print(checkoff)

    # Analysis Functions

    def get_all_habits(self):
        """
        Lists all currently tracked habits.
        """
        habit_analysis = HabitAnalysis(self.db)
        habits = habit_analysis.get_all_habits()
        for habit in habits:
            print(habit)

    def get_habits_by_frequency(self, frequency_name):
        """
        Lists all habits with a specified frequency.
        
        Args:
            frequency_name (str): The name of the frequency (e.g., 'Daily', 'Weekly').
        """
        habit_analysis = HabitAnalysis(self.db)
        habits = habit_analysis.get_habits_by_frequency(frequency_name)
        for habit in habits:
            print(habit)

    def get_longest_streak(self):
        """
        Retrieves the habit with the longest streak.
        """
        habit_analysis = HabitAnalysis(self.db)
        habit, streak = habit_analysis.get_longest_streak()
        print(f"Longest Streak Habit: {habit}")
        print(f"Longest Streak Length: {streak}")

    def get_habit_streak(self, habit_id):
        """
        Retrieves the streak for a specific habit.
        
        Args:
            habit_id (int): The ID of the habit.
        """
        habit_analysis = HabitAnalysis(self.db)
        frequency_name = self.db.fetch_one('SELECT name FROM frequency WHERE id = (SELECT frequency_id FROM habit WHERE id = ?)', (habit_id,))[0]
        streak = habit_analysis.get_habit_streak(habit_id, frequency_name)
        print(f"Longest Streak for Habit {habit_id} ({frequency_name}): {streak}")

if __name__ == '__main__':
    fire.Fire(ManageDB)
