import webbrowser


class Movie():
    """This class is used to generate the information for movies that
    the program needs to create the movie website fresh_tomatoes."""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, critic_score, movie_rating):
        """This function is used to initialize each instance of the movie class
        with the various variables needed to flesh out the content on the
        website.  These variables (the input) are the title, story, poster URL,
        trailer URL, critical score, and rating.  The output is the generated
        instance of class Movie."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.score = critic_score
        self.rating = movie_rating

    def show_trailer(self):
        """This function is used to open the trailer when the movie poster
        image on the website is clicked.  This causes the 'popout' trailer
        feature on the page.  The only notable input is the instance's
        (YouTube) trailer URL."""
        webbrowser.open(self.trailer_youtube_url)
