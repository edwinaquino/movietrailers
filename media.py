import webbrowser


class Movie():
    """
    Generates movie website for my favorite movies.
    Click on each movie to viewthe movie's trailer.
    """

    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube
    ):
        """
        This is the constructor method for the Movie class.
        It is used to setup all the variables in the Movie class.
        Reguired arguments are:
        Movie Title
        Movie Story Line/Description
        URL to Movie Poster Image (example: http://example.com/image.jpg)
        Youtube trailer URL. (example: https://www.youtube.com/watch?v=vKQi3bBA1y8)   # noqa
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Opens the youtube trailer by using the webbrowser module
        """
        webbrowser.open(self.trailer_youtube_url)
