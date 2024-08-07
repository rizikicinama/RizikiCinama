import unittest
from dbutil import Database
from habit import Habit
from frequency import Frequency
from checkoff import CheckOff
from habitanalysis import HabitAnalysis
from datetime import datetime

# Test Suite for habits. Analysis methods are tested against the test data, destructive tests use a temporary database
class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.db = Database('test_habits.db')
	# Temp DB
        self.tempdb = Database(db_name=':memory:')  # Use in-memory database for desctructive tests
        self.tempdb.create_tables()  # Ensure tables are created

    # Test Longest streak from DB
    def test_longest_streak(self):
        """Test the longest streak in the database"""
        habit_analysis = HabitAnalysis(self.db)
        habit, streak = habit_analysis.get_longest_streak()
        self.assertEqual(streak, 90) # Longest steak in the database is 90.
    
    # Test Get frequency in DB
    def test_frequency_exists(self):
        """Test if the Daily frequency exists in the database"""
        freq_id = self.db.fetch_one("SELECT id FROM frequency WHERE name = ?", ("Daily",))[0]
        result = self.db.fetch_one("SELECT * FROM frequency WHERE id = ?", (freq_id,))
        self.assertIsNotNone(result)

    # Test Longest streak from DB
    def test_longest_streak_for_a_habbit(self):
        """Test the streak for a specified habit"""
        habit_analysis = HabitAnalysis(self.db)
        streak = habit_analysis.get_habit_streak(4, 'Weekly')
        self.assertEqual(streak, 1)

    # Test Habit Creation using temp DB
    def test_create_habbit(self):
        test_name = "Test Habbit"
        habit = Habit(self.tempdb, test_name, "Test Description", 1, '', '')
        habit.save()
        result = self.tempdb.fetch_one("SELECT * FROM habit WHERE name = ?", (test_name,))
        self.assertIsNotNone(result)

    # Test Habit Edit using temp DB
    def test_edit_habbit(self):
        test_name = "Test Habbit"
        new_name = "Updated Name"
        new_desc = "New Description"
        new_start = "2024-07-01"
        new_end = "2024-07-30"
        new_freq = 2
        habit = Habit(self.tempdb, test_name, "Test Description", 1, '', '')
        habit.save()
        result = self.tempdb.fetch_one("SELECT id FROM habit WHERE name = ?", (test_name,))[0]
        Habit.update(self.tempdb, result, new_name, new_desc, new_freq, new_start, new_end)
        result2 = self.tempdb.fetch_one("SELECT id FROM habit WHERE name = ? AND description = ? AND frequency_id = ? AND startdate = ? AND enddate = ?", (new_name,new_desc,new_freq,new_start,new_end,))
        self.assertIsNotNone(result2)

    # Test Delete Habit using temp DB
    def test_delete_habit(self):
        """Test deleting a habit."""
        test_name = "Test Habbit"
        habit = Habit(self.tempdb, test_name, "Test Description", 1, '', '')
        habit.save()
        habit_id = self.tempdb.fetch_one("SELECT id FROM habit WHERE name = ?", (test_name,))[0]
        Habit.delete(self.tempdb, habit_id)
        result = self.tempdb.fetch_one("SELECT * FROM habit WHERE id = ?", (habit_id,))
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()