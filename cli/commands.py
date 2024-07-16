import sqlite3
from models.movie import Movie


def list_movies():
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    c.execute('SELECT * FROM movies')
    movies = c.fetchall()

    for movie in movies:
        print(Movie(*movie))

    conn.close()


def movie_details(movie_id):
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    c.execute('SELECT * FROM movies WHERE id = ?', (movie_id,))
    movie = c.fetchone()

    if movie:
        print(Movie(*movie))
    else:
        print(f"No movie found with id {movie_id}")

    conn.close()


def search_movies(query):
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    c.execute('SELECT * FROM movies WHERE title LIKE ?', (f'%{query}%',))
    movies = c.fetchall()

    for movie in movies:
        print(Movie(*movie))

    conn.close()


def add_movie(title, desc, date, director, genre):
    conn = None
    try:
        # Validate input data
        if not all([title, desc, date, director, genre]):
            raise ValueError("All fields (title, description, release date, director, genre) are required.")

        conn = sqlite3.connect('movies.db')
        c = conn.cursor()

        c.execute('''
        INSERT INTO movies (title, description, release_date, director, genre)
        VALUES (?, ?, ?, ?, ?)
        ''', (title, desc, date, director, genre))

        conn.commit()
        print("Movie added successfully")

    except (sqlite3.Error, ValueError) as e:
        print(f"Error adding movie: {e}")

    finally:
        if conn:
            conn.close()


def favorite_movie(movie_id):
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    c.execute('INSERT INTO favorites (movie_id) VALUES (?)', (movie_id,))

    conn.commit()
    conn.close()
    print(f"Movie with id {movie_id} added to favorites")


def categorize_movies(category):
    conn = None
    try:
        conn = sqlite3.connect('movies.db')
        c = conn.cursor()

        if category == 'liked':
            c.execute('''
                SELECT movies.* FROM movies
                JOIN favorites ON movies.id = favorites.movie_id
                LIMIT 5
                ''')
        elif category == 'newest':
            c.execute('SELECT * FROM movies ORDER BY release_date DESC LIMIT 5')
        elif category == 'genre':
            c.execute('SELECT * FROM movies GROUP BY genre ORDER BY COUNT(*) DESC LIMIT 5')
        else:
            print(f"Unknown category: {category}")
            return

        movies = c.fetchall()

        for movie in movies:
            print(Movie(*movie))  # Assuming `movie` contains all required fields for Movie object

    except sqlite3.Error as e:
        print(f"Error retrieving categorized movies: {e}")

    finally:
        if conn:
            conn.close()


def remove_movie(movie_id):
    conn = None
    try:
        conn = sqlite3.connect('movies.db')
        c = conn.cursor()

        c.execute('SELECT * FROM movies WHERE id = ?', (movie_id,))
        movie = c.fetchone()

        if movie:

            c.execute('DELETE FROM movies WHERE id = ?', (movie_id,))
            conn.commit()
            print(f"Movie with id {movie_id} removed successfully")
        else:
            print(f"No movie found with id {movie_id}")

    except sqlite3.Error as e:
        print(f"Error removing movie: {e}")

    finally:
        if conn:
            conn.close()


def like_movie(self, movie_id):
    conn = self.conn
    c = self.cursor

    try:
        c.execute('UPDATE movies SET likes = likes + 1 WHERE id = ?', (movie_id,))
        conn.commit()
        print(f"Movie with id {movie_id} liked successfully")
    except sqlite3.Error as e:
        print(f"Error liking movie: {e}")


def get_top_liked_movies(self, limit=5):
    conn = self.conn
    c = self.cursor

    try:
        c.execute('''
                SELECT id, title, description, release_date, director, genre, likes
                FROM movies
                ORDER BY likes DESC
                LIMIT ?
            ''', (limit,))
        movies = c.fetchall()
        return movies
    except sqlite3.Error as e:
        print(f"Error retrieving top liked movies: {e}")
        return None


def __del__(self):
    self.conn.close()
