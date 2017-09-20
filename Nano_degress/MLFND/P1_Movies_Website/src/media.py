import webbrowser

class Media():
    """
    This class represents a Movie object.
    
    The purpose of this class is to create a movie object with given
    attributes.

    Attributes:
        movie_title: A variable representing name or title of the movie.
        movie_storyline: A single sentence which summarizes the story.
        poster_image: An URL link that contains the poster image of the movie.
        trailer_youtube: An URL containing the official trailer of the movie.
    """
    
    VALID_RATINGS= ["G", "PG", "PG-13", "R"] #represents allowed ratings for a movie.
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Inits this object's attributes with the provided parameters."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens the YouTube trailer page of the movie.
        Args: self which represents a movie object.

        Returns: A web page playing the YouTube trailer of the self.

        Raises: An error if self is Null.
        """
        webbrowser.open(self.trailer_youtube_url)

    
