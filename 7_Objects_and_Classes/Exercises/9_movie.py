class Movie:
    watched_movies = []
    def __init__(self, name, director):
        self.name = name
        self.director = director
        self.watched = False
    def change_name(self, new_name: str):
        self.name = new_name
    def change_director(self, new_director: str):
        self.director = new_director
    def watch(self):
        self.watched = True
        Movie.watched_movies.append(self)
    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {len(Movie.watched_movies)}"
