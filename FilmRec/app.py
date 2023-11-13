from identities import User, Movie
from ratings import RatingRegister, MovieRating
from recommendations import MovieRecommendation


user1 = User(1, 'User 1')
user2 = User(2, 'User 2')
user3 = User(3, 'User 3')

movie1 = Movie(1, 'Batman Begins')
movie2 = Movie(2, 'Liar Liar')
movie3 = Movie(3, 'The Godfather')

ratings = RatingRegister()
ratings.addRating(user1, movie1, MovieRating.FIVE)
ratings.addRating(user1, movie2, MovieRating.TWO)
ratings.addRating(user2, movie2, MovieRating.TWO)
ratings.addRating(user2, movie3, MovieRating.FOUR)

recommender = MovieRecommendation(ratings)

print(recommender.recommendMovie(user1)) # The Godfather
print(recommender.recommendMovie(user2)) # Batman Begins
print(recommender.recommendMovie(user3)) # Batman Begins
