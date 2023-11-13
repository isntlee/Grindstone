from enum import Enum

class MovieRating(Enum):
    NOT_RATED = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class RatingRegister:
    def __init__(self):
        self._userMovies = {}   # Map<UserId, List<Movie>>
        self._movieRatings = {} # Map<MovieId, Map<UserId, Rating>>

        self._movies = []       # List<Movie>
        self._users = []        # List<User>

    def addRating(self, user, movie, rating):
        if movie.getId() not in self._movieRatings:
            self._movieRatings[movie.getId()] = {}
            self._movies.append(movie)
        if user.getId() not in self._userMovies:
            self._userMovies[user.getId()] = []
            self._users.append(user)
        self._userMovies[user.getId()].append(movie)
        self._movieRatings[movie.getId()][user.getId()] = rating

    def getAverageRating(self, movie):
        if movie.getId() not in self._movieRatings:
            return MovieRating.NOT_RATED.value
        ratings = self._movieRatings[movie.getId()].values()
        ratingValues = [rating.value for rating in ratings]
        return sum(ratingValues) / len(ratings)

    def getUsers(self):
        return self._users

    def getMovies(self):
        return self._movies

    def getUserMovies(self, user):
        return self._userMovies.get(user.getId(), [])

    def getMovieRatings(self, movie):
        return self._movieRatings.get(movie.getId(), {})
