import webbrowser


class Movie():
    """ This class will allow the user the store information about movies.
    Attributes:
       movie_title: A string showing the name of a movie.
       movie_storyline: A brief description of the movies story.
       poster_image_url: A url linking to a pictrue of the movie poster
       traier_youtube_url: A url linking to a youtube trailer of the movie.
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image_url,
                 trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
