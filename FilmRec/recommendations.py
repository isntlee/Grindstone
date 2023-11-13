class MovieRecommendation:
    def __init__(self, ratings):
        self._movieRatings = ratings

    def recommendMovie(self, user):
        if len(self._movieRatings.getUserMovies(user)) == 0:
            return self._recommendMovieNewUser()
        else:
            return self._recommendMovieExistingUser(user)

    def _recommendMovieNewUser(self):
        best_movie = None
        best_rating = 0
        for movie in self._movieRatings.getMovies():
            rating = self._movieRatings.getAverageRating(movie)
            if rating > best_rating:
                best_movie = movie
                best_rating = rating
        return best_movie.getTitle() if best_movie else None

    def _recommendMovieExistingUser(self, user):
        best_movie = None
        similarity_score = float('inf') # Lower is better

        for reviewer in self._movieRatings.getUsers():
            if reviewer.getId() == user.getId():
                continue
            score = self._getSimilarityScore(user, reviewer)
            if score < similarity_score:
                similarity_score = score
                recommended_movie = self._recommendUnwatchedMovie(user, reviewer)
                best_movie = recommended_movie if recommended_movie else best_movie
        return best_movie.getTitle() if best_movie else None

    def _getSimilarityScore(self, user1, user2):
        user1_id = user1.getId()
        user2_id = user2.getId()
        user2_movies = self._movieRatings.getUserMovies(user2)
        score = float('inf') # Lower is better

        for movie in user2_movies:
            cur_movie_ratings = self._movieRatings.getMovieRatings(movie)
            if user1_id in cur_movie_ratings:
                score = 0 if score == float('inf') else score
                score += abs(cur_movie_ratings[user1_id].value - cur_movie_ratings[user2_id].value)
        return score

    def _recommendUnwatchedMovie(self, user, reviewer):
        user_id = user.getId()
        reviewer_id = reviewer.getId()
        best_movie = None
        best_rating = 0

        reviewer_movies = self._movieRatings.getUserMovies(reviewer)
        for movie in reviewer_movies:
            cur_movie_ratings = self._movieRatings.getMovieRatings(movie)
            if user_id not in cur_movie_ratings and cur_movie_ratings[reviewer_id].value > best_rating:
                best_movie = movie
                best_rating = cur_movie_ratings[reviewer_id].value
        return best_movie
