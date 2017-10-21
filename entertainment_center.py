import media
import fresh_tomatoes

rocky_horror = media.Movie("Rocky Horror",
                            "The story of a young couple's encounter with a"
                            "bizarre scientist.",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcSw4XUIY54oe7kXffs5aHPny8lz4v-j1A4XuLRC4ebfpHOHUfLL",  # noqa
                            "https://www.youtube.com/watch?v=Pgx1QZFNMz8",
                            "R", "80%")
  """Each instance listed in this page is a specific instance of class Movie.
  Each instance of class Movie is an individual movie that takes title,
  storyline, poster url, YouTube url, rating, and critical score as
  arguments during initialization.  These instances of class movie are
  the variables listed up to the point where the movies are selected as
  a list."""
donnie_darko = media.Movie("Donnie Darko", "A troubled teen follows a rabbit"
                            "into madness.",
                            "https://upload.wikimedia.org/wikipedia/en/d/db/Donnie_Darko_poster.jpg",  # noqa
                            "https://www.youtube.com/watch?v=rPeGaos7DB4",
                            "R", "86%")
zoolander = media.Movie("Zoolander",
                        "Male model Derek Zoolander finds himself in the"
                        "middle of a major conspiracy.",
                        "https://upload.wikimedia.org/wikipedia/en/7/7c/Movie_poster_zoolander.jpg",  # noqa
                        "https://www.youtube.com/watch?v=YtQq0T3ExLs",
                        "PG-13", "64%")
the_producers = media.Movie("The Producers",
                            "A washed up theatre producer and timid accountant"
                            "scheme to get rich.",
                            "https://upload.wikimedia.org/wikipedia/en/4/49/The_Producers_%282005%29.jpg",  # noqa
                            "https://www.youtube.com/watch?v=u36iNj52rac",
                            "PG-13", "50%")
road_to_el_dorado = media.Movie("The Road to El Dorado",
                                "Two con artists discover the golden city of"
                                "El Dorado.",
                                "https://upload.wikimedia.org/wikipedia/en/f/fa/Road_to_el_dorado_ver3.jpg",  # noqa
                                "https://www.youtube.com/watch?v=JcOfJwN0bdY",
                                "PG", "69%")
the_dark_knight = media.Movie("The Dark Knight",
                                "Batman sets out to dismantle the remaining"
                                "criminal organizations that plague the streets"
                                "of Gotham.",
                                "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",  # noqa
                                "https://www.youtube.com/watch?v=kmJLuwP3MbY",
                                "PG-13", "94%")

# Here we select the movies (variables above) to be used.
movies = [rocky_horror, donnie_darko, zoolander, the_producers,
          road_to_el_dorado, the_dark_knight]

# Open the newly-generated fresh_tomatoes HTML file.
fresh_tomatoes.open_movies_page(movies)
