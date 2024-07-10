class Movie:
    def __init__(self, id, title, description, release_date, director, genre):
        self.id = id
        self.title = title
        self.description = description
        self.release_date = release_date
        self.director = director
        self.genre = genre

    def __str__(self):
        return f"ID: {self.id}\nTitle: {self.title}\nDescription: {self.description}\nRelease Date: {self.release_date}\nDirector: {self.director}\nGenre: {self.genre}\n"
