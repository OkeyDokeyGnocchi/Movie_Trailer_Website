import webbrowser


class Movie():
    """This class is used to generate the information for movies that
    the program needs to create the movie website fresh_tomatoes."""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, critic_score, movie_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.score = critic_score
        self.rating = movie_rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
