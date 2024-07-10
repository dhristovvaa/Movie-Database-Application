import sys
from cli.commands import list_movies, movie_details, search_movies, add_movie, favorite_movie, categorize_movies

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
    elif command == 'movsrch' and len(sys.argv) == 3:
        search_movies(sys.argv[2])
    elif command == 'movadd' and len(sys.argv) == 7:
        add_movie(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    elif command == 'movfv' and len(sys.argv) == 3:
        favorite_movie(sys.argv[2])
    elif command == 'movcat' and len(sys.argv) == 3:
        categorize_movies(sys.argv[2])
    else:
        print_help()

if __name__ == '__main__':
    main()
