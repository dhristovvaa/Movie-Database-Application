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
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    c.execute('''
    INSERT INTO movies (title, description, release_date, director, genre)
    VALUES (?, ?, ?, ?, ?)
    ''', (title, desc, date, director, genre))

    conn.commit()
    conn.close()
    print("Movie added successfully")

def favorite_movie(movie_id):
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    c.execute('INSERT INTO favorites (movie_id) VALUES (?)', (movie_id,))

    conn.commit()
    conn.close()
    print(f"Movie with id {movie_id} added to favorites")

def categorize_movies(category):
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
        c.execute('SELECT genre, COUNT(*) as count FROM movies GROUP BY genre ORDER BY count DESC LIMIT 5')
    else:
        print(f"Unknown category: {category}")
        return

    movies = c.fetchall()

    for movie in movies:
        print(Movie(*movie))

    conn.close()
