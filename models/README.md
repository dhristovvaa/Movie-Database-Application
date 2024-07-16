# Movie Database CLI Application
This is a command-line Python application for managing a movie database using SQLite. It allows users to list, view, search, add, categorize movies, and mark them as favorites.

# Table of Contents
Installation
Usage
Commands
Database Setup
Project Structure
Contact
Installation
Clone the repository:


Set up a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies (if any):

bash
Copy code
pip install -r requirements.txt
If there are no external dependencies beyond Python's standard library, you can skip this step.

# Usage
To run the application, execute main.py with Python:

bash
Copy code
python main.py <command>
# Commands
movlst: List all movies in the database.
movdt <movie_id>: Show details of a specific movie.
movsrch <query>: Search for movies by title.
movadd <title> <desc> <date> <director> <genre>: Add a new movie.
movfv <movie_id>: Mark a movie as favorite.
movcat <category>: Categorize movies (liked, newest, genre).
Database Setup
The database (movies.db) is initialized using db/setup.py, which creates two tables: movies and favorites.

# Project Structure
main.py: Entry point for the CLI application.
cli/commands.py: Contains functions for handling CLI commands.
models/movie.py: Defines the Movie class for representing movie objects.
db/setup.py: Sets up the SQLite database and creates necessary tables.


# Notes:
Replace placeholders (<command>, <movie_id>, <query>, etc.) with actual values when running commands.
Customize the contact information with your own details.
Provide additional instructions or details specific to your project as needed.