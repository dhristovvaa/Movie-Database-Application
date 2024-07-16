import sys
from cli.commands import list_movies,add_movie, favorite_movie, categorize_movies, remove_movie,like_movie, get_top_liked_movies, movie_details, search_movies

def print_help():
    print("""
Usage:
    movlst                          List all movies
    movdt <movie_id>                Show details of a movie
    movsrch <query>                 Search for movies by title
    movadd <title> <desc> <date> <director> <genre>  Add a new movie
    movfv <movie_id>                Mark a movie as favorite
    movcat <category>               Categorize movies
""")


def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1]

    if command == 'movlst':
        list_movies()
    elif command == 'movdt' and len(sys.argv) == 3:
        movie_details(sys.argv[2])
    elif command == 'movsrch':
        if len(sys.argv) == 3:  # movsrch <query>
            query = sys.argv[2]
            movies = search_movies(query)
            if movies:
                for movie in movies:
                    print(
                        f"ID: {movie[0]}, Title: {movie[1]}, Description: {movie[2]}, Release Date: {movie[3]}, Director: {movie[4]}, Genre: {movie[5]}")


        elif len(sys.argv) == 4 and sys.argv[2] == 'genre':  # movsrch genre <genre>
            genre = sys.argv[3]
            movies = search_movies(genre, search_type='genre')
            if movies:
                for movie in movies:
                    print(
                        f"ID: {movie[0]}, Title: {movie[1]}, Description: {movie[2]}, Release Date: {movie[3]}, Director: {movie[4]}, Genre: {movie[5]}")

        else:
            print_help()
    elif command == 'movadd' and len(sys.argv) == 7:
        add_movie(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    elif command == 'movfv' and len(sys.argv) == 3:
        favorite_movie(sys.argv[2])
    elif command == 'movcat' and len(sys.argv) == 3:
        categorize_movies(sys.argv[2])
    elif command == 'movrm' and len(sys.argv) == 3:
        print("Calling remove_movie function")  # Debug
        remove_movie(sys.argv[2])
    elif command == 'movlike' and len(sys.argv) == 3:
        like_movie(sys.argv[2])
        print(f"Movie with id {sys.argv[2]} liked successfully.")
    elif command == 'movcat' and sys.argv[2] == 'liked':
        top_movies = get_top_liked_movies()
        for movie in top_movies:
            print(
                f"ID: {movie[1]}\nTitle: {movie[0]}\nDescription: {movie[2]}\nRelease Date: {movie[3]}\nDirector: {movie[4]}\nGenre: {movie[5]}\nLikes: {movie[6]}\n")
    else:
        print_help()


def print_help():
    print("Usage:")
    print("movadd <title> <description> <release_date> <director> <genre>")
    print("movfav <movie_id>")
    print("movcat <genre>")
    print("movcat liked")
    print("movrm <movie_id>")
    print("movlike <movie_id>")


if __name__ == '__main__':
    main()
