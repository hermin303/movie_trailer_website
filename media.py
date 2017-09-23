# importing the webbrowser to display the web application
import webbrowser

# Creating class to set structure for the movies' features


class Movie:

    def __init__(self,
                 movie_title,
                 movie_genre,
                 movie_director,
                 movie_year,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.genre = movie_genre
        self.director = movie_director
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Creating the instance method to display the movie trailer


def show_trailer(self):

    webbrowser.open(self.trailer_youtube_url)
