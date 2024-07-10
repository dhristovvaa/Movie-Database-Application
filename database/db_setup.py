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
