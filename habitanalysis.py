from dbutil import Database
from habit import Habit
from datetime import datetime, timedelta
from checkoff import CheckOff

# Analytics module for the Habit Tracker application
class HabitAnalysis:
    """
    A class to perform various analytics on habits.

    Attributes:
        db (Database): The database instance to interact with.
    """

    def __init__(self, db: Database):
        """
        Initializes the HabitAnalysis instance.

        Args:
            db (Database): The database instance to interact with.
        """
        self.db = db

    def get_all_habits(self):
        """
        Retrieves all habits from the database.

        Returns:
            list: A list of tuples containing all habits.
        """
        return Habit.get_all(self.db)

    def get_habits_by_frequency(self, frequency_name):
        """
        Retrieves all habits with a specified frequency.

        Args:
            frequency_name (str): The name of the frequency (e.g., 'Daily', 'Weekly').

        Returns:
            list: A list of tuples containing habits with the specified frequency.
        """
        query = '''SELECT habit.* FROM habit
                   JOIN frequency ON habit.frequency_id = frequency.id
                   WHERE frequency.name = ?'''
        return self.db.fetch_all(query, (frequency_name,))

    def get_longest_streak(self):
        """
        Calculates the longest streak across all habits.

        Returns:
            tuple: A tuple containing the habit with the longest streak and the streak length.
        """
        habits = self.get_all_habits()
        longest_streak = 0
        longest_streak_habit = None

        for habit in habits:
            streak = self.get_habit_streak(habit[0], habit[3])
            if streak > longest_streak:
                longest_streak = streak
                longest_streak_habit = habit

        return longest_streak_habit, longest_streak

    def get_habit_streak(self, habit_id, frequency_id):
        """
        Calculates the longest streak for a specified habit.

        Args:
            habit_id (int): The ID of the habit.
            frequency_id (int): The ID of the frequency associated with the habit.

        Returns:
            int: The longest streak length for the specified habit.
        """
        check_dates = CheckOff.get_checkdates_for_habit(self.db, habit_id)

        if not check_dates:
            return 0

        streak = 1
        max_streak = 1

        # Daily habit streak calculation
        if frequency_id == 1:
            for i in range(1, len(check_dates)):
                if check_dates[i] - check_dates[i - 1] == timedelta(days=1):
                    streak += 1
                    max_streak = max(max_streak, streak)
                else:
                    streak = 1

        # Weekly habit streak calculation
        elif frequency_id == 2:
            for i in range(1, len(check_dates)):
                if check_dates[i] - check_dates[i - 1] == timedelta(weeks=1):
                    streak += 1
                    max_streak = max(max_streak, streak)
                else:
                    streak = 1

        return max_streak
