import sqlite3

def create_tables():
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        release_date TEXT,
        director TEXT,
        genre TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS favorites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER,
        FOREIGN KEY (movie_id) REFERENCES movies(id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()

import sqlite3

def search_movies(query, search_type='title'):
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    if search_type == 'title':
        c.execute('SELECT * FROM movies WHERE title LIKE ?', (f'%{query}%',))
    elif search_type == 'genre':
        c.execute('SELECT * FROM movies WHERE genre = ?', (query,))
    else:
        conn.close()
        return []

    movies = c.fetchall()
    conn.close()

    return movies

# Define other database operations functions here (e.g., add_movie, list_movies, etc.)

