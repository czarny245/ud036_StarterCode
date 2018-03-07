import webbrowser
class Movie():
    
    def __init__(self, movie_title, poster_image,
                 trailer_youtube):
    
    """This class contains movie related information
        Args:
            movie_title (str): Include the movie title
            poster_image (str): Include a url to a movie poster image
            trailer_youtube (str): Include a url to a movie trailer video

        """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
