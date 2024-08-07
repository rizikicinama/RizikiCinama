# Habit Tracker

A habit tracking application that helps users to create, track, and analyze their habits. The application supports adding habits with various frequencies, marking them as complete, and analyzing streaks.

## 1. Features

- **Habit Management**: Add, update, and delete habits with descriptions, start and end dates.
- **Frequency Management**: Set different frequencies for habits such as daily, weekly, etc.
- **Check-Offs**: Mark habits as completed on specific dates.
- **Analysis**: Analyze habits to find the longest streaks and categorize habits by frequency.

## 2. Getting Started

### 2.1 Prerequisites

- Python 3.x
- SQLite3

### 2.2 Installation

Clone the repository:

   ```bash
   git clone https://github.com/rizikicinama/RizikiCinama.git
   cd RizikiCinama
   ```

### 2.3 To install the dependencies:

   ```bash 
   pip install -r requirements.txt
   ```

## 3. Usage

### 3.1 Database Setup: 
The application uses an SQLite database. You can customize the  database name in the dbutil.py file or leave it as test_habits.db for development purposes.

### 3.2 Managing Habits and Frequencies: 
Use the manage module to add, update, or delete habits and frequencies. Please note that if you are using MacOS or Linux you need to use python3 and not python to execute the commands.

### 3.3 Running the Application: 
Use command-line interface to interact with the application, leveraging the "fire" library.

## 4. Example Commands

### 4.1 Add a new frequency:

To add a new frequency:

   ```bash 
   python -m manage add_frequency "Daily"
   ```

### 4.2 Add a new habit:

To add a new habit:
   ```bash 
   python -m manage add_habit "Exercise" "Morning routine" 1 "2024-01-01" "2024-12-31"
   ```

### 4.3 List all habits:

To check all habits:
   ```bash 
   python -m manage list_habits
   ```

### 4.4 Analyze longest streak:

To analyse the checkOffs and identify the longest streak:

   ```bash
   python -m manage get_longest_streak
   ```

## 5. Running Tests:

To run tests:

   ```bash 
   python -m unittest discover
   ```


